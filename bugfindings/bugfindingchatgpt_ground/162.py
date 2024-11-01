
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5('text').hexdigest() if text else None
assert string_to_md5('') == None
assert string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
assert string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3'
assert string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b'
assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f'
assert string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'
assert string_to_md5('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') == 'd174ab98d277d9f5a5611c2c9f419d9f'
assert string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
assert string_to_md5('world') == '7d793037a0760186574b0282f2f435e7'
assert string_to_md5('123456') == 'e10adc3949ba59abbe56e057f20f883e'
assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
assert string_to_md5("world") == "7d793037a0760186574b0282f2f435e7"
assert string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592', "Test case 2 failed"
assert string_to_md5('world') == '7d793037a0760186574b0282f2f435e7', "Test case 3 failed"
assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f', "Test case 4 failed"
assert string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b', "Test case 5 failed"
assert string_to_md5("") == None
assert string_to_md5('md5') == '1bc29b36f623ba82aaf6724fd3b16718'
assert string_to_md5("Hello") == "8b1a9953c4611296a827abf8c47804d7"
assert string_to_md5("1234567890") == "e807f1fcf82d132f9bb018ca6738a19f"
assert string_to_md5("abcdefghijklmnopqrstuvwxyz") == "c3fcd3d76192e4007dfb496cca67e13b"
assert string_to_md5("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "437bba8e0bf58337674f4539e75186ac"
assert string_to_md5('password') == '5f4dcc3b5aa765d61d8327deb882cf99'
assert string_to_md5('12345') == '827ccb0eea8a706c4c34a16891f84e7b', "Test case 4 failed"
assert string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"
assert string_to_md5("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") == "d174ab98d277d9f5a5611c2c9f419d9f"
assert string_to_md5("The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"
assert string_to_md5("abc123") == "e99a18c428cb38d5f260853678922e03"
assert string_to_md5("password") == "5f4dcc3b5aa765d61d8327deb882cf99"
assert string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
assert string_to_md5("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
assert string_to_md5('abc123') == 'e99a18c428cb38d5f260853678922e03'
assert string_to_md5('password123') == '482c811da5d5b4bc6d497ffa98491e38'
assert string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5'
assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592", "Test case 2 failed"
assert string_to_md5("abc123") == "e99a18c428cb38d5f260853678922e03", "Test case 3 failed"
assert string_to_md5("password") == "5f4dcc3b5aa765d61d8327deb882cf99", "Test case 4 failed"
assert string_to_md5('Hello World') == 'b10a8db164e0754105b7a99be72e3fe5', "Error: Test Case 2"
assert string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b', "Error: Test Case 3"
assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f', "Error: Test Case 4"
assert string_to_md5('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == '437bba8e0bf58337674f4539e75186ac'
assert string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72', "Test case 2 failed"
assert string_to_md5('hello world') == '5eb63bbbe01eeed093cb22bb8f5acdc3', "Test case 3 failed"
assert string_to_md5('Hello World!') == 'ed076287532e86365e841e92bfc50d8c'
