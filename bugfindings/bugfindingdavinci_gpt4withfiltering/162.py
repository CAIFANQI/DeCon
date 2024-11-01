
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5('text').hexdigest() if text else None
assert string_to_md5("") == None
assert string_to_md5("Hello World!") == "ed076287532e86365e841e92bfc50d8c"
assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"
assert string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
assert string_to_md5("message digest") == "f96b697d7cb7938d525a2f31aaf161d0"
assert string_to_md5("abcdefghijklmnopqrstuvwxyz") == "c3fcd3d76192e4007dfb496cca67e13b"
assert string_to_md5("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") == "d174ab98d277d9f5a5611c2c9f419d9f"
assert string_to_md5(" ") == "7215ee9c7d9dc229d2921a40e899ec5f"
assert string_to_md5("ab") == "187ef4436122d1cc2f40dc2b92f0eba0"
assert string_to_md5("abcd") == "e2fc714c4727ee9395f324cd2e7f331f"
assert string_to_md5("abcde") == "ab56b4d92b40713acc5af89985d4b786"
assert string_to_md5('A') == '7fc56270e7a70fa81a5935b72eacbe29'
assert string_to_md5('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') == 'd174ab98d277d9f5a5611c2c9f419d9f'
assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"
assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
assert string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
assert string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'
assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'
assert string_to_md5('message digest') == 'f96b697d7cb7938d525a2f31aaf161d0'
assert string_to_md5('abcdefghijklmnopqrstuvwxyz') == 'c3fcd3d76192e4007dfb496cca67e13b'
assert string_to_md5('123') == '202cb962ac59075b964b07152d234b70'
assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"
assert string_to_md5("hello world") == "5eb63bbbe01eeed093cb22bb8f5acdc3"
assert string_to_md5("world") == "7d793037a0760186574b0282f2f435e7"
assert string_to_md5("admin") == "21232f297a57a5a743894a0e4a801fc3"
assert string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
assert string_to_md5('Hello') == '8b1a9953c4611296a827abf8c47804d7'
assert string_to_md5('Hello, World!') == '65a8e27d8879283831b664bd8b7f0ad4'
assert string_to_md5(' ') == '7215ee9c7d9dc229d2921a40e899ec5f'
assert string_to_md5("123") == "202cb962ac59075b964b07152d234b70"
assert string_to_md5('ab') == '187ef4436122d1cc2f40dc2b92f0eba0'
assert string_to_md5('abcd') == 'e2fc714c4727ee9395f324cd2e7f331f'
assert string_to_md5('abcde') == 'ab56b4d92b40713acc5af89985d4b786'
assert string_to_md5('abcdef') == 'e80b5017098950fc58aad83c8c14978e'
assert string_to_md5("abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq") == "8215ef0796a20bcaaae116d3876c664a"
assert string_to_md5(" ") == "7215ee9c7d9dc229d2921a40e899ec5f", "Test 3 Failed"
assert string_to_md5("0123456789") == "781e5e245d69b566979b86e28d23f2c7"
assert string_to_md5("The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"
assert string_to_md5('\n') == '68b329da9893e34099c7d8ad5cb9c940'
assert string_to_md5("12345678901234567890123456789012345678901234567890123456789012345678901234567890") == "57edf4a22be3c955ac49da2e2107b67a"
assert None == string_to_md5('')
assert string_to_md5("abcdef") == "e80b5017098950fc58aad83c8c14978e"
assert string_to_md5("abcdefg") == "7ac66c0f148de9519b8bd264312c4d64"
assert string_to_md5("abcdefgh") == "e8dc4081b13434b45189a720b77b6818"
assert string_to_md5("1") == "c4ca4238a0b923820dcc509a6f75849b"
assert (string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661")
assert (string_to_md5("ab") == "187ef4436122d1cc2f40dc2b92f0eba0")
assert (string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72")
assert (string_to_md5("abcd") == "e2fc714c4727ee9395f324cd2e7f331f")
assert (string_to_md5("abcde") == "ab56b4d92b40713acc5af89985d4b786")
assert (string_to_md5("abcdef") == "e80b5017098950fc58aad83c8c14978e")
assert (string_to_md5("abcdefg") == "7ac66c0f148de9519b8bd264312c4d64")
assert (string_to_md5("abcdefgh") == "e8dc4081b13434b45189a720b77b6818")
assert string_to_md5("0") == "cfcd208495d565ef66e7dff9f98764da"
assert string_to_md5("asdf") == "912ec803b2ce49e4a541068d495ab570"
assert string_to_md5('x') == '9dd4e461268c8034f5c8564e155c67a6'
assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f'
