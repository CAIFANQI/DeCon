import json
import re
import os

solution_file ="..\\human-eval-v2-20210705.jsonl"
with open(solution_file, 'r', encoding="utf-8") as f_json_file:
    solution=f_json_file.read().rstrip("\n").split("\n")

brackets_map = {')': '(', ']': '[', '}': '{'}

def parse_args(s):
    arg_list = []
    brackets_stack = []
    in_string=0
    arg = ''
    for c in s:
        if c==' ' and brackets_stack==[] and in_string==0:
            continue
        elif c==',':
            if brackets_stack==[] and not in_string:
                arg_list.append(arg)
                arg=''
                continue
        elif c=='(' or c=='[' or c=='{':
            brackets_stack.append(c)
        elif c==')' or c==']' or c=='}':
            if brackets_stack==[] or brackets_stack[-1]!=brackets_map[c]:
                return "wrong type args"
            brackets_stack.pop()
        elif c=='\'' or c=='\"':
            in_string ^= 1
        arg = arg + c
    if arg!='':
        arg_list.append(arg)
    return arg_list

def generate_jsonl(dict_list, f_name):
    with open(f_name, 'w', encoding='utf-8') as f:
        for i in dict_list:
            f.write(json.dumps(i)+'\n')

def find_function_argname(prompt, name):
    n_idx = prompt.find(name)
    stop_idx = prompt.find(')', n_idx)
    argname_ls = []
    args = prompt[n_idx+len(name)+1:stop_idx]
    flag = 1
    arg = ''
    for c in args:
        if c==' ':
            continue
        if c==':':
            argname_ls.append(arg)
            arg=''
            flag=0
        elif c==',':
            if flag:
                argname_ls.append(arg)
                arg=''
            else:
                flag = 1
            continue
        if flag:
            arg = arg + c
    if arg!='':
        argname_ls.append(arg)
    print(argname_ls)
    return argname_ls

final_dict_ls = []
special_task = ["HumanEval/1"]
modify_task = ['HumanEval/76', 'HumanEval/67', 'HumanEval/87', 'HumanEval/71', 'HumanEval/137', 'HumanEval/95', 'HumanEval/84', 'HumanEval/135', 'HumanEval/113', 'HumanEval/47', 'HumanEval/115', 'HumanEval/50', 'HumanEval/45', 'HumanEval/65', 'HumanEval/158', 'HumanEval/116', 'HumanEval/32', 'HumanEval/148', 'HumanEval/79']
for s in solution:
    temp_dict = {}
    s_json = json.loads(s)
    if s_json["task_id"] not in modify_task:
        continue
    temp_dict["task_id"] = s_json["task_id"]
    temp_dict["testcases"] = []
    prompts = s_json["prompt"].split('\n')
    mp = re.compile(r'(?<!def )'+s_json["entry_point"]+r' ?\(')
    argname_ls = find_function_argname(s_json["prompt"], s_json["entry_point"])
    for i in range(len(prompts)):
        m =mp.search(prompts[i])
        if m == None:
            continue
        r_idx = prompts[i].find(")", m.end())
        if s_json['task_id'] in special_task:
            r_idx = prompts[i].rfind(")")
        args = parse_args(prompts[i][m.end():r_idx])
        eq_id = max([prompts[i].find('=='), prompts[i].find('=>'), prompts[i].find('->')])
        if eq_id>0:
            result = prompts[i][eq_id+2:].strip()
        else:
            result = prompts[i+1].strip()
        t = {k:v for k,v in zip(argname_ls, args)}
        t["return_val"] = result
        temp_dict["testcases"].append(t)
    final_dict_ls.append(temp_dict)

dir_path = "testcase"
for i in range(len(final_dict_ls)):
    num = int(final_dict_ls[i]["task_id"][final_dict_ls[i]["task_id"].find("/")+1:])
    with open(os.path.join(dir_path, f'{num}.txt'),'w',encoding='utf-8') as f:
        for t in final_dict_ls[i]["testcases"]:
            for k,v in t.items():
                f.write(k+'='+v+'\n')
            f.write('-------------------\n')
#generate_jsonl(final_dict_ls, "humaneval_testcases_in_prompt_args_result.jsonl")
# with open("humaneval_testcases_in_prompt_args_result.jsonl", 'r', encoding='utf-8') as f:
#     c = f.readline()
#     c_json = json.loads(c)
#     print(c_json)






















# with open("D:\\assertion\\bytedance\\idx_corr.json") as f:
#     idx_corr = json.load(f)
#
# method_name=[]
#
# for s in solution:
#     s_json = json.loads(s)
#     m_name = s_json["entry_point"]
#     method_name.append(m_name)
#
# for file in os.listdir("D:\\assertion\\bytedance\\CodeT-main\\CodeT\\data\\generated_data"):
#     if file.startswith("HumanEval") and file.endswith("test_case.jsonl"):
#         with open(os.path.join("D:\\assertion\\bytedance\\CodeT-main\\CodeT\\data\\generated_data",file),'r',encoding="utf-8") as f:
#             content = f.read().rstrip("\n").split("\n")
#         for mi, m_name in enumerate(method_name):
#             c = content[idx_corr[str(mi)]]
#             c_json = json.loads(c)
#             mp = re.compile(m_name + r" ?\(")
#             def_idx = c_json["prompt"].rfind("def ")
#             if mp.match(c_json["prompt"][def_idx+4:]) == None:
#                 print(file, m_name)
#         print("----------")

