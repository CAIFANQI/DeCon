
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

assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Pizza", ['Italian', 'Huge', 'Extremely']) == 'Pizza.Huge'
assert Strongest_Extension("Ingredients", ['Tomato', 'Cheese', 'Pepperoni']) == 'Ingredients.Tomato'
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Muffin", ["muffin", "Muffin", "Muffin.Muffin"]) == "Muffin.Muffin"
assert Strongest_Extension("Bees", ["B", "E", "E", "S"]) == "Bees.B"
assert Strongest_Extension("Bees", ["B", "B", "B", "B"]) == "Bees.B"
assert Strongest_Extension("Cheesecake", ['StrawberryCheesecake', 'AppleCheesecake', 'Cheesecake']) == "Cheesecake.Cheesecake"
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("", ['Ultra', 'GeneralSuper']) == '.Ultra'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Cheese.ChEeSe']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ['Cheese', 'SErviNGSliCes', 'StuFfed', 'Cheese.ChEeSe']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ['Cheese', 'StuFfed', 'SErviNGSliCes', 'Cheese.ChEeSe']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ['Cheese', 'StuFfed', 'Cheese.ChEeSe', 'SErviNGSliCes']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Book",['DryErase', 'BackToSchool', 'Notebook']) == 'Book.DryErase'
assert Strongest_Extension("A",['A', 'B', 'C']) == 'A.A'
assert Strongest_Extension("Masa", ["Masa", "Sushi", "Sashimi", "Onigiri"]) == "Masa.Masa"
assert Strongest_Extension("Burger", ['Deluxe', 'CHEESEBURGER']) == 'Burger.CHEESEBURGER'
assert Strongest_Extension("Cheese", ['CHEESEBURGER', 'Regular']) == 'Cheese.CHEESEBURGER'
assert Strongest_Extension("Burger", ['Deluxe', 'CHEESEBURGER', 'Regular']) == 'Burger.CHEESEBURGER'
assert Strongest_Extension("Burger", ['Deluxe', 'CHEESEBURGER', 'Regular', 'Double']) == 'Burger.CHEESEBURGER'
assert Strongest_Extension("Burger", ['Deluxe', 'CHEESEBURGER', 'Double', 'Regular']) == 'Burger.CHEESEBURGER'
assert Strongest_Extension("Pizza", ['Cheese', 'PEPPERoni', 'StuFfed']) == 'Pizza.PEPPERoni'
assert Strongest_Extension("A", ['a', 'A', 'A1', 'a2', 'A2']) == 'A.A'
assert Strongest_Extension("AA", ['Aa', 'aA', 'AA']) == 'AA.AA'
assert Strongest_Extension("AAA", ['AaA', 'aAa', 'AAa', 'Aaa', 'AAA']) == 'AAA.AAA'
assert Strongest_Extension("R", ["R", "", "r", "Rr"]) == "R.R"
assert Strongest_Extension("Burger", ['Cheese', 'WithBacon']) == 'Burger.Cheese'
assert Strongest_Extension("K", ["KPants", "Knickers", "Ketchup", "Kool-Aid"]) == "K.KPants"
assert Strongest_Extension("A", ["a", "Aa", "Aaa", "aAa"]) == "A.Aa"
assert Strongest_Extension("Vegan", ['CheEse', 'seRvingCheese', 'servingCHeese']) == 'Vegan.CheEse'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Mushrooms', 'stuffed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("VegAn", ['CheEse', 'seRvingCheese', 'servingCHeese', 'Cheese', 'seRvingCheese', 'servingCHeese']) == 'VegAn.CheEse'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Mushrooms', 'stuffed', 'MushRooms']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['Cheese', 'SErviNGSliCes', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Wedge']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Stack", ["ArrayLinkedList", "LinkedListArray"]) == "Stack.ArrayLinkedList"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed", "LinkedList"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed", "LinkedList", "Array"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Cakes", ["CAke", "CHeeSe", "cake", "cheesE"]) == 'Cakes.CAke'
assert Strongest_Extension("Pizza", ["Nutella", "pIzza", "PIZZA", "cHeese"]) == 'Pizza.PIZZA'
assert Strongest_Extension("Warrior",['Dwarf', 'Giant', 'Caveman']) == "Warrior.Dwarf"
assert Strongest_Extension("Warrior",['Dwarf', 'Caveman', 'Giant']) == "Warrior.Dwarf"
assert Strongest_Extension("Bagels", ['PoP']) == 'Bagels.PoP'
assert Strongest_Extension("Bagels", ['Pop']) == 'Bagels.Pop'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'StuFfed', 'SErviNGSliCes']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Bagels", ['PoP', 'PoP', 'Pop']) == 'Bagels.PoP'
assert Strongest_Extension("Bagels", ['PoP', 'Pop', 'PoP']) == 'Bagels.PoP'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfedPie']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Cake", ['Candles']) == 'Cake.Candles'
assert Strongest_Extension("Cake", ['Frosting', 'CreamCheese']) == 'Cake.Frosting'
assert Strongest_Extension("Pizza", ['Pepperoni', 'Cheese', 'StuFfed', 'Salad']) == 'Pizza.StuFfed'
assert Strongest_Extension("Slices", ['Cheese', 'StuFfed', 'SliCes']) == "Slices.SliCes"
assert Strongest_Extension("Pizza", ['Pizza', 'Pizza']) == "Pizza.Pizza"
assert Strongest_Extension("Pizza", ['PizzA', 'Pizza', 'pizzA']) == 'Pizza.PizzA'
assert Strongest_Extension("BlueberryMilk", ['BlueberryMilkShake', 'BlueberryMilk']) == 'BlueberryMilk.BlueberryMilk'
assert Strongest_Extension("BlueberryMilk", ['BlueberryMilkShake', 'BlueberryMilk', 'BlueberryMilkShake']) == 'BlueberryMilk.BlueberryMilk'
assert Strongest_Extension("BlueberryMilk", ['BlueberryMilkShake', 'BlueberryMilk', 'BlueberryMilkShake', 'BlueberryMilkShake']) == 'BlueberryMilk.BlueberryMilk'
assert Strongest_Extension("BlueberryMilk", ['BlueberryMilkShake', 'BlueberryMilk', 'BlueberryMilkShake', 'BlueberryMilk']) == 'BlueberryMilk.BlueberryMilk'
assert Strongest_Extension("Bacon", ['Canadian', 'sliced', 'steak', 'round']) == "Bacon.steak"
assert Strongest_Extension("Root", ['vegetable', 'Carrot', 'Turnip', 'Radish']) == "Root.Carrot"
assert Strongest_Extension("B", ["B", "c", "aBc", "A1"]) == "B.B"
assert Strongest_Extension("aBc", ["aBc", "aBc", "ab", "abc"]) == "aBc.aBc"
assert Strongest_Extension("aBc", ["A", "B", "A"]) == "aBc.A"
assert Strongest_Extension("aBc", ["aBc", "ab", "abc"]) == "aBc.aBc"
assert Strongest_Extension("aBc", ["ab", "abc"]) == "aBc.ab"
assert Strongest_Extension("Pizza", ['Pizza']) == 'Pizza.Pizza'
assert Strongest_Extension("Italian", ['iTALiAN', 'Italian']) == 'Italian.iTALiAN'
assert Strongest_Extension("Pizza", ['Pie', 'Crust', 'Ventian', 'DELICIOUS']) == 'Pizza.DELICIOUS'
assert Strongest_Extension("Pizza", ['Pie', 'Crust', 'Ventian', 'DELICIOUS', 'goooOOOoood']) == 'Pizza.DELICIOUS'
assert Strongest_Extension("Pizza", ['Veggie', 'ITALIAN']) == 'Pizza.ITALIAN'
assert Strongest_Extension("Curry", ['SpICy', 'Hot']) == 'Curry.SpICy'
assert Strongest_Extension("Software", ['Design', 'Security', 'Development']) == "Software.Design"
assert Strongest_Extension("StuFfed", ["ThinSlices", "ThickSlices", "Cheese", "StuFfed"]) == "StuFfed.StuFfed"
assert Strongest_Extension("Legumes", ['Beans', 'LENTILS', 'Lima', 'ChickPeas']) == 'Legumes.LENTILS'
assert Strongest_Extension("Spaghetti", ['Linguine', 'PENNE', 'Rotini', 'Fusilli']) == 'Spaghetti.PENNE'
assert Strongest_Extension("Cake", ['Cream', 'Chocolate']) == 'Cake.Cream'
assert Strongest_Extension("Cake", ['Cream', 'Chocolate', 'Marzipan']) == 'Cake.Cream'
assert Strongest_Extension("Pizza", ['Sausage', 'Pepperoni', 'Anchovies']) == 'Pizza.Sausage'
assert Strongest_Extension("Cake", ['Cream', 'Chocolate', 'Marzipan', 'Pistachio']) == 'Cake.Cream'
assert Strongest_Extension("Kebab",['Kebab', 'Pizza', 'mila.n', 'mila.N']) == "Kebab.Kebab"
assert Strongest_Extension("Pizza",['Pizza', 'Kebab', 'mila.n', 'mila.N']) == "Pizza.Pizza"
assert Strongest_Extension("Pizza",['Pizza', 'Kebab', 'mila.n', 'Cheese', 'mila.N']) == "Pizza.Pizza"
assert "Slices.SErviNGSliCes" == Strongest_Extension("Slices", ['Cheese', 'SErviNGSliCes', 'StuFfed'])
assert Strongest_Extension("ClassName", ['ExtensionName']) == "ClassName.ExtensionName"
assert Strongest_Extension("Cabage", ['Tomato', 'cABBAGE']) == "Cabage.cABBAGE"
assert Strongest_Extension("Slices", ['', '', '', '']) == 'Slices.'
assert Strongest_Extension("Sandwich", ["Ketchup", "Sauce", "Mustard"]) == "Sandwich.Sauce"
assert Strongest_Extension("Bowl", ['Bowl', 'Bowl', 'Bowl']) == 'Bowl.Bowl'
assert Strongest_Extension("", ['Bowl', 'Bowl', 'Bowl']) == '.Bowl'
assert Strongest_Extension("Cheese", ['cheese']) == "Cheese.cheese"
assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("PiZZa", ['Salami', 'Pepperoni', 'Anchovies']) == "PiZZa.Salami"
assert Strongest_Extension("Bread", ['Rye', 'Wheat', 'White']) == "Bread.Rye"
assert Strongest_Extension("Bread", ['Rye', 'WHEAT', 'White']) == "Bread.WHEAT"
assert Strongest_Extension("Slices", ['SliCes', 'SliCes', 'SliCes']) == 'Slices.SliCes'
assert Strongest_Extension("Slices", ['1', '2', '3']) == 'Slices.1'
assert Strongest_Extension("Sector", ["Sectoral", "Sectarian"]) == "Sector.Sectoral"
assert Strongest_Extension("Slice", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slice.SErviNGSliCes"
assert Strongest_Extension("Pizza", ["Cheese", "StuFfed", "SErviNGSliCes"]) == "Pizza.SErviNGSliCes"
assert Strongest_Extension("Slices", ["SERVINGSLICES", "CHEESE", "STUFFED"]) == "Slices.SERVINGSLICES"
assert Strongest_Extension("Slices", ["SERVINGSLICES", "CHEESE", "STUFFED", "SERVINGS", "LICES"]) == "Slices.SERVINGSLICES"
assert Strongest_Extension("Model", ['ModelA', 'ModelB', 'ModelC']) == 'Model.ModelA'
assert Strongest_Extension("Water", ['Watermelon', 'WATER', 'Water']) == 'Water.WATER'
assert Strongest_Extension("Sauce", ['Pesto', 'Tomato', 'Teriyaki']) == 'Sauce.Pesto'
assert Strongest_Extension("Chicken", ['SAlad', 'SoPrAno']) == "Chicken.SAlad"
assert Strongest_Extension("Dough", ['TirAmiSu', 'MonTaz']) == "Dough.TirAmiSu"
assert Strongest_Extension("Dough", ['TirAmiSu', 'Dough']) == "Dough.TirAmiSu"
assert Strongest_Extension("IceCream", ['Sprinkles', 'Sprinkles']) == "IceCream.Sprinkles"
assert Strongest_Extension("Junkfood", ['Chips', 'CheeseDip', 'JelLyBeaNs']) == "Junkfood.JelLyBeaNs"
assert Strongest_Extension("Birds", ['Hawk', 'Eagle', 'Lion']) == "Birds.Hawk"
assert Strongest_Extension("A2", ['A2']) == "A2.A2"
assert Strongest_Extension("A2", ['A2', 'a2']) == "A2.A2"
assert Strongest_Extension("Cake", ["SuGar", "SpONge", "ChOcolate"]) == "Cake.SpONge"
assert Strongest_Extension("Slices", ['Cheese', 'StuFfed', 'HALF']) == "Slices.HALF"
assert Strongest_Extension("Bread", ['Breadsticks']) == 'Bread.Breadsticks'
assert Strongest_Extension("Bread", ['bread']) == 'Bread.bread'
assert Strongest_Extension("Bread", ['bread', 'Breadsticks']) == 'Bread.bread'
assert Strongest_Extension("IceCream", ['Vanilla', 'Chocolate', 'StrawBerry']) == 'IceCream.Vanilla'
assert Strongest_Extension("Slices", ['StuFfed', 'Cheese', 'SErviNGSliCes']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'with-some-more-Stuff']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Bread", ['Refined', 'Refined', 'Refined']) == 'Bread.Refined'
assert Strongest_Extension("Slices", ['SALAMI', 'COLDcuts', 'BASIC', 'SAlami']) == 'Slices.SALAMI'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'SliCes', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'SliCes', 'Cheese']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'SliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'SliCes']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Snacks", ['CanOpeners','Snackde','SnACkS']) == 'Snacks.SnACkS'
assert Strongest_Extension("Spices", ['SPices','SPICE','SpiCE','SpICe','SPICES']) == 'Spices.SPICES'
assert Strongest_Extension("Eggs", ['eggs','EGGS','egg','Egg','Eggs','EGG']) == 'Eggs.EGGS'
assert Strongest_Extension("Fruit", ['Fruit','FRUIT','FRUITS','fruits','fruit']) == 'Fruit.FRUITS'
assert Strongest_Extension("Flour", ['flour','Flour','FLOUR','FLOURS','FLOuR']) == 'Flour.FLOURS'
assert Strongest_Extension("Asparagus", ['ASPAragus', 'spring', 'Local']) == "Asparagus.ASPAragus"
assert Strongest_Extension("Car",['Toyota','Toyota','Toyota', 'Toyota']) == "Car.Toyota"
assert Strongest_Extension("Slices", ['Cheese', 'SErviNGSliCes', 'StuFfed']) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Pizza", ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Pizza', 'PiZZA']) == "Pizza.PiZZA"
assert Strongest_Extension("Soup", ['Tomato', 'Pea', 'Chicken']) == 'Soup.Pea'
assert Strongest_Extension("Slices",['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
assert Strongest_Extension("Is",['SErviNGSliCes', 'Cheese', 'StuFfed', 'Is']) == 'Is.Is'
assert Strongest_Extension("Is",['SErviNGSliCes', 'Cheese', 'StuFfed', 'Is', 'IsX']) == 'Is.IsX'
assert "Slices.SErviNGSliCes" == Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"])
assert Strongest_Extension("StuFfed", ['SErviNGSliCes', 'Cheese', 'Extension']) == "StuFfed.SErviNGSliCes"
assert Strongest_Extension("Slices", ["Cheese", "SErviNGSliCes", "StuFfed"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Slices", ["StuFfed", "SErviNGSliCes", "Cheese"]) == "Slices.SErviNGSliCes"
assert Strongest_Extension("Fried", ["fRIED", "friED", "FRiED"]) == "Fried.fRIED"
assert Strongest_Extension("Fried", ["friED", "fRIED", "FRiED"]) == "Fried.fRIED"
assert Strongest_Extension("Pizza", ["Crusted", "EXTRA", "EXTRAEXTRA"]) == "Pizza.EXTRAEXTRA"
assert Strongest_Extension("Pizza", ["EXTRAEXTRA", "EXTRA", "Crusted"]) == "Pizza.EXTRAEXTRA"
assert Strongest_Extension("Caps", ['CapsCAPS', 'cApsCapscaps']) == "Caps.CapsCAPS"
assert Strongest_Extension("Hat", ['Hat', 'Coat']) == "Hat.Hat"
assert Strongest_Extension("Cat", ['Cat', 'Bat', 'Sat']) == "Cat.Cat"
