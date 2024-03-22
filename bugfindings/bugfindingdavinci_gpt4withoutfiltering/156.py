
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i]
        i -= 1
    return res.lower()
assert 'x' == int_to_mini_roman(10)
assert 'iii' == int_to_mini_roman(3)
assert 'xxix' == int_to_mini_roman(29)
assert 'xxxiii' == int_to_mini_roman(33)
assert 'lxxxix' == int_to_mini_roman(89)
assert 'xc' == int_to_mini_roman(90)
assert 'ccc' == int_to_mini_roman(300)
assert 'cdxciii' == int_to_mini_roman(493)
assert 'dxcix' == int_to_mini_roman(599)
assert 'cm' == int_to_mini_roman(900)
assert 'cmxcix' == int_to_mini_roman(999)
assert 'm' == int_to_mini_roman(1000)
assert int_to_mini_roman(3) == 'iii'
assert int_to_mini_roman(10) == 'x'
assert int_to_mini_roman(59) == 'lix'
assert int_to_mini_roman(93) == 'xciii'
assert int_to_mini_roman(141) == 'cxli'
assert int_to_mini_roman(163) == 'clxiii'
assert int_to_mini_roman(402) == 'cdii'
assert int_to_mini_roman(911) == 'cmxi'
assert int_to_mini_roman(1024) == 'mxxiv'
assert int_to_mini_roman(3000) == 'mmm'
assert int_to_mini_roman(5) == 'v'
assert int_to_mini_roman(13) == 'xiii'
assert int_to_mini_roman(49) == 'xlix'
assert int_to_mini_roman(2) == 'ii'
assert int_to_mini_roman(9) == 'ix'
assert int_to_mini_roman(42) == 'xlii'
assert int_to_mini_roman(99) == 'xcix'
assert int_to_mini_roman(499) == 'cdxcix'
assert int_to_mini_roman(999) == 'cmxcix'
assert int_to_mini_roman(1000) == 'm'
assert int_to_mini_roman(4) == 'iv'
assert int_to_mini_roman(11) == 'xi'
assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(22) == 'xxii'
assert int_to_mini_roman(15) == 'xv'
assert int_to_mini_roman(1001) == 'mi'
assert int_to_mini_roman(1990) == 'mcmxc'
assert int_to_mini_roman(2007) == 'mmvii'
assert int_to_mini_roman(2008) == 'mmviii'
assert int_to_mini_roman(150) == 'cl'
assert int_to_mini_roman(80) == 'lxxx'
assert int_to_mini_roman(8) == 'viii'
assert int_to_mini_roman(50) == 'l'
assert int_to_mini_roman(100) == 'c'
assert int_to_mini_roman(500) == 'd'
assert int_to_mini_roman(6) == 'vi'
assert int_to_mini_roman(18) == 'xviii'
assert int_to_mini_roman(666) == 'dclxvi'
assert int_to_mini_roman(2019) == 'mmxix'
assert int_to_mini_roman(201) == 'cci'
assert int_to_mini_roman(79) == 'lxxix'
assert int_to_mini_roman(48) == 'xlviii'
assert int_to_mini_roman(575) == 'dlxxv'
assert int_to_mini_roman(7) == 'vii'
assert int_to_mini_roman(12) == 'xii'
assert int_to_mini_roman(16) == 'xvi'
assert int_to_mini_roman(20) == 'xx'
assert int_to_mini_roman(30) == 'xxx'
assert int_to_mini_roman(60) == 'lx'
assert int_to_mini_roman(70) == 'lxx'
assert int_to_mini_roman(25) == 'xxv'
assert int_to_mini_roman(256) == 'cclvi'
assert int_to_mini_roman(39) == 'xxxix'
assert int_to_mini_roman(242) == 'ccxlii'
assert int_to_mini_roman(37) == 'xxxvii'
assert int_to_mini_roman(137) == 'cxxxvii'
assert int_to_mini_roman(939) == 'cmxxxix'
assert int_to_mini_roman(919) == 'cmxix'
assert int_to_mini_roman(43) == 'xliii'
assert int_to_mini_roman(400) == 'cd'
assert int_to_mini_roman(399) == 'cccxcix'
assert int_to_mini_roman(24) == 'xxiv'
assert (int_to_mini_roman(4) == 'iv')
assert (int_to_mini_roman(9) == 'ix')
assert (int_to_mini_roman(40) == 'xl')
assert (int_to_mini_roman(90) == 'xc')
assert (int_to_mini_roman(400) == 'cd')
assert (int_to_mini_roman(900) == 'cm')
assert (int_to_mini_roman(666) == 'dclxvi')
assert int_to_mini_roman(155) == 'clv'
assert int_to_mini_roman(40) == 'xl'
assert int_to_mini_roman(90) == 'xc'
assert int_to_mini_roman(900) == 'cm'
assert int_to_mini_roman(55) == 'lv'
assert int_to_mini_roman(14) == 'xiv'
assert int_to_mini_roman(300) == 'ccc'
assert int_to_mini_roman(444) == 'cdxliv'
assert int_to_mini_roman(58) == 'lviii'
assert int_to_mini_roman(1999) == 'mcmxcix'
assert int_to_mini_roman(17) == 'xvii'
assert int_to_mini_roman(943) == 'cmxliii'
assert (int_to_mini_roman(5) == 'v')
assert (int_to_mini_roman(10) == 'x')
assert (int_to_mini_roman(50) == 'l')
assert (int_to_mini_roman(100) == 'c')
assert (int_to_mini_roman(500) == 'd')
assert (int_to_mini_roman(1000) == 'm')
assert (int_to_mini_roman(1001) == 'mi')
assert (int_to_mini_roman(1999) == 'mcmxcix')
assert (int_to_mini_roman(45) == 'xlv')
assert (int_to_mini_roman(99) == 'xcix')
assert (int_to_mini_roman(246) == 'ccxlvi')
assert (int_to_mini_roman(721) == 'dccxxi')
assert (int_to_mini_roman(999) == 'cmxcix')
assert (int_to_mini_roman(1666) == 'mdclxvi')
assert int_to_mini_roman(34) == 'xxxiv'
assert int_to_mini_roman(44) == 'xliv'
assert int_to_mini_roman(77) == 'lxxvii'
assert int_to_mini_roman(140) == 'cxl'
assert int_to_mini_roman(156) == 'clvi'
assert int_to_mini_roman(177) == 'clxxvii'
assert int_to_mini_roman(200) == 'cc'
assert int_to_mini_roman(111) == 'cxi'
assert int_to_mini_roman(1111) == 'mcxi'
assert int_to_mini_roman(21) == 'xxi'
assert int_to_mini_roman(27) == 'xxvii'
assert int_to_mini_roman(28) == 'xxviii'
assert int_to_mini_roman(33) == 'xxxiii'
assert int_to_mini_roman(38) == 'xxxviii'
assert int_to_mini_roman(860) == 'dccclx'
assert int_to_mini_roman(64) == 'lxiv'
assert int_to_mini_roman(1) == 'i'
assert int_to_mini_roman(45) == 'xlv'
assert int_to_mini_roman(195) == 'cxcv'
assert int_to_mini_roman(1066) == 'mlxvi'
assert int_to_mini_roman(450) == 'cdl'
assert int_to_mini_roman(29) == 'xxix'
assert int_to_mini_roman(31) == 'xxxi'
assert int_to_mini_roman(75) == 'lxxv'
assert int_to_mini_roman(23) == 'xxiii'
assert "ii" == int_to_mini_roman(2)
assert "iii" == int_to_mini_roman(3)
assert "iv" == int_to_mini_roman(4)
assert "v" == int_to_mini_roman(5)
assert "ix" == int_to_mini_roman(9)
assert "xlii" == int_to_mini_roman(42)
assert "xlviii" == int_to_mini_roman(48)
assert "lxix" == int_to_mini_roman(69)
assert "xcviii" == int_to_mini_roman(98)
assert "cxxxiii" == int_to_mini_roman(133)
assert "cdxlix" == int_to_mini_roman(449)
assert "mcclxxi" == int_to_mini_roman(1271)
assert int_to_mini_roman(143) == 'cxliii'
assert int_to_mini_roman(1007) == 'mvii'
assert int_to_mini_roman(98) == 'xcviii'
assert int_to_mini_roman(68) == 'lxviii'
assert int_to_mini_roman(164) == 'clxiv'
assert int_to_mini_roman(356) == 'ccclvi'
assert int_to_mini_roman(1700) == 'mdcc'
assert int_to_mini_roman(78) == 'lxxviii'
assert int_to_mini_roman(710) == 'dccx'
assert int_to_mini_roman(101) == 'ci'
assert int_to_mini_roman(550) == 'dl'
assert int_to_mini_roman(530) == 'dxxx'
assert int_to_mini_roman(106) == 'cvi'
assert int_to_mini_roman(209) == 'ccix'
assert int_to_mini_roman(51) == 'li'
assert int_to_mini_roman(501) == 'di'
assert int_to_mini_roman(46) == 'xlvi'
assert int_to_mini_roman(253) == 'ccliii'
assert int_to_mini_roman(456) == 'cdlvi'
assert int_to_mini_roman(555) == 'dlv'
assert int_to_mini_roman(901) == 'cmi'
assert int_to_mini_roman(97) == 'xcvii'
assert int_to_mini_roman(754) == 'dccliv'
assert int_to_mini_roman(821) == 'dcccxxi'
assert int_to_mini_roman(2000) == 'mm'
assert int_to_mini_roman(56) == 'lvi'
assert int_to_mini_roman(142) == 'cxlii'
assert int_to_mini_roman(997) == 'cmxcvii'
assert int_to_mini_roman(749) == 'dccxlix'
assert int_to_mini_roman(800) == 'dccc'
assert int_to_mini_roman(599) == 'dxcix'
assert int_to_mini_roman(144) == 'cxliv'
assert int_to_mini_roman(2001) == 'mmi'
assert int_to_mini_roman(955) == 'cmlv'
assert int_to_mini_roman(199) == 'cxcix'
assert int_to_mini_roman(2555) == 'mmdlv'
assert int_to_mini_roman(944) == 'cmxliv'
assert int_to_mini_roman(254) == 'ccliv'
assert int_to_mini_roman(1200) == 'mcc'
assert int_to_mini_roman(700) == 'dcc'
assert int_to_mini_roman(934) == 'cmxxxiv'
assert int_to_mini_roman(1666) == 'mdclxvi'
assert int_to_mini_roman(72) == 'lxxii'
assert int_to_mini_roman(52) == 'lii'
assert int_to_mini_roman(32) == 'xxxii'
assert int_to_mini_roman(89) == 'lxxxix'
assert int_to_mini_roman(850) == 'dcccl'
assert int_to_mini_roman(1) == "i"
assert int_to_mini_roman(10) == "x"
assert int_to_mini_roman(99) == "xcix"
assert int_to_mini_roman(1000) == "m"
