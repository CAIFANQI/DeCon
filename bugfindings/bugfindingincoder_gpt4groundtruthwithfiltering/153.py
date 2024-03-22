
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

assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice', 'Slice']) == 'Slice.Slice'
assert Strongest_Extension('Slices', ['StuFfed']) == 'Slices.StuFfed', 'Wrong answer'
assert Strongest_Extension('Slices', ['SErviNGSliCes']) == 'Slices.SErviNGSliCes', 'Wrong answer'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese']) == 'Slices.SErviNGSliCes', 'Wrong answer'
assert Strongest_Extension('Slices', ['StuFfed', 'Cheese']) == 'Slices.StuFfed', 'Wrong answer'
assert Strongest_Extension('Slices', ['StuFfed', 'Cheese', 'StuFfed']) == 'Slices.StuFfed', 'Wrong answer'
assert Strongest_Extension('Pizza', ['ABC', 'bcd']) == 'Pizza.ABC'
assert Strongest_Extension('Pizza', ['AB']) == 'Pizza.AB'
assert Strongest_Extension('Slices', ['SErviNGSliCes','stufFed', 'Cheese']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes','stufFed', 'cheese']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'StuFfed']) == "Slices.SErviNGSliCes"
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese']) == "Slices.SErviNGSliCes"
assert Strongest_Extension('Objects', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Objects.SErviNGSliCes'
assert Strongest_Extension('Slice', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slice.SErviNGSliCes'
assert Strongest_Extension('Object', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Object.SErviNGSliCes'
assert Strongest_Extension("Slices", ['StuFfed', 'Cheese', 'StuFfed']) == "Slices.StuFfed"
assert Strongest_Extension("Slices", ['Cheese', 'StuFfed', 'StuFfed']) == "Slices.StuFfed"
assert Strongest_Extension("Slices", ['StuFfed', 'StuFfed', 'StuFfed']) == "Slices.StuFfed"
assert Strongest_Extension('Snake', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Snake.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('ScaC', ['SErviNGSliCes', 'StuFfed', 'Cheese']) == 'ScaC.SErviNGSliCes'
assert Strongest_Extension('ScAc', ['SErviNGSliCes', 'StuFfed', 'Cheese']) == 'ScAc.SErviNGSliCes'
assert Strongest_Extension('Slice', ['SErviNGSliCes', 'StuFfed', 'Cheese']) == 'Slice.SErviNGSliCes'
assert Strongest_Extension('Strings', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Strings.SErviNGSliCes'
assert Strongest_Extension('Strings', ['SErviNGSliCes']) == 'Strings.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['Cheese']) == 'Slices.Cheese'
assert Strongest_Extension('Slices', ['StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['StuFfed', 'Cheese']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['CErviNGSliCes', 'StUFfed', 'Geese']) == 'Slices.CErviNGSliCes'
assert Strongest_Extension('Slices', ['CeRviNGSliCes', 'StuFfed', 'Geese']) == 'Slices.CeRviNGSliCes'
assert Strongest_Extension('Slices', ['StuFfed', 'Cheese', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension("Slices", ['StupFeD', 'Cheese', 'StupFeD']) == "Slices.StupFeD", "Wrong answer"
assert Strongest_Extension("Slices", ['StupFeD', 'Cheese', 'StuFfed']) == "Slices.StupFeD", "Wrong answer"
assert Strongest_Extension("Slices", ['StuFfed', 'StuFfed', 'Cheese']) == "Slices.StuFfed", "Wrong answer"
assert Strongest_Extension('Slices', ['SliCes', 'cheese','stuFEd']) == 'Slices.SliCes'
assert Strongest_Extension('Slices', ['SliCes', 'cheEse','stuFed']) == 'Slices.SliCes'
assert Strongest_Extension('Slices', ['SliCes', 'CHeese','stuFed']) == 'Slices.SliCes'
assert Strongest_Extension('Slices', ['SLiCes', 'cheese','stuFed']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['SLiCes', 'cheese','stuFEd']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['SLiCes', 'cheEse','stuFed']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['SLiCes', 'CHeese','stuFed']) == 'Slices.SLiCes'
assert Strongest_Extension('Slices', ['StuFfed', 'StuFfed', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['StuFfed', 'StuFfed', 'StuFfed', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension("Slices", ["Slice", "Slices"]) == "Slices.Slice"
assert Strongest_Extension("Slice", ["Slice"]) == "Slice.Slice"
assert Strongest_Extension('Slipper', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slipper.SErviNGSliCes'
assert Strongest_Extension('Slipper', ['SErviNGSliCes', 'StuFfed', 'Cheese']) == 'Slipper.SErviNGSliCes'
assert Strongest_Extension('Slider', ['SErviNGSliCes', 'StuFfed', 'Cheese']) == 'Slider.SErviNGSliCes'
assert Strongest_Extension('Slipper', ['StuFfed', 'Cheese', 'SErviNGSliCes']) == 'Slipper.SErviNGSliCes'
assert Strongest_Extension('Slider', ['StuFfed', 'Cheese', 'SErviNGSliCes']) == 'Slider.SErviNGSliCes'
assert Strongest_Extension('strongest_extension', ['ASDF']) =='strongest_extension.ASDF'
assert Strongest_Extension('strongest_extension', ['AbCd']) =='strongest_extension.AbCd'
assert Strongest_Extension('strongest_extension', ['AbCd', 'ASDF', 'asdf']) =='strongest_extension.ASDF'
assert Strongest_Extension('strongest_extension', ['abCd']) =='strongest_extension.abCd'
assert Strongest_Extension('strongest_extension', ['abCd', 'ASDF', 'asdf']) =='strongest_extension.ASDF'
assert Strongest_Extension("Pizza", ["SErviNGSliCes", "Ham", "Cheese", "StuFfed", "sErviNGSliCes", "Ham", "Cheese", "StuFfed"]) == "Pizza.SErviNGSliCes"
assert Strongest_Extension("Slice", ["SErviNGSliCes"]) == "Slice.SErviNGSliCes"
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'StuFfed', 'Cheese']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['StuFfed', 'Cheese', 'SErviNGSliCes']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['StuFfed', 'Cheese', 'SErviNGSliCes']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['StuFfed', 'Cheese', 'StuFfed']) == 'Slices.StuFfed'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Mouth', 'Nothing']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Foo", ["Bar"]) == "Foo.Bar"
assert Strongest_Extension("Slice", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slice.SErviNGSliCes"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed", "Pizza"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed", "Pizza", "Burger"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed", "Pizza", "Burger", "Donuts"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed", "Pizza", "Burger", "Donuts", "Apples"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Vanilla']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slice', ['SErviNGSliCes']) == 'Slice.SErviNGSliCes'
assert Strongest_Extension("Slices", ["StuFfed"]) == "Slices.StuFfed"
assert Strongest_Extension("Slices", ["StuFfed", "Cheese"]) == "Slices.StuFfed"
assert Strongest_Extension('Slice', ['Slice', 'Slices']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slice', 'Slices', 'Slices']) == 'Slice.Slice'
assert Strongest_Extension('Slice', ['Slices']) == 'Slice.Slices'
assert Strongest_Extension('Slice', ['Slices', 'Slices', 'Slices']) == 'Slice.Slices'
assert Strongest_Extension('Slice', ['Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices']) == 'Slice.Slices'
assert Strongest_Extension("String", ["Ab", "xyz"]) == "String.Ab"
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Stuffed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['StuFed', 'StuFed', 'StuFed']) == 'Slices.StuFed'
assert Strongest_Extension('Slices', ['StuFed', 'StuFed', 'StuFed', 'StuFed']) == 'Slices.StuFed'
assert Strongest_Extension('Slices', ['StuFed']) == 'Slices.StuFed'
assert Strongest_Extension('Slice', ['StuFfed']) == 'Slice.StuFfed'
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Zoo']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension('Slices', ['Apple']) == 'Slices.Apple'
assert Strongest_Extension('Slices', ['Orange']) == 'Slices.Orange'
assert Strongest_Extension('Class', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Class.SErviNGSliCes'
assert Strongest_Extension('Class', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'PieSlecEs', 'Coat']) == 'Class.SErviNGSliCes'
assert Strongest_Extension("Lions", ["Lions", "Cheese", "Camel"]) == "Lions.Lions"
assert Strongest_Extension("Elephants", ["StuFfed", "Elephants"]) == "Elephants.StuFfed"
assert Strongest_Extension("Bears", ["StuFfed", "Camel", "Bears"]) == "Bears.StuFfed"
assert Strongest_Extension("Cats", ["StuFfed", "Camel", "Bears"]) == "Cats.StuFfed"
assert Strongest_Extension("Candy", ["Juice", "Sugar"]) == 'Candy.Juice'
assert Strongest_Extension('Test', ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'RST']) == 'Test.ABC'
assert Strongest_Extension("Pie", ["Pie", "Cese", "Stuff"]) == "Pie.Pie"
assert Strongest_Extension("Hens", ["Slices", "Pie", "Stuff"]) == "Hens.Pie"
assert Strongest_Extension('Slice', ['Slice','slices', 'SErviNGSliCes','slices']) == 'Slice.SErviNGSliCes'
assert Strongest_Extension('Slice', ['Slice','slices','slice','slices']) == 'Slice.Slice'
assert Strongest_Extension('CamelCase', ['A', 'CamelCase', 'd']) == 'CamelCase.A'
assert Strongest_Extension("Cars", ['BMW', 'Toyota', 'Subaru']) == "Cars.BMW"
assert Strongest_Extension("Squares", ['Cube', 'Rectangle', 'Lipid']) == "Squares.Cube"
assert Strongest_Extension("Peanuts", ['Lollipop', 'Apple']) == "Peanuts.Apple"
