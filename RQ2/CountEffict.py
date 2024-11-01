import json

file_path="human-eval-v2-20210705.jsonl"
dict_all={}
dict_entry={}
dict_candidate={}
dict_tests={}
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        json_data = json.loads(line)
        dict_all[json_data["task_id"]]=json_data["prompt"]
        dict_entry[json_data["task_id"]]=json_data["entry_point"]
        dict_tests[json_data["task_id"]]=json_data["test"]
        dict_candidate[json_data["task_id"]]=json_data["canonical_solution"]

respath="RQ2-result1201\\"
listmodel=["codegen","davinci","chatgpt","incoder"]
postmodel=["chatgpt","gpt4"]
for genmodel in listmodel:
    for pmodel in postmodel:
        for j in range(1,4):
            file_name=respath+"record_humaneval_"+genmodel+"_testcases_unique_in_assert_args_result_new_"+pmodel+str(j)+".jsonl"
            f=open(file_name,'r',encoding="utf-8")
            content_list_chatgpt=f.read().rstrip("\n").split("\n")
            f.close()
            totfalse=0
            tottrue=0
            identifyfalse=0
            truetofalse=0
            dict_totfalse= {}
            dict_tottrue={}
            dict_identifyfalse={}
            dict_truetofalse={}
            for i in range(0,164):
                dict_totfalse["HumanEval/"+str(i)]=0
                dict_tottrue["HumanEval/"+str(i)]=0
                dict_identifyfalse["HumanEval/"+str(i)]=0
                dict_truetofalse["HumanEval/"+str(i)]=0
            for content_chatgpt in content_list_chatgpt:
                content_chatgpt_json=json.loads(content_chatgpt)
                if content_chatgpt_json["label"]:
                    tottrue+=1
                    dict_tottrue[content_chatgpt_json["task_id"]]+=1
                    if not content_chatgpt_json["res"]:
                        truetofalse+=1
                        dict_truetofalse[content_chatgpt_json["task_id"]]+=1
                else:
                    if not content_chatgpt_json["res"]:
                        identifyfalse+=1
                        dict_identifyfalse[content_chatgpt_json["task_id"]]+=1
                    else:
                        pass
                    totfalse+=1
                    dict_totfalse[content_chatgpt_json["task_id"]]+=1
            print(genmodel+"_"+pmodel+"_"+str(j))
            print("tot_true:"+str(tottrue),"truetofalse:"+str(truetofalse),"rate:"+str(truetofalse*1.0/tottrue))
            print("tot_false:"+str(totfalse),"tot_identifyfalse:"+str(identifyfalse),"rate:"+str(identifyfalse*1.0/totfalse))

# print(tottrue,totfalse)
# print(truetofalse,identifyfalse)