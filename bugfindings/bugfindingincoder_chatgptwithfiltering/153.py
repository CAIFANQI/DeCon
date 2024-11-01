
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + strong
    return ans

assert Strongest_Extension('Slices', ['StuFfed']) == 'Slices.StuFfed', 'Wrong answer'
assert Strongest_Extension('Slices', ['SErviNGSliCes']) == 'Slices.SErviNGSliCes', 'Wrong answer'
assert Strongest_Extension('Pizza', ['ABC', 'bcd']) == 'Pizza.ABC'
assert Strongest_Extension('Pizza', ['AB']) == 'Pizza.AB'
assert Strongest_Extension('Strings', ['SErviNGSliCes']) == 'Strings.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['Cheese']) == 'Slices.Cheese'
assert Strongest_Extension('Slices', ['StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['SliCes', 'cheese','stuFEd']) == 'Slices.SliCes'
assert Strongest_Extension('Slices', ['SliCes', 'cheEse','stuFed']) == 'Slices.SliCes'
assert Strongest_Extension('Slices', ['SliCes', 'CHeese','stuFed']) == 'Slices.SliCes'
assert Strongest_Extension('Slices', ['SLiCes', 'cheese','stuFed']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['SLiCes', 'cheese','stuFEd']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['SLiCes', 'cheEse','stuFed']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['SLiCes', 'CHeese','stuFed']) == 'Slices.SLiCes'
assert Strongest_Extension("Slice", ["Slice"]) == "Slice.Slice"
assert Strongest_Extension('strongest_extension', ['ASDF']) =='strongest_extension.ASDF'
assert Strongest_Extension('strongest_extension', ['AbCd']) =='strongest_extension.AbCd'
assert Strongest_Extension('strongest_extension', ['abCd']) =='strongest_extension.abCd'
assert Strongest_Extension("Slice", ["SErviNGSliCes"]) == "Slice.SErviNGSliCes"
assert Strongest_Extension("Foo", ["Bar"]) == "Foo.Bar"
assert Strongest_Extension('Slice', ['SErviNGSliCes']) == 'Slice.SErviNGSliCes'
assert Strongest_Extension("Slices", ["StuFfed"]) == "Slices.StuFfed"
assert Strongest_Extension('Slice', ['Slices']) == 'Slice.Slices'
assert Strongest_Extension('Slices', ['StuFed']) == 'Slices.StuFed'
assert Strongest_Extension('Slice', ['StuFfed']) == 'Slice.StuFfed'
assert Strongest_Extension('Slices', ['Apple']) == 'Slices.Apple'
assert Strongest_Extension('Slices', ['Orange']) == 'Slices.Orange'
assert Strongest_Extension("Candy", ["Juice", "Sugar"]) == 'Candy.Juice'
assert Strongest_Extension('Test', ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'RST']) == 'Test.ABC'
