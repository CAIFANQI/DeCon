import re
import sys
import subprocess
import multiprocessing
from subprocess import TimeoutExpired

class Process(multiprocessing.Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.sut, *_ = kwargs['args']
        self._pconn, self._cconn = multiprocessing.Pipe()
        self._exception = None

    def run(self):
        try:
            multiprocessing.Process.run(self)
            self._cconn.send(None)
        except Exception as exception:  # pylint: disable=broad-except
            self._cconn.send(exception)

    def join(self, timeout):  # pylint: disable=signature-differs
        super().join(timeout)

        if self.is_alive():
            # self._cconn.send(TimeoutError(f'function {self.sut.__name__} execution time exceeds {timeout}s'))
            self.terminate()
        super().join()

    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception


json_file="/home/huangjiaming/bytedance/HumanEval_incoder6B_temp0.8_topp0.95_num100_max300_test_case.jsonl"
solution_file ="/home/huangjiaming/bytedance/human-eval-v2-20210705.jsonl"
f_json_file=open(json_file, 'r', encoding="utf-8")
content=f_json_file.read().rstrip("\n").split("\n")
f_json_file.close()

f_json_file=open(solution_file, 'r', encoding="utf-8")
solution=f_json_file.read().rstrip("\n").split("\n")
f_json_file.close()
list_all=[]

import json
def generate_jsonl(dict_list, f_name):
    with open(f_name, 'w', encoding='utf-8') as f:
        for i in dict_list:
            f.write(json.dumps(i)+'\n')

def find_function_head(prompt, name):
    n_idx = prompt.find(name)
    stop_idx = prompt.find('\n', n_idx)
    return prompt[:stop_idx+1]

dict_l = []
method_name=[]
#dm = "sum_squares"
#duplicated_name = ["sum_squares", "add", "correct_bracketing", "triangle_area", "solve", "sort_array"]
with open("incoder_idx_corr.json",'r',encoding="utf-8") as f:
    idx_corr = json.load(f)
print(idx_corr)

for s in solution:
    temp_list_assertions = []
    s_json = json.loads(s)
    tmp_dict = {}
    tmp_dict["task_id"] = s_json["task_id"]
    tmp_dict["candidate_code"] = []
    tmp_dict["assertions"] = []
    m_name = s_json["entry_point"]
    fh = find_function_head(s_json["prompt"], m_name)
    method_name.append(m_name)
    target = fh + s_json["canonical_solution"]
    tmp_dict["candidate_code"].append(target)
    dict_l.append(tmp_dict)

print(len(method_name))
ap = re.compile(r"assert ")
#debug_dict_ls = []
for mi, m_name in enumerate(method_name):
    temp_list_assertions = []
    mp = re.compile(r'(?<=\b)'+m_name+r' ?\(')
    c = content[idx_corr[str(mi)]]
    c_json=json.loads(c)
    for i,l in enumerate(c_json["samples"]):
        l_list=l.split("\n")
        for j, lll in enumerate(l_list):
            if i==0 and j==0:
                temp_list_assertions.append("assert "+ lll)
            elif ap.match(lll) and mp.search(lll):
                temp_list_assertions.append(lll)
    list_all.append(temp_list_assertions)

print(len(list_all))
dict_err_ls = []
for i in range(len(dict_l)):
    tot_false_num, tle_num, nameerr_num, typeerr_num, incomplete_num, assertfalse_num = (0,0,0,0,0,0)
    content = dict_l[i]["candidate_code"][0]
    state_dict = {"task_id":dict_l[i]["task_id"]}
    tot = len(list_all[i])
    for l in list_all[i]:
        new_data=content+"\n"+l
        f=open("executefunction.py",'w',encoding="utf-8")
        f.write(new_data)
        f.close()
        tmp_assert = {"assert":l, "isT":True}
        try:
            process = subprocess.Popen([sys.executable, "/home/huangjiaming/bytedance/executefunction.py"],
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output, error = process.communicate(timeout=10)
        except TimeoutExpired:
            print("error:",l)
            process.kill()
            output, error = process.communicate()
            print("-------")
            tot_false_num += 1
            tle_num += 1
            tmp_assert["isT"] = "Time Limit Exceed"
        else:
            if process.returncode != 0:
                print(l)
                print(output)
                print("---------")
                tot_false_num += 1
                if b"NameError" in output:
                    nameerr_num += 1
                    tmp_assert["isT"] = "external variables not defined in assert line"
                elif b"TypeError" in output:
                    typeerr_num += 1
                    tmp_assert["isT"] = "illegal type for some parameters"
                elif b"SyntaxError" in output:
                    incomplete_num += 1
                    tmp_assert["isT"] = "incomplete"
                else:
                    assertfalse_num += 1
                    tmp_assert["isT"] = False
        finally:
            dict_l[i]["assertions"].append(tmp_assert)
    print(tot_false_num)
    state_dict["total assertion number"] = tot
    state_dict["total correct assertion number"] = tot - tot_false_num
    state_dict["total false assertion number"] = tot_false_num
    state_dict["timeout error number"] = tle_num
    state_dict["undefined name error number"] = nameerr_num
    state_dict["parameters'type error number"] = typeerr_num
    state_dict["incomplete number"] = incomplete_num
    state_dict["doesn't pass assertion error number"] = assertfalse_num
    dict_err_ls.append(state_dict)

#print(false_num)
jsonl_file = "human-eval-incoder_testcases.jsonl"
count_file = "incoder-testcases-statistic.jsonl"
generate_jsonl(dict_l, jsonl_file)
generate_jsonl(dict_err_ls, count_file)



# list_error_oracle1=[]
# false_num1=0
# for l in list_error_oracle:
#     input_value1=[]
#     input_value2=0.0
#     output=True
#     if l.find(")")>0 and l.find("has_close_elements(")>0:
#         l_l=l.split(")")
#         if len(l_l)!=2:
#             continue
#         if l_l[-1]=="":
#             if l_l[0].find("assert not "):
#                 tempa=l_l[0].split("has_close_elements(")[1]
#                 tempaa = tempa.split("]")[0]
#                 tempbb = tempaa.split(", ")[1].lstrip(", ")
#                 tempaa+="]"
#                 output="False"
#             else:
#                 tempa=l_l[0].split("has_close_elements(")[1]
#                 tempaa = tempa.split("]")[0]
#                 tempbb = tempaa.split(", ")[1].lstrip(", ")
#                 tempaa+="]"
#                 output="True"
#             print(tempaa,tempbb,output)
#
#             f = open("backuppostcondition.py", 'r', encoding="utf-8")
#             content = f.read()
#             f.close()
#             str1="numbers="+tempaa
#             str2="threshold="+tempbb
#             str3 = "result=" + output
#             new_data = str1+"\n"+str2+"\n"+str3+"\n"+ l
#             f = open("executepostcondition.py", 'w', encoding="utf-8")
#             f.write(new_data)
#             f.close()
#             try:
#                 process = subprocess.Popen([sys.executable,
#                                             "C:\\Users\yh199\PycharmProjects\pythonProject\\bytedancebench\\executepostcondition.py"],
#                                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#                 output, error = process.communicate(timeout=30)
#             except:
#                 print("error:", l)
#                 continue
#             if process.returncode != 0:
#                 print(l)
#                 list_error_oracle1.append(l)
#                 false_num1 += 1
# print("---------------------")
# for l in list_error_oracle1:
#     print(l)
# print(false_num1)


# import json
# def read_jsonl(file_path):
#     results = []
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             json_data = json.loads(line)
#             results.append(json_data)
#             print(json_data["canonical_solution"])
#             print(json_data["task_id"])
#             print(json_data["prompt"])
#             print("------------------------------")
#             break
#             # print(json_data["entry_point"])
#
#
#     return results
#
# file_path = 'C:\\Users\yh199\Downloads\HumanEval.jsonl\\human-eval-v2-20210705.jsonl'  # Replace with the path to your JSONL file
