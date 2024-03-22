import json
import re
import os
import sys

solution_file ="/home/huangjiaming/bytedance/human-eval-v2-20210705.jsonl"
model=sys.argv[1]
testcase_file =f"/home/huangjiaming/bytedance/human-eval-{model}_testcases_latest.jsonl"
with open(solution_file, 'r', encoding="utf-8") as f_json_file:
    solution=f_json_file.read().rstrip("\n").split("\n")
with open(testcase_file, 'r', encoding='utf-8') as f:
    tmp = f.read().rstrip('\n').split('\n')
    final_dict_ls = [json.loads(i) for i in tmp]

brackets_map = {')': '(', ']': '[', '}': '{'}

def parse_args(s):
    arg_list = []
    brackets_stack = []
    in_string=0
    last_quote = None
    arg = ''
    for c in s:
        if c==' ' and brackets_stack==[] and in_string==0:
            continue
        elif c==',':
            if brackets_stack==[] and in_string==0:
                arg_list.append(arg)
                arg=''
                continue
        elif c=='(' or c=='[' or c=='{':
            if not in_string:
                brackets_stack.append(c)
        elif c==')' or c==']' or c=='}':
            if in_string==0 and (brackets_stack==[] or brackets_stack[-1]!=brackets_map[c]):
                return "wrong type args"
            if not in_string:
                brackets_stack.pop()
        elif c=='\'' or c=='\"':
            if in_string and c==last_quote:
                in_string=0
                last_quote=None
            elif not in_string:
                in_string=1
                last_quote=c
        arg = arg + c
    if arg!='':
        arg_list.append(arg)
    return arg_list

def generate_jsonl(dict_list, f_name):
    with open(f_name, 'w', encoding='utf-8') as f:
        for i in dict_list:
            f.write(json.dumps(i)+'\n')

def paren_match(s):
    in_string=0
    last_quote=None
    ret = ''
    b_s = []
    for c in s:
        if c=='\'' or c=='\"':
            if in_string and c==last_quote:
                in_string=0
                last_quote=None
            elif not in_string:
                in_string=1
                last_quote=c
        elif c=='(' or c=='[' or c=='{':
            if not in_string:
                b_s.append(c)
        elif c==')' or c==']' or c=='}':
            if in_string==0 and (b_s==[] or b_s[-1]!=brackets_map[c]):
                break
            if not in_string:
                b_s.pop()
        ret = ret + c
    while b_s:
        ret = ret.replace(b_s[-1], '', 1)
        b_s.pop()
    return ret

def extract_paren_result(s):
    in_string=0
    last_quote=None
    ret = ''
    b_s = []
    for c in s:
        if c=='\'' or c=='\"':
            if in_string and c==last_quote:
                in_string=0
                last_quote=None
            elif not in_string:
                in_string=1
                last_quote=c
        elif c=='(' or c=='[' or c=='{':
            if not in_string:
                b_s.append(c)
        elif c==')' or c==']' or c=='}':
            if in_string==0 and (b_s==[] or b_s[-1]!=brackets_map[c]):
                break
            if not in_string:
                b_s.pop()
                if b_s == []:
                    ret = ret + c
                    break
        ret = ret + c
    while b_s:
        ret = ret.replace(b_s[-1], '', 1)
        b_s.pop()
    return ret

def find_function_argname(prompt, name):
    n_idx = prompt.find("def "+name)
    stop_idx = prompt.find(')', n_idx)
    argname_ls = []
    args = prompt[n_idx+len("def "+name)+1:stop_idx]
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
    return argname_ls

w_dict_ls = []
ap = re.compile("assert not")
not_eq_set = {'!=', '<', '>', '<=', '>='}
#special_task = ["HumanEval/1", "HumanEval/6", "HumanEval/38","HumanEval/50", "HumanEval/119","HumanEval/121", "HumanEval/127"]
for si, s in enumerate(solution):
    s_json = json.loads(s)
    assertions = final_dict_ls[si]["assertions"]
    #print(type(assertions[0]))
    tmp_dict = final_dict_ls[si]
    tmp_dict["assertions"] = []
    mp = re.compile(s_json["entry_point"]+r' ?\(')
    ignore_case_pattern = re.compile(r'(len\(|isinstance\(|type\()')
    argname_ls = find_function_argname(s_json["prompt"], s_json["entry_point"])
    assert_set = set()
    #print(argname_ls)
    for ai, a in enumerate(assertions):
        if not isinstance(a["isT"], bool):
            continue
        aa = a["assert"]
        if aa in assert_set:
            continue
        assert_set.add(aa)
        if len(mp.findall(aa)) > 1:
            continue
        m =mp.search(aa)
        if m == None:
            continue
        if ignore_case_pattern.search(aa):
            continue
        before_m = aa[:m.start()].strip()
        #if (before_m[-1] in not_eq_set) or (before_m[-2:] in not_eq_set):
        #    continue
        out=""
        eq_id = aa.find("==")
        l = 2
        r_idx = aa.rfind(")", m.end())
        args_string = paren_match(aa[m.end():r_idx])
        r_idx = m.end() + len(args_string)
        aa_ridx = aa[r_idx:]
        last_m = aa_ridx[1:].strip()
        flag = False
        for neq_mask in not_eq_set:
            if before_m.find(neq_mask) >= 0 and ((before_m[-1]==neq_mask) or (before_m[-2:]==neq_mask)):
                flag=True
                break
            if last_m.find(neq_mask) >= 0 and ((last_m[0] == neq_mask) or (last_m[:2] == neq_mask)):
                flag=True
                break
        if flag:
            continue
        args = parse_args(args_string)
        comment_id = aa_ridx.find('#')
        if comment_id>0:
            comment_id += r_idx
        if eq_id<0:
            eq_id = aa.find(' is ', r_idx)
            l = 4
            if comment_id>0 and eq_id>comment_id:
                eq_id=-1
        result=None
        if eq_id>0:
            if eq_id>m.end():
                tmp = aa[eq_id+l:].strip()
                if tmp[0] in brackets_map.values():
                    result = extract_paren_result(tmp)
                else:
                    end_id = len(aa)
                    err_id = re.search(r", *f?(\".*\"|\'.*\')$", aa_ridx)
                    if err_id != None:
                        end_id = err_id.start() + r_idx
                    result = aa[eq_id+l:end_id].strip()
                    result = paren_match(result)
            else:
                result = aa[re.match(r"assert (not)?",aa).end():eq_id].strip()
                result = paren_match(result)
        #else:
        #    result = str(a["isT"])
        #if result=="True" or result=="False":
        #    if ap.match(aa)!=None:
        if result==None:
            result = "True" if ap.match(aa)==None else "False"
        if len(argname_ls) == len(args):
            for k,v in zip(argname_ls, args):
                if v.startswith(f'{k}='):
                    v=v[v.find('=')+1:]
                out = out + k + '=' + v+ '\n'
        elif len(argname_ls)==1 and len(args)>1:
            out = argname_ls[0] + '=' + ','.join(args) + '\n'
        out = out + "return_val" + '=' + result
        print(aa)
        print(f'isT={a["isT"]}')
        print(out)
        print("-----------")
        tmp_dict["assertions"].append({"assert":a["assert"], "isT":a["isT"], "args_and_result": out})
    w_dict_ls.append(tmp_dict)

#dir_path = "testcase"
#for i in range(len(final_dict_ls)):
#    with open(os.path.join(dir_path, f'{i}.txt'),'w',encoding='utf-8') as f:
#        for t in final_dict_ls[i]["testcases"]:
#            for k,v in t.items():
#                f.write(k+'='+v+'\n')
#            f.write('-------------------\n')
generate_jsonl(w_dict_ls, f"humaneval_{model}_testcases_unique_in_assert_args_result_new.jsonl")
#with open("humaneval_testcases_in_prompt_args_result.jsonl", 'r', encoding='utf-8') as f:
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

