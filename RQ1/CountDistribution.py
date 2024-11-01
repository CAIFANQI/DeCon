dictt_before={}

import os
import json
file_dir="C:\\Users\yh199\Downloads\isstafigure\\withoutduplicated\\"
# file_dir="C:\\Users\yh199\Documents\WeChat Files\wxid_mnexmfkh3xnr22\FileStorage\File\\2023-12\\args_new_2\\"
files=os.listdir(file_dir)
all_before=0
all_false_before=0
all_after=0
all_false_after=0
for file in files:
    # print(file)
    model_name=file.split("-")[0]
    tot_assertion_num=0
    correct_assertion_num = 0
    incorrect_assertion_num = 0
    error_assertion_num = 0
    f=open(file_dir+file,'r',encoding="utf-8")
    content_list=f.read().rstrip("\n").split("\n")
    f.close()
    for content in content_list:
        content_json=json.loads(content)
        # print(content_json.keys())
        tot_assertion_num += content_json["total assertion number"]
        correct_assertion_num += content_json["total correct assertion number"]
        incorrect_assertion_num += content_json["total false assertion number"]
        for keyy in content_json.keys():
            if keyy=="doesn't pass assertion error number" or keyy =="total assertion number" or keyy =="task_id" or keyy=="total correct assertion number" or keyy=="total false assertion number":
                continue
            # print(keyy)
            error_assertion_num+=content_json[keyy]


        # error_assertion_num += content_json["total error number"]
        # tot_assertion_num+=content_json["total assertion number"]
        # correct_assertion_num += content_json["total correct assertion number"]
        # incorrect_assertion_num += content_json["total false assertion number"]


        # error_assertion_num+=content_json["total error number"]
        # print(content_json.keys())
        #
        # for keyy in content_json.keys():
        #     pass
        # break
    print(file)
    incorrect_assertion_num -= error_assertion_num
    all_false_before+=incorrect_assertion_num
    all_before+=tot_assertion_num
    print(tot_assertion_num,correct_assertion_num,incorrect_assertion_num,error_assertion_num)
    print("correct",correct_assertion_num,correct_assertion_num*1.0/tot_assertion_num)
    print("incorrect", incorrect_assertion_num, incorrect_assertion_num * 1.0 / tot_assertion_num)
    print("error", error_assertion_num, error_assertion_num * 1.0 / tot_assertion_num)
    dictt_before[model_name]=(tot_assertion_num)
    # print(correct_assertion_num+incorrect_assertion_num+error_assertion_num)

    # break
dictt_after={}
# file_dir="C:\\Users\yh199\Downloads\isstafigure\\withoutduplicated\\"
file_dir="C:\\Users\yh199\Documents\WeChat Files\wxid_mnexmfkh3xnr22\FileStorage\File\\2023-12\\args_new_2\\"
files=os.listdir(file_dir)
for file in files:
    # print(file)
    model_name=file.split("_")[0]
    tot_assertion_num=0
    correct_assertion_num = 0
    incorrect_assertion_num = 0
    error_assertion_num = 0
    f=open(file_dir+file,'r',encoding="utf-8")
    content_list=f.read().rstrip("\n").split("\n")
    f.close()
    for content in content_list:
        content_json=json.loads(content)
        # print(content_json.keys())
        # tot_assertion_num += content_json["total assertion number"]
        # correct_assertion_num += content_json["total correct assertion number"]
        # incorrect_assertion_num += content_json["total false assertion number"]
        # for keyy in content_json.keys():
        #     if keyy=="doesn't pass assertion error number" or keyy =="total assertion number" or keyy =="task_id" or keyy=="total correct assertion number" or keyy=="total false assertion number":
        #         continue
        #     # print(keyy)
        #     error_assertion_num+=content_json[keyy]


        error_assertion_num += content_json["total error number"]
        tot_assertion_num+=content_json["total assertion number"]
        correct_assertion_num += content_json["total correct assertion number"]
        incorrect_assertion_num += content_json["total false assertion number"]

        # error_assertion_num+=content_json["total error number"]
        # print(content_json.keys())
        #
        # for keyy in content_json.keys():
        #     pass
        # break
    print(file)
    # incorrect_assertion_num -= error_assertion_num
    all_after +=tot_assertion_num
    all_false_after+=incorrect_assertion_num
    print(tot_assertion_num,correct_assertion_num,incorrect_assertion_num,error_assertion_num)
    print("correct",correct_assertion_num,correct_assertion_num*1.0/tot_assertion_num)
    print("incorrect", incorrect_assertion_num, incorrect_assertion_num * 1.0 / tot_assertion_num)
    print("error", error_assertion_num, error_assertion_num * 1.0 / tot_assertion_num)
    dictt_after[model_name]=(tot_assertion_num)
print(dictt_before)
print(dictt_after)
for keyy in dictt_before.keys():
    print(keyy,dictt_before[keyy],dictt_after[keyy],dictt_after[keyy]*1.0/dictt_before[keyy])
totbefore=0
totafter=0

for keyy in dictt_before.keys():
    totbefore+=dictt_before[keyy]
for keyy in dictt_after.keys():
    totafter+=dictt_after[keyy]

print(totbefore,totafter)

print(all_before,all_false_before,all_false_before*1.0/all_before)
print(all_after,all_false_after,all_false_after*1.0/all_after)