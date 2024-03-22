
import subprocess
listt=[]
f=open("input38.txt")
cccc=f.read()
f.close()
input_38=cccc
# setonly_id_list=["HumanEval/32"]
dictt_tests={}
all_tests_path="/home/yuhao/falseoraclereduce/testcase"
for i in range(0,164):
    file_contain_path = all_tests_path + "/" + str(i) + ".txt"
    f = open(file_contain_path, 'r')
    content_temp = f.read()
    f.close()
    dictt_tests["HumanEval/"+str(i)]=content_temp


import json
import sys
inputfile=sys.argv[1]
outputfile=sys.argv[2]
postcorrectfile=sys.argv[3]
model = outputfile.split('_')[2]+postcorrectfile.split('_')[1]
f_codex_oracle=open(inputfile,'r',encoding="utf-8")

fwriteres=open(outputfile,'w',encoding="utf-8")

content_codex_oracle=f_codex_oracle.read().rstrip("\n").split("\n")
f_codex_oracle.close()
print(len(content_codex_oracle))

dictt_generate_oracle_origin={}
dictt_generate_oracle_formate={}
for oracle_codex in content_codex_oracle:
    oracle_codex_json=json.loads(oracle_codex)
    list_formate=[]
    for assertion in oracle_codex_json["assertions"]:
        # print(assertion["isT"])
        # print(type(assertion["isT"]))
        # if assertion["isT"] or "incomplete"==assertion["isT"]:
        #     continue
        # print(oracle_codex_json["task_id"])
        # print(assertion.keys(),assertion["isT"])
        # print(assertion["args_and_result"])

        # if assertion["isT"]=="false":
        list_formate.append((assertion["assert"],assertion["args_and_result"],assertion["isT"]))
    dictt_generate_oracle_formate[oracle_codex_json["task_id"]]=list_formate

zz=0
f_postcondition_trim_correct=open(postcorrectfile,'r',encoding="utf-8")
content_list=f_postcondition_trim_correct.read().rstrip("\n").split("\n")
f_postcondition_trim_correct.close()
all_error_assert=0
find_error_assert=0
zzallfalseoracle=0
all_num=0
for keyy in dictt_generate_oracle_formate.keys():
    zzallfalseoracle+=len(dictt_generate_oracle_formate[keyy])
for posts in content_list:
    post_json=json.loads(posts)
    # print(post_json.keys())
    # break
    # if post_json["task_id"] in setonly_id_list:
    #     continue
    #if post_json["task_id"] !="HumanEval/26":
    #    continue
    correct_post=post_json["generated_postcondition_set"]
    if len(correct_post)==0:
        zz+=1
        continue
    input_list=dictt_generate_oracle_formate[post_json["task_id"]]
    # print(len(input_list))
    for ttt in input_list:
        assertion_temp=ttt[1]
        assertion_isT=ttt[2]
        if post_json["task_id"]=="HumanEval/38":
            assertion_temp=input_38+"\n"+ttt[1]
        if post_json["task_id"]=="HumanEval/2":
            newassert = ""
            for ll in assertion_temp.split("\n"):
                if ll.startswith("return_val="):
                    if ll.find(".") < 0:
                        ll += ".0"
                newassert += ll
                newassert += "\n"
        f_temp = open(f"/home/yuhao/falseoraclereduce/selectpostcondition_{model}_idenfalse118.py", 'w',
                      encoding="utf-8")
        f_temp.write("import sys\nimport math\n")
        if post_json["task_id"] == "HumanEval/2":
            f_temp.write(newassert+ "\n")
            strw = "import sys\nimport math\n" + newassert + "\n"
        else:
            strw = "import sys\nimport math\n" + assertion_temp + "\n"
            f_temp.write(assertion_temp+ "\n")
        # f_temp.write(assertion_temp+ "\n")
        # strw="import sys\n"+assertion_temp+ "\n"
        for post_condition in correct_post:
            strw += post_condition+"\n"
            f_temp.write(post_condition+"\n")
        f_temp.close()
        try:
            process = subprocess.Popen([sys.executable,
                                        f"/home/yuhao/falseoraclereduce/selectpostcondition_{model}_idenfalse118.py"],
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output, error = process.communicate(timeout=30)
        except:
            process.kill()
            print("error:", assertion_temp)
            continue
        if process.returncode != 0:
            dicttempwrite = {"task_id": post_json["task_id"], "content": strw,"assertion":ttt[0],"label":assertion_isT,"res":False}
            fwriteres.write(json.dumps(dicttempwrite) + "\n")
        else:
            dicttempwrite = {"task_id": post_json["task_id"], "content": strw, "assertion": ttt[0],
                             "label": assertion_isT, "res": True}
            fwriteres.write(json.dumps(dicttempwrite) + "\n")
        all_num+=1
        print(all_num)
        # print(find_error_assert,all_error_assert)
            # print(l)
        # break

fwriteres.close()



# 14143 26008   54.4%
