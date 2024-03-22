
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'
assert 	file_name_check("abc.txt") == "Yes"
assert 	file_name_check("abc.exe.exe") == "No"
assert 	file_name_check("abc.exe.dll") == "No"
assert 	file_name_check("abc.exe.txt") == "No"
assert 	file_name_check("abc.dll.exe") == "No"
assert 	file_name_check("abc.dll.dll") == "No"
assert 	file_name_check("abc.dll.txt") == "No"
assert 	file_name_check("abc.txt.exe.exe") == "No"
assert 	file_name_check('file1.exe.exe.exe') == 'No', 'ERROR'
assert 	file_name_check('file1.exe.exe.dll') == 'No', 'ERROR'
assert 	file_name_check('file1.exe.dll.exe') == 'No', 'ERROR'
assert 	file_name_check('file1.exe.dll.dll') == 'No', 'ERROR'
assert 	file_name_check('file1.dll.exe') == 'No', 'ERROR'
assert 	file_name_check('file1.dll.dll') == 'No', 'ERROR'
assert 	file_name_check("..txt") == 'No'
assert 	file_name_check("name.txt") == 'Yes'
assert 	file_name_check("name.exe") == 'Yes'
assert 	file_name_check("name.dll") == 'Yes'
assert 	file_name_check("name.txt.") == 'No'
assert 	file_name_check("a..txt") == 'No'
assert 	file_name_check("name.txt.exe") == 'No'
assert 	file_name_check("name.txt.dll") == 'No'
assert 	file_name_check("name.exe.exe") == 'No'
assert 	file_name_check("file.txt.") == "No", "There should be no more than three digits."
assert 	file_name_check(".file.txt") == "No", "There should be no more than three digits."
assert 	file_name_check(".file.txt.exe") == "No", "There should be no more than three digits."
assert 	file_name_check("file.txt.exe.dll") == "No", "There should be one dot."
assert 	file_name_check("file.exe.dll") == "No", "There should be one dot."
assert 	file_name_check("file.exe.dll.txt") == "No", "There should be one dot."
assert 	file_name_check("file.exe.dll.txt.") == "No", "There should be one dot."
assert 	file_name_check("a.txt.") == 'No', "Wrong output for 'a.txt.'"
assert 	file_name_check(".a.txt") == 'No', "Wrong output for '.a.txt'"
assert 	file_name_check("a..txt") == 'No', "Wrong output for 'a..txt'"
assert 	file_name_check("a.txt.exe") == 'No', "Wrong output for 'a.txt.exe'"
assert 	file_name_check("a.txt.exe.") == 'No', "Wrong output for 'a.txt.exe.'"
assert 	file_name_check(".a.txt.exe") == 'No', "Wrong output for '.a.txt.exe'"
assert 	file_name_check('vali') == 'No'
assert 	file_name_check('invalid.') == 'No'
assert 	file_name_check('invalid.exe.txt') == 'No'
assert 	file_name_check('invalid.txt.exe') == 'No'
assert 	file_name_check('valid.exe.exe') == 'No'
assert 	file_name_check('valid.exe.') == 'No'
assert 	file_name_check('valid.exe.exe.') == 'No'
assert 	file_name_check('valid.') == 'No'
assert 	file_name_check('valid..txt') == 'No'
assert 	file_name_check('abc.exe') == 'Yes'
assert 	file_name_check('abc.dll') == 'Yes'
assert 	file_name_check('0a.txt') == 'No'
assert 	file_name_check('a.exe.dll') == 'No'
assert 	file_name_check('a.txt.') == 'No'
assert 	file_name_check('a.') == 'No'
assert 	file_name_check('a..') == 'No'
assert 	file_name_check('0name.txt') == 'No', 'file_name_check returns wrong value'
assert 	file_name_check('name.docx') == 'No', 'file_name_check returns wrong value'
assert 	file_name_check('name.pdf') == 'No', 'file_name_check returns wrong value'
assert 	file_name_check('name.py') == 'No', 'file_name_check returns wrong value'
assert 	file_name_check('name.c') == 'No', 'file_name_check returns wrong value'
assert 	file_name_check('name.csv') == 'No', 'file_name_check returns wrong value'
assert file_name_check('123.dll') == 'No'
assert file_name_check('a.txt') == 'Yes'
assert file_name_check('abc.txt') == 'Yes'
assert file_name_check('abc.exe') == 'Yes'
assert file_name_check('abc.xls') == 'No'
assert file_name_check('abc.xlsx') == 'No'
assert file_name_check('abc.abc') == 'No'
assert file_name_check('abc.txt.exe') == 'No'
assert file_name_check('abc.exe.dll') == 'No'
assert 	file_name_check('dummy.exe') == "Yes", "Wrong answer"
assert 	file_name_check('dummy.dll') == "Yes", "Wrong answer"
assert 	file_name_check('dummy.pdf') == "No", "Wrong answer"
assert 	file_name_check('dummy.py') == "No", "Wrong answer"
assert 	file_name_check('dummy.py.exe') == "No", "Wrong answer"
assert 	file_name_check('dummy.py.txt') == "No", "Wrong answer"
assert 	file_name_check('0name.txt') == 'No' 
assert 	file_name_check('1name.exe') == 'No' 
assert 	file_name_check('2name.dll') == 'No' 
assert 	file_name_check('3name.png') == 'No' 
assert 	file_name_check('4name.doc') == 'No' 
assert 	file_name_check('name.exe.') == 'No' 
assert 	file_name_check('name.txt') == 'Yes' 
assert 	file_name_check('name.doc') == 'No' 
assert 	file_name_check('name.txt.doc') == 'No' 
assert 	file_name_check('name.doc.txt') == 'No' 
assert 	file_name_check('01.txt') == 'No'
assert 	file_name_check('a.bat') == 'No'
assert 	file_name_check('a.txt.exe') == 'No'
assert 	file_name_check('a.exe.exe') == 'No'
assert 	file_name_check('a.txt.exe.exe') == 'No'
assert 	file_name_check('a.exe.txt.exe') == 'No'
assert 	file_name_check('a.exe.txt') == 'No'
assert 	file_name_check('a.exe.dll.exe') == 'No'
assert 	file_name_check('a.exe') == 'Yes'
assert 	file_name_check('a.dll') == 'Yes'
assert 	file_name_check('a.exe.dll.txt') == 'No'
assert 	file_name_check('abc.exe.txt') == 'No'
assert 	file_name_check('a.exe.txt.exe.txt') == 'No'
assert 	file_name_check('a.b.exe') == 'No'
assert 	file_name_check('abc.txt') == 'Yes'
assert 	file_name_check('1.txt') == 'No'
assert 	file_name_check('1234567890.txt') == 'No'
assert 	file_name_check('valid.txt') == 'Yes'
assert 	file_name_check('a.txt') == 'Yes'
assert 	file_name_check('123.txt') == 'No'
assert 	file_name_check('hello') == 'No'
assert 	file_name_check('hello.txt') == 'Yes'
assert 	file_name_check('hello.doc') == 'No'
assert 	file_name_check('hello.docx') == 'No'
assert 	file_name_check('hello.dox') == 'No'
assert 	file_name_check('hello.pdf') == 'No'
