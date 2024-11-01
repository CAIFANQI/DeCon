# err_path="C:\\Users\yh199\PycharmProjects\pythonProject\\reducefalseoracle\groundtruth\\errpythonfile"
f=open("input38.txt")
cccc=f.read()
f.close()
input_38=cccc
listt=[]
import os
import subprocess
import sys
only_id_list=[]
# for file in os.listdir(err_path):
#     listt.append(file.split("_")[0]+"/"+file.split("_")[1])
#     only_id_list.append(file.split("_")[1])
# setlist=list(set(listt))
# print(setlist)
# print(len(setlist))
# setonly_id_list=list(set(setlist))
setonly_id_list=["HumanEval/32"]
dictt_tests={}
all_tests_path="/home/yuhao/falseoraclereduce/testcase"
for i in range(0,164):
    file_contain_path = all_tests_path + "/" + str(i) + ".txt"
    f = open(file_contain_path, 'r')
    content_temp = f.read()
    f.close()
    dictt_tests["HumanEval/"+str(i)]=content_temp
import json
f_postcondition=open("invovle_generate_gpt4-1_b.jsonl",'r',encoding="utf-8")

# f_postcondition=open("generatedpostcondtion_chatgpt1.jsonl",'r',encoding="utf-8")
content_post_list=f_postcondition.read().rstrip("\n").split("\n")
f_postcondition.close()
print(len(content_post_list))

f_postcondition_trim_correct=open("invovle_generate_gpt4-1_correct.jsonl",'w',encoding="utf-8")


# f_postcondition=open("/home/yuhao/1125oracle/gpt4/generatedpostcondtiongpt4-5-0.8-1.jsonl",'r',encoding="utf-8")
# content_post_list=f_postcondition.read().rstrip("\n").split("\n")
# f_postcondition.close()
# print(len(content_post_list))
#
# f_postcondition_trim_correct=open("/home/yuhao/1125oracle/gpt4/generatedpostcondtion_correct_gpt4-5-0.8-1.jsonl",'w',encoding="utf-8")
zz=0
for posts in content_post_list:
    post_json=json.loads(posts)
    # print(post_json.keys())
    # break
    correct_postcondition=[]
    # if post_json["task_id"] in setonly_id_list:
    #     continue

    input_list=dictt_tests[post_json["task_id"]].rstrip("\n").rstrip("-------------------").split("-------------------\n")
    post_ctemp=post_json["generated_postcondition"]
    post_ctemp_set=list(set(post_json["generated_postcondition"]))
    for post_condition in post_json["generated_postcondition"]:
        print(post_condition)
        f_temp=open("selectpostconditionttt.py",'w',encoding="utf-8")
        f_temp.write("import sys\n")
        for ll in input_list:
            f_temp.write(ll+"\n")
            f_temp.write(post_condition+"\n")
        f_temp.close()
        try:
            process = subprocess.Popen([sys.executable,
                                        "selectpostconditionttt.py"],
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output, error = process.communicate(timeout=30)
        except:
            print("error:", post_condition)
            continue
        if process.returncode == 0:
            correct_postcondition.append(post_condition)
            # print(l)
        # break
    correct_postcondition_set=list(set(correct_postcondition))
    print(len(correct_postcondition),len(post_json["generated_postcondition"]))
    post_json["correct_posts"]=correct_postcondition
    post_json["correct_posts_set"] = correct_postcondition_set
    post_json["generated_postcondition_set"]=post_ctemp_set
    f_postcondition_trim_correct.write(json.dumps(post_json)+"\n")

print(zz)




