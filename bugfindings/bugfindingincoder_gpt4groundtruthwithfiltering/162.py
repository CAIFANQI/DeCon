
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5('text').hexdigest() if text else None
assert string_to_md5('') == None
assert string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"
assert string_to_md5("") is None
assert string_to_md5('abc') == '900150983cd24fb0d6963f7d28e17f72'
assert string_to_md5('hello') == '5d41402abc4b2a76b9719d911017c592'
assert string_to_md5('') is None
assert string_to_md5("")        is None
assert string_to_md5("") == None
assert string_to_md5("")         is None
assert string_to_md5('') == (None)
