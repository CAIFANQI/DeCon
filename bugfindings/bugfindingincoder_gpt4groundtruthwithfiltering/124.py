
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    try:
        date = date.strip()
        day, month, year = date.split('-')
        day, month, year = int(day), int(month), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True
assert not valid_date("")
assert not valid_date("   ")
assert not valid_date("   x")
assert not valid_date("   xx")
assert not valid_date("   xxx")
assert not valid_date("   xxxx")
assert not valid_date("   xxxxx")
assert not valid_date("   xxxxxx")
assert not valid_date("   xxxxxxx")
assert not valid_date("   xxxxxxxx")
assert not valid_date("   xxxxxxxxx")
assert not valid_date("   xxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxxxxxxx")
assert not valid_date("   xxxxxxxxxxxxxxxxxxxxxxxx")
assert not valid_date('13-2-2017')
assert not valid_date('13-3-2017')
assert not valid_date('13-4-2017')
assert not valid_date('13-5-2017')
assert not valid_date('13-6-2017')
assert not valid_date('13-7-2017')
assert not valid_date('13-8-2017')
assert not valid_date('13-9-2017')
assert not valid_date('13-10-2017')
assert not valid_date('13-11-2017')
assert not valid_date('13-12-2017')
assert not valid_date('13-13-2017')
assert not valid_date('13-14-2017')
assert not valid_date('13-15-2017')
assert not valid_date('13-16-2017')
assert not valid_date('13-17-2017')
assert not valid_date('13-18-2017')
assert not valid_date('13-19-2017')
assert not valid_date('13-20-2017')
assert not valid_date('13-21-2017')
assert not valid_date('13-22-2017')
assert not valid_date('13-23-2017')
assert not valid_date('13-24-2017')
assert not valid_date('13-25-2017')
assert not valid_date('13-26-2017')
assert valid_date("01-02-2020") == True
assert valid_date("01-03-2020") == True
assert valid_date("01-05-2020") == True
assert valid_date("01-06-2020") == True
assert valid_date("01-07-2020") == True
assert valid_date("01-09-2020") == True
assert valid_date("01-10-2020") == True
assert valid_date("01-11-2020") == True
assert valid_date("01-12-2020") == True
assert valid_date("02-01-2020") == True
assert valid_date("02-02-2020") == True
assert valid_date("02-03-2020") == True
assert valid_date("02-05-2020") == True
assert valid_date("02-06-2020") == True
assert valid_date("02-07-2020") == True
assert valid_date("02-09-2020") == True
assert valid_date("02-10-2020") == True
assert valid_date("02-11-2020") == True
assert valid_date("02-12-2020") == True
assert valid_date("03-01-2020") == True
assert valid_date("03-02-2020") == True
assert valid_date("03-03-2020") == True
assert valid_date("03-05-2020") == True
assert valid_date("03-06-2020") == True
assert valid_date("03-07-2020") == True
assert valid_date("03-09-2020") == True
assert valid_date("03-10-2020") == True
assert not valid_date('')
assert not valid_date('31-12-2020')
assert not valid_date('31-31-2020')
assert not valid_date('31-32-2020')
assert not valid_date('31-33-2020')
assert not valid_date('31-34-2020')
assert not valid_date('31-35-2020')
assert not valid_date('31-36-2020')
assert not valid_date('31-37-2020')
assert not valid_date('31-38-2020')
assert not valid_date('31-39-2020')
assert not valid_date('31-40-2020')
assert not valid_date('31-41-2020')
assert not valid_date('31-42-2020')
assert not valid_date('31-43-2020')
assert not valid_date('31-44-2020')
assert not valid_date('31-45-2020')
assert not valid_date('31-46-2020')
assert not valid_date('31-47-2020')
assert not valid_date('31-48-2020')
assert not valid_date('31-49-2020')
assert not valid_date('31-50-2020')
assert not valid_date('31-51-2020')
assert not valid_date('31-52-2020')
assert not valid_date('31-53-2020')
assert valid_date('01-1-1990') is True
assert valid_date('31-31-1990') is False
assert valid_date('30-01-1990') is False
assert valid_date('30-1-1990') is False
assert valid_date('30-31-1990') is False
assert valid_date('29-01-1990') is False
assert valid_date('29-1-1990') is False
assert valid_date('29-31-1990') is False
assert valid_date('28-01-1990') is False
assert valid_date('28-1-1990') is False
assert valid_date('28-31-1990') is False
assert valid_date('27-01-1990') is False
assert valid_date('27-1-1990') is False
assert valid_date('27-31-1990') is False
assert valid_date('26-01-1990') is False
assert valid_date('26-1-1990') is False
assert valid_date('26-31-1990') is False
assert valid_date('25-01-1990') is False
assert valid_date('25-1-1990') is False
assert valid_date('25-31-1990') is False
assert valid_date('02-31-20') is False
assert valid_date('02-31-21') is False
assert valid_date("02-15-2020") == True
assert valid_date('ab') == False
assert valid_date('01-01-2020') == True
assert valid_date('02-02-2020') == True
assert valid_date('03-29-2020') == True
assert valid_date('04-29-2020') == True
assert valid_date('05-29-2020') == True
assert valid_date('06-29-2020') == True
assert valid_date('07-29-2020') == True
assert valid_date('08-29-2020') == True
assert valid_date('09-29-2020') == True
assert valid_date("31-07-1999") == False
assert valid_date("30-07-1998") == False
assert valid_date("31-07-1997") == False
assert valid_date("30-07-1996") == False
assert valid_date("31-07-1995") == False
assert valid_date("30-07-1994") == False
assert valid_date("31-07-1993") == False
assert valid_date("30-07-1992") == False
assert valid_date("31-07-1991") == False
assert valid_date("30-07-1990") == False
assert valid_date("31-07-1989") == False
assert valid_date('10-01-2020')
assert not valid_date('25-12-2020')
assert not valid_date('29-01-2020')
assert not valid_date('30-12-2020')
assert not valid_date('1')
assert valid_date('02-29-2001')
assert valid_date("12-32-2019") == False
assert valid_date("01-32-2019") == False
assert valid_date("31-31-2019") == False
assert valid_date("31-32-2019") == False
assert valid_date("31-33-2019") == False
assert valid_date("31-34-2019") == False
assert valid_date("31-35-2019") == False
assert valid_date("31-36-2019") == False
assert valid_date("31-37-2019") == False
assert valid_date("31-38-2019") == False
assert valid_date("31-39-2019") == False
assert valid_date("31-41-2019") == False
assert valid_date('30-31-2018') is False
assert valid_date('29-02-2018') is False
assert valid_date('30-02-2018') is False
assert valid_date('30-11-2018') is False
assert valid_date('28-02-2012') == False
assert valid_date('31-03-2011') == False
assert valid_date('31-05-2012') == False
assert valid_date('30-07-2012') == False
assert valid_date('29-08-2012') == False
assert valid_date('31-10-2012') == False
assert valid_date('30-12-2012') == False
assert valid_date('01-02-2013') == True
assert valid_date('01-03-2013') == True
assert valid_date('01-04-2013') == True
assert valid_date('01-05-2013') == True
assert valid_date('01-06-2013') == True
assert valid_date('01-07-2013') == True
assert valid_date('01-08-2013') == True
assert valid_date('01-09-2013') == True
assert valid_date('01-10-2013') == True
assert valid_date('01-11-2013') == True
assert valid_date('01-12-2013') == True
assert valid_date('01-01-2014') == True
assert valid_date('01-02-2014') == True
assert valid_date('01-03-2014') == True
assert valid_date('01-04-2014') == True
assert valid_date('01-05-2014') == True
assert valid_date(' ')== False
assert valid_date('31-31-2013') == False
assert valid_date('31-31-2013 ') == False
assert valid_date('31-01-2013') == False
assert valid_date('31-01-2013 ') == False
assert valid_date('30-1-1') is False
assert valid_date('30-1-13') is False
assert valid_date('30-1-13-2019') is False
assert valid_date("31-07-2001") is False
assert valid_date("30-31-2016") == False
assert valid_date("31-31-2016") == False
assert valid_date('31-02-2001') is False
assert valid_date('31-01-2000') is False
assert valid_date('29-02-2000') is False
assert valid_date('29-01-2000') is False
assert valid_date('31-02-2000') is False
assert valid_date('28-02-2000') is False
assert not valid_date('31-01-2020')
assert not valid_date('30-31-2020')
assert not valid_date('30-31-2021')
assert not valid_date('29-02-2021')
assert valid_date('31-01-2020') == False
assert valid_date('29-02-2020') == False
assert valid_date('29-3-2020') == False
assert valid_date('29-4-2020') == False
assert valid_date('29-5-2020') == False
assert valid_date('29-6-2020') == False
assert valid_date('29-7-2020') == False
assert valid_date('29-8-2020') == False
assert valid_date('29-9-2020') == False
assert valid_date('29-10-2020') == False
assert valid_date('29-11-2020') == False
assert valid_date('29-12-2020') == False
assert valid_date('30-12-2020') == False
assert valid_date('30-13-2020') == False
assert valid_date('30-14-2020') == False
assert valid_date('30-15-2020') == False
assert valid_date('30-16-2020') == False
assert valid_date('30-17-2020') == False
assert valid_date('30-18-2020') == False
assert valid_date('30-19-2020') == False
assert valid_date('1-13-2017') == True
assert valid_date('1-10-2017') == True
assert valid_date('1-13-2014') == True
assert valid_date('1-10-2014') == True
assert valid_date('31-29-2014') == False
assert valid_date('30-31-2014') == False
assert valid_date('31-29-2015') == False
assert valid_date('30-31-2015') == False
assert valid_date('31-29-2016') == False
assert valid_date('30-31-2016') == False
assert valid_date('31-29-2017') == False
assert valid_date('30-31-2017') == False
assert valid_date(' ') == False
assert valid_date('1 ') == False
assert valid_date('1-') == False
assert valid_date('1 2') == False
assert valid_date('1-22') == False
assert valid_date('1 22') == False
assert valid_date('1 0-1') == False
assert valid_date('1 01-') == False
assert valid_date('01-02-2019') == True
assert valid_date('04-02-2019') == True
assert valid_date('10-02-2019') == True
assert valid_date('14-02-2019') == False
assert valid_date('01-01-1900') == True
assert valid_date('01-02-2015') == True
assert valid_date('12-01-2012')
assert valid_date('11-11-2012')
assert valid_date('10-23-2012')
assert valid_date('08-15-2012')
assert valid_date('07-08-2012')
assert valid_date('06-07-2012')
assert valid_date('05-06-2012')
assert valid_date('12-02-2012')
assert valid_date('12-16-2012')
assert valid_date('12-15-2014')
assert valid_date('12-01-2014')
assert valid_date('11-11-2014')
assert valid_date('10-23-2014')
assert valid_date('08-15-2014')
assert valid_date('07-08-2014')
assert valid_date('06-07-2014')
assert valid_date('05-06-2014')
assert valid_date('12-02-2014')
assert valid_date('12-16-2014')
assert valid_date('12-15-2015')
assert valid_date('12-01-2015')
assert valid_date('31-12-2010') is False
assert valid_date('28-02-2010') is False
assert valid_date('29-02-2010') is False
assert valid_date('01-01-2011') is True
assert valid_date('01-01-2012') is True
assert valid_date("0-1-2019") == False
assert valid_date("31-1-2019") == False
assert valid_date("30-1-19") == False
assert valid_date("31-1-19") == False
assert valid_date("30-1-18") == False
assert valid_date("31-1-17") == False
assert valid_date("30-1-16") == False
assert valid_date("31-1-15") == False
assert valid_date("30-1-14") == False
assert valid_date("31-1-13") == False
assert valid_date("30-1-12") == False
assert valid_date("31-1-11") == False
assert valid_date("30-1-11") == False
assert valid_date("31-1-10") == False
assert valid_date("30-1-9") == False
assert valid_date("31-1-8") == False
assert valid_date("30-1-7") == False
assert valid_date("31-1-6") == False
assert valid_date("30-1-5") == False
assert valid_date("31-1-4") == False
assert valid_date("30-1-3") == False
assert valid_date('11-28-2014') == True
assert valid_date('12-21-2014') == True
assert valid_date('30-31-2018') == False
assert valid_date('30-31-2019') == False
assert valid_date('30-31-2020') == False
assert valid_date('30-31-202') == False
assert valid_date('30-31-203') == False
assert valid_date('30-31-204') == False
assert valid_date('31-12-2016') == False
assert valid_date('30-12-2016') == False
assert valid_date('31-12-2099') == False
assert valid_date('31-01-2000') == False
assert valid_date('31-01-1999') == False
assert valid_date('31-12-2000') == False
assert valid_date('31-12-1999') == False
assert valid_date('31-12-2003') == False
assert valid_date('31-12-2004') == False
assert valid_date('31-12-2005') == False
assert valid_date('31-12-2006') == False
assert valid_date('31-12-2007') == False
assert valid_date('31-12-2008') == False
assert valid_date('31-12-2009') == False
assert valid_date('31-12-2010') == False
assert valid_date('31-12-2011') == False
assert valid_date('31-12-2012') == False
assert valid_date('31-12-2013') == False
assert valid_date('31-12-2014') == False
assert valid_date("1-01-1978") == True
assert valid_date("31-12-2000") == False
assert valid_date("31-12-12") == False
assert valid_date('12-34-2015') is False
assert valid_date('31-01-2015') is False
assert valid_date('30-31-2015') is False
assert valid_date('31-30-2015') is False
assert valid_date('31-31-2015') is False
assert valid_date('30-01-2015') is False
assert valid_date('12-03-2020')
assert valid_date('04-05-2020')
assert valid_date('06-05-2020')
assert valid_date('09-05-2020')
assert valid_date('11-05-2020')
assert valid_date('03-07-2020')
assert valid_date('07-07-2020')
assert valid_date('08-07-2020')
assert valid_date('10-07-2020')
assert valid_date('11-07-2020')
assert valid_date('05-09-2020')
assert valid_date('08-09-2020')
assert valid_date('11-09-2020')
assert valid_date('02-11-2020')
assert valid_date('03-11-2020')
assert valid_date('07-11-2020')
assert valid_date('08-11-2020')
assert valid_date('09-11-2020')
assert valid_date('10-11-2020')
assert valid_date('12-11-2020')
assert valid_date("02-29-2000") == True
assert valid_date("01-01-1900") == True
assert valid_date("02-29-1900") == True
assert valid_date("01-01-2020") == True
assert valid_date("02-29-2020") == True
assert valid_date('06-29-2019') == True
assert valid_date('06-01-2020') == True
assert valid_date('06-02-2020') == True
assert not valid_date('32-04-2019')
assert not valid_date('28-01-2019')
assert not valid_date('28-02-2019')
assert not valid_date('28-01-2020')
assert not valid_date('31-02-2020')
assert not valid_date('31-03-2020')
assert not valid_date('30-02-2020')
assert not valid_date('30-03-2020')
assert not valid_date('30-05-2020')
assert not valid_date('31-03-2021')
assert not valid_date('28-06-2020')
assert not valid_date('31-09-2020')
assert not valid_date('30-06-2020')
assert valid_date('02-02-2018')
assert valid_date('02-29-2018')
assert valid_date('01-02-2019')
assert valid_date('02-02-2019')
assert valid_date('02-29-2019')
assert valid_date('   ') == False
assert valid_date('1-01-2000') == True
assert valid_date('2-29-2000') == True
assert valid_date('2-29-2001') == True
assert valid_date('02-29-2000') == True
assert valid_date('02-29-2001') == True
assert valid_date('02-29-2002') == True
assert valid_date('30-02-2020') == False
assert valid_date('29-02-2019') == False
assert valid_date('01-02-2000') == True
assert valid_date('30-31-1900') == False
assert valid_date('31-02-1900') == False
assert valid_date('31-03-1900') == False
assert valid_date('01-02-2017') == True
assert valid_date('31-03-2017') == False
assert valid_date('31-12-20') is False
assert valid_date('30-31-12') is False
assert valid_date('30-31-2020') is False
assert valid_date('31-29-2020') is False
assert valid_date('30-31-200') is False
assert valid_date('29-30-2020') is False
assert valid_date('29-30-200') is False
assert valid_date('31-31-2020') is False
assert valid_date('31-29-200') is False
assert valid_date('31-31-200') is False
assert not valid_date("13-12-2001")
assert not valid_date("31-12-2001")
assert valid_date("01-00-2019") == False
assert valid_date("31-02-2019") == False
assert valid_date("31-00-2019") == False
assert valid_date("00-00-2019") == False
assert valid_date("31-00-2020") == False
assert valid_date('1-01-2017')
assert not valid_date('31-31-2017')
assert not valid_date('31-12-2017')
assert not valid_date('30-31-2017')
assert not valid_date('29-31-2017')
assert not valid_date('0-12-2017')
assert not valid_date('01-32-2017')
assert valid_date("03-29-2019") == True
assert valid_date('2-29-2020') == True
assert valid_date('31-31-2020') == False
assert valid_date('31-02-2020') == False
assert valid_date('31-12-2020') == False
assert not valid_date('31-15-2018')
assert not valid_date('30-15-2018')
assert not valid_date('29-15-2018')
assert not valid_date('31-15-2015')
assert not valid_date('30-15-2015')
assert valid_date('02-01-2020')
assert not valid_date('01-00-2020')
assert valid_date("13-2-2013") == False
assert not valid_date('25-31-2020')
assert valid_date('30-31-2011') == False
assert valid_date('1-12-2011') == True
assert valid_date('31-31-2011') == False
assert valid_date("31-02-2015") == False
assert valid_date('1-01-2010') == True
assert valid_date('2-29-2010') == True
assert valid_date('30-11-2010') == False
assert valid_date('1-01-1101') == True
assert valid_date('30-12-2010') == False
assert valid_date('31-11-2011') == False
assert valid_date('29-02-2011') == False
assert valid_date('29-02-2012') == False
assert valid_date('29-02-2013') == False
assert valid_date('29-02-2014') == False
assert valid_date('29-02-2015') == False
assert not valid_date('abc')
assert not valid_date('30-01-2000')
assert not valid_date('29-feb-2010')
assert not valid_date('31-31-2000')
assert not valid_date('29-feb-2011')
assert valid_date('02-02-2010')
assert valid_date('02-02-2020')
assert valid_date('02-29-2020')
assert valid_date('01-15-2011')
assert valid_date('01-16-2011')
assert valid_date('01-16-2010')
assert valid_date('25-25-1988') == False
assert valid_date('22-25-1988') == False
assert valid_date('21-25-1988') == False
assert valid_date('23-25-1988') == False
assert valid_date('20-25-1988') == False
assert valid_date('a') == False
assert valid_date('02') == False
assert valid_date('04-29') == False
assert not valid_date('31-12-2000')
assert not valid_date('31-32-1999')
assert valid_date('02-21-2019') == True
assert valid_date('02-21-2021') == True
assert valid_date('02-01-2018') == True
assert valid_date('30-05-2017') == False
assert valid_date('30-02-2015') == False
assert valid_date('30-11-2015') == False
assert valid_date('31-01-2016') == False
assert valid_date('29-02-2016') == False
assert valid_date('29-11-2016') == False
assert valid_date("30-02-2020") is False
assert valid_date("01-01-2020") is True
assert valid_date("01-12-2020") is True
assert valid_date('13-08-1999') == False
assert valid_date('13-13-2019') == False
assert valid_date('13-31-2019') == False
assert valid_date('13-01-2019') == False
assert valid_date("21-30-2020") == False
assert valid_date("21-31-2020") == False
assert valid_date("21-31-2099") == False
assert valid_date('31-31-2099') == False
assert not valid_date('31-1-2013'), 'Months are 31 to 12'
assert not valid_date('29-2-2013'), 'Months are 29 and 2nd'
assert valid_date('01-01-2013'), 'Date should be in the format: mm-dd-yyyy'
assert valid_date('19-00-2020') == False
assert not valid_date("a1")
assert not valid_date("29-29-2010")
assert valid_date('31-02-2015') is False
assert valid_date('11-31-20') == False
assert valid_date('21-03-2000') is False
assert valid_date('20-23-2003') is False
assert valid_date('23-23-2023') is False
assert valid_date('23-23-23') is False
assert valid_date('23-23-') is False
assert valid_date('') is False
assert valid_date('3-1-2019')
assert valid_date('2-3-2019')
assert valid_date('12-13-2019')
assert valid_date('10-6-2019')
assert valid_date('1-05-2012')
assert valid_date('011-11-2012')
assert valid_date('02-02-2012')
assert valid_date('03-01-2012')
assert valid_date('10-02-2018') == True
assert valid_date('30-02-2017') == False
assert valid_date('30-02-18') == False
assert valid_date('  ') == False
assert valid_date('13-1-2068') == False
assert valid_date('31-05-2019') == False
assert valid_date('25-02-2010') == False
assert valid_date("10-5-1996")
assert valid_date("12-12-2013")
assert valid_date("12-1-1996")
assert valid_date("12-1-1976")
assert valid_date("10-5-2013")
assert valid_date("10-29-1976")
assert valid_date("10-29-1996")
assert valid_date("12-1-2001")
assert valid_date('02-11-1986') == True
assert valid_date('22-12-1980') == False
assert valid_date('30-4-2001') == False
