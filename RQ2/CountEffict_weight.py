import json

file_path = "human-eval-v2-20210705.jsonl"
dict_all = {}
dict_entry = {}
dict_candidate = {}
dict_tests = {}
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        json_data = json.loads(line)
        dict_all[json_data["task_id"]] = json_data["prompt"]
        dict_entry[json_data["task_id"]] = json_data["entry_point"]
        dict_tests[json_data["task_id"]] = json_data["test"]
        dict_candidate[json_data["task_id"]] = json_data["canonical_solution"]

respath = "RQ2-result1201\\"
listmodel = ["codegen", "incoder" , "davinci", "chatgpt"]
postmodel = ["chatgpt", "gpt4"]
for genmodel in listmodel:
    for pmodel in postmodel:
        for j in range(1, 4):
            if not ((pmodel == "chatgpt" and str(j) == "1") or pmodel == "gpt4" and str(j) == "2"):
                continue
            ttnopost = 0
            # file_name = respath + "record_humaneval_" + genmodel + "_testcases_unique_in_assert_args_result_new_" + pmodel + str(
            #     j) + "_nof.jsonl"
            file_name = respath + "record_humaneval_" + genmodel + "_testcases_unique_in_assert_args_result_new_" + pmodel + str(
                j) + ".jsonl"
            # print(file_name)
            # file_name=respath+"record_humaneval_"+genmodel+"_testcases_unique_in_assert_args_result_new_"+pmodel+str(j)+".jsonl"
            f = open(file_name, 'r', encoding="utf-8")
            content_list_chatgpt = f.read().rstrip("\n").split("\n")
            f.close()
            totfalse = 0
            tottrue = 0
            identifyfalse = 0
            truetofalse = 0
            dict_totfalse = {}
            dict_tottrue = {}
            dict_identifyfalse = {}
            dict_truetofalse = {}
            for i in range(0, 164):
                dict_totfalse["HumanEval/" + str(i)] = 0
                dict_tottrue["HumanEval/" + str(i)] = 0
                dict_identifyfalse["HumanEval/" + str(i)] = 0
                dict_truetofalse["HumanEval/" + str(i)] = 0
            for content_chatgpt in content_list_chatgpt:
                content_chatgpt_json = json.loads(content_chatgpt)

                if content_chatgpt_json["label"]:
                    tottrue += 1
                    dict_tottrue[content_chatgpt_json["task_id"]] += 1
                    if not content_chatgpt_json["res"]:
                        truetofalse += 1
                        dict_truetofalse[content_chatgpt_json["task_id"]] += 1
                else:
                    if not content_chatgpt_json["res"]:
                        identifyfalse += 1
                        dict_identifyfalse[content_chatgpt_json["task_id"]] += 1
                    else:
                        pass
                    totfalse += 1
                    dict_totfalse[content_chatgpt_json["task_id"]] += 1

            print(genmodel + "_" + pmodel + "_" + str(j))
            all_true_notzero = 0
            all_false_notzero = 0
            true_tofalse_rate_tot = 0
            idenfalse_rate_tot = 0
            prec_rate_tot = 0
            recal_rate_tot = 0
            f1_rate_tot = 0
            zzz = 0
            num_f1_zero=0
            num_tpfn_zero = 0
            for task_id in dict_tottrue.keys():
                all_true = dict_tottrue[task_id]
                all_false = dict_totfalse[task_id]
                truetofalsetemp = dict_truetofalse[task_id]
                idenfalsetemp = dict_identifyfalse[task_id]
                TP = all_true - truetofalsetemp
                FN = truetofalsetemp
                TN = idenfalsetemp
                FP = all_false - idenfalsetemp
                if TP == 0:
                    prec = 0
                    # print("g")
                    # continue
                else:
                    prec = (TP) * 1.0 / (TP + FP)
                if TP == 0:
                    recall = 0
                    # print("gg")
                    # continue
                else:
                    recall = (TP) * 1.0 / (TP + FN)

                if TP == 0:
                    # continue
                    f1 = 0
                    num_f1_zero+=1
                    # print("ggg")
                    # continue
                else:
                    # print(TP,FP,FN)
                    f1 = (2 * prec * recall) / (prec + recall)
                if TP+FN==0:
                    num_tpfn_zero+=1
                prec_rate_tot += prec
                recal_rate_tot += recall
                f1_rate_tot += f1
                zzz += 1
                # print(prec, recall, f1)
                # if all_true!=0:
                #     all_true_notzero+=1
                #     true_tofalse_rate_tot+=truetofalsetemp*1.0/all_true
                # if all_false!=0:
                #     all_false_notzero+=1
                #     idenfalse_rate_tot+=idenfalsetemp*1.0/all_false
            # print(round((idenfalse_rate_tot*1.0/all_false_notzero)*100,2),round((true_tofalse_rate_tot*1.0/all_true_notzero)*100,2))
            # print("tot_true:"+str(tottrue),"truetofalse:"+str(truetofalse),"rate:"+str(truetofalse*1.0/tottrue))
            # print("tot_false:"+str(totfalse),"tot_identifyfalse:"+str(identifyfalse),"rate:"+str(identifyfalse*1.0/totfalse))
            print(round((prec_rate_tot * 1.0 / zzz) , 3), round((recal_rate_tot * 1.0 / zzz) , 3),
                  round((((2 * prec_rate_tot * recal_rate_tot) / (prec_rate_tot + recal_rate_tot) )/ zzz) , 3))
            print(str(round((prec_rate_tot * 1.0 / zzz), 3))+" & "+ str(round((recal_rate_tot * 1.0 / zzz), 3))+" & "+
                  str(round((((2 * prec_rate_tot * recal_rate_tot) / (prec_rate_tot + recal_rate_tot)) / zzz), 3)))

            print(zzz,num_f1_zero,num_tpfn_zero)
# print(tottrue,totfalse)
# print(truetofalse,identifyfalse)
