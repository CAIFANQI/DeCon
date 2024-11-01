
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
assert valid_date("01-32-2010") == False
assert valid_date("01-29-2010") == True
assert valid_date("13-31-2010") == False
assert valid_date("31-01-2010") == False
assert valid_date("29-01-2011") == False
assert valid_date("0-1-2010") == False
assert valid_date("1-1-2010") == True
assert valid_date("") == False
assert valid_date("00-00-0000") == False
assert valid_date("12-25-2013") == True
assert valid_date("02-29-2004") == True
assert valid_date("2-28-2009") == True
assert valid_date("01-12-2016") == True
assert valid_date("1-01-2017") == True
assert valid_date("01-1-2017") == True
assert valid_date("1-1-2017") == True
assert valid_date("02-29-2016") == True
assert valid_date("02/29/2016") == False
assert valid_date("00-29-2016") == False
assert valid_date("13-29-2016") == False
assert valid_date("02-00-2016") == False
assert valid_date("02-32-2016") == False
assert valid_date("-2-29-2016") == False
assert valid_date("15-10-18") == False
assert valid_date("10-35-2018") == False
assert valid_date("10-10-2018") == True
assert valid_date("00-10-1018") == False
assert valid_date("55-10-2018") == False
assert valid_date("55-55-5555") == False
assert valid_date("10-00-2018") == False
assert valid_date("10-00-0000") == False
assert valid_date("15-10-18-2018") == False
assert valid_date("10-10-2018-15") == False
assert valid_date("10-10-2018-10-10-10") == False
assert valid_date("1010-10-2018") == False
assert valid_date("10-1010-2018") == False
assert valid_date("1010-1010-2018") == False
assert valid_date("01-02-2003") == True
assert valid_date("1-1-1999") == True
assert valid_date("30-2-2000") == False
assert valid_date("01-02-2001") == True
assert valid_date("5-5-2080") == True
assert valid_date("2-2-2016") == True
assert valid_date("2-2-2000") == True
assert valid_date("1-1-1990") == True
assert valid_date("1-1-2003") == True
assert valid_date("3-3-1993") == True
assert valid_date("2-2-1999") == True
assert valid_date("2-2-1993") == True
assert valid_date("10-4-2000") == True
assert valid_date("13-30-1992") == False
assert valid_date("22-06-198") == False
assert valid_date("12-05-2018") == True
assert valid_date("03-05-2019") == True
assert valid_date("12-10-2019") == True
assert valid_date("12-32-2019") == False
assert valid_date("13-05-2019") == False
assert valid_date("00-05-2019") == False
assert valid_date("01-00-2019") == False
assert valid_date("01-01-2019") == True
assert valid_date("02-28-2019") == True
assert valid_date("02-28-2020") == True
assert valid_date("15-05-2020") == False
assert valid_date("15-5-2020") == False
assert valid_date("15-05-21") == False
assert valid_date("100-5-2020") == False
assert valid_date("5-100-2020") == False
assert valid_date("02-29-2020") == True
assert not valid_date("13-31-3001")
assert valid_date("01-15-2016") == True
assert valid_date("2-29-2016") == True
assert valid_date("2-40-2018") == False
assert valid_date("03-32-2016") == False
assert valid_date("2-32-2016") == False
assert valid_date("13-31-2018") == False
assert valid_date("12-32-2018") == False
assert valid_date("1-1-2019") == True
assert valid_date("02-29-2019") == True
assert valid_date("12/31/2018") == False
assert valid_date("12/31/18") == False
assert valid_date("12/31/201") == False
assert valid_date("12/31/20189") == False
assert valid_date("12-") == False
assert valid_date("1-") == False
assert valid_date("15-15-1999") == False
assert valid_date("01-01-2001") == True
assert valid_date("00-01-2001") == False
assert valid_date("03-03-2003") == True
assert valid_date("04-04-2004") == True
assert valid_date("05-05-2005") == True
assert valid_date("06-06-2006") == True
assert valid_date("07-07-2007") == True
assert valid_date("08-08-2008") == True
assert valid_date("09-09-2009") == True
assert valid_date("10-10-2010") == True
assert valid_date("11-11-2011") == True
assert valid_date("12-12-2012") == True
assert valid_date("11-12-2019") is True
assert valid_date("12-12-2019") is True
assert valid_date("12-20-2019") is True
assert valid_date("13-13-2019") is False
assert valid_date("12-11-2019") is True
assert valid_date("12-11-2020") is True
assert valid_date("") is False
assert valid_date("12122019") is False
assert valid_date("12-11-2020-") is False
assert valid_date("01-05-2003") == True
assert valid_date("12-01-2004") == True
assert valid_date("12-20-2004") == True
assert valid_date("13-01-2004") == False
assert valid_date("12-40-2004") == False
assert valid_date("12-01-2040") == True
assert valid_date("1201-2004") == False
assert valid_date("1") == False
assert valid_date("01-45-2018") == False
assert valid_date("01-05-1989") == True
assert valid_date("12-24-2011") == True
assert valid_date("10-10") == False
assert valid_date("10-210-2010") == False
assert valid_date("10-32-2010") == False
assert valid_date("10-00-2010") == False
assert valid_date("10.10.2010") == False
assert valid_date("13-10-2010") == False
assert valid_date("12-35-1980") == False
assert valid_date("00-35-1980") == False
assert valid_date("13-12-1980") == False
assert valid_date("12-12-1980") == True
assert valid_date("12-21-1980") == True
assert valid_date("02-29-1980") == True
assert valid_date("29-02-1900") == False
assert valid_date("00-31-2010") == False
assert valid_date("01-00-2010") == False
assert valid_date("01-40-2010") == False
assert valid_date("01-29-2012") == True
assert valid_date("1-1-2000") == True
assert valid_date("12-1-2000") == True
assert valid_date("1-1-1900") == True
assert valid_date("0-1-2000") == False
assert valid_date("1-0-2000") == False
assert valid_date("13-1-2000") == False
assert valid_date("1-32-2000") == False
assert valid_date("12-0-2000") == False
assert valid_date("2-29-2000") == True
assert valid_date("12-01-1994") == True
assert valid_date("01-32-1994") == False
assert valid_date("12-32-1994") == False
assert valid_date("02-29-1994") == True
assert valid_date("14-01-1994") == False
assert valid_date("12-01-1944") == True
assert valid_date("30-11-2012") is False
assert valid_date("12-00-2012") is False
assert valid_date("12-32-2012") is False
assert valid_date("11-29-2012") is True
assert valid_date("2-29-2012") is True
assert valid_date("13-32-2012") is False
assert valid_date("11-31-201") is False
assert valid_date("01-32-2019") == False
assert valid_date("08-29-2017") == True
assert valid_date("08-28-2017") == True
assert valid_date("08-27-2017") == True
assert valid_date("12-29-2017") == True
assert valid_date("12-28-2017") == True
assert valid_date("12-27-2017") == True
assert valid_date("02-28-2018") == True
assert valid_date("01-32-2016") == False
assert valid_date("13-01-2016") == False
assert valid_date("12-00-2016") == False
assert valid_date("13-25-2016") == False
assert valid_date("12-32-2016") == False
assert valid_date("12-25-2015") == True
assert valid_date("abc") == False
assert valid_date("10-10-2050") == True
assert valid_date("10-10-2000") == True
assert valid_date("10-10-1999") == True
assert valid_date("01-50-2010") == False
assert valid_date("01-12-2015") == True
assert valid_date("01-0-2015") == False
assert valid_date("01-32-2015") == False
assert valid_date("03-01-2015") == True
assert valid_date("2-29-2004") == True
assert valid_date("21-12-2012") == False
assert valid_date("12-15-2013") == True
assert valid_date("02-29-2000") == True
assert valid_date("13-15-2013") == False
assert valid_date("15-15-2013") == False
assert valid_date("-12-24-2010") is False
assert valid_date("12-24") is False
assert valid_date("-12-24-") is False
assert valid_date("12-00-2010") is False
assert valid_date("12-32-2010") is False
assert valid_date("12-40-2010") is False
assert valid_date("05-25-2020-12") == False
assert valid_date("15-40-2020") == False
assert valid_date("15-40-20") == False
assert valid_date("15-40-2020-20") == False
assert valid_date("1-1-2011") == True
assert valid_date("12-00-2015") == False
assert valid_date("13-06-1990") == False
assert valid_date("12-32-1990") == False
assert valid_date("12/06/1990") == False
assert valid_date("01-05-2007") == True
assert valid_date("11-01-2007") == True
assert valid_date("10-12-2007") == True
assert valid_date("10-10-2007") == True
assert valid_date("10-07-2010") == True
assert valid_date("15-15-2007") == False
assert valid_date("2-28-2007") == True
assert valid_date("15-11-2007") == False
assert valid_date("2-29-2008") == True
assert valid_date("-12-25-2007") == False
assert valid_date("12-25-2007-") == False
assert valid_date("09-29-1973") == True
assert valid_date("32-10-2020") == False
assert valid_date("1-0-2020") == False
assert valid_date("29-02-2021") == False
assert valid_date("05-33-2020") == False
assert valid_date("00-34-2000") == False
assert valid_date("13-03-2015") == False
assert valid_date("31-02-2015") == False
assert valid_date("00-12-2015") == False
assert valid_date("31-09-2018") == False
assert valid_date("32-09-2018") == False
assert valid_date("32-04-2018") == False
assert valid_date("32-13-2018") == False
assert valid_date("32-11-2018") == False
assert valid_date("30-02-2016") == False
assert valid_date("31-02-2016") == False
assert valid_date("29-02-2017") == False
assert valid_date("12-32-2000") == False
assert valid_date("00-01-2000") == False
assert valid_date("11-01-2000") == True
assert valid_date("01-32-2000") == False
assert valid_date("10-32-2000") == False
assert valid_date("02-29-1004") == True
assert valid_date("01-12-2020") == True
assert valid_date("99-99-9999") == False
assert valid_date("01-00-2020") == False
assert valid_date("12-00-2000") == False
assert valid_date("11-20-2018") is True
assert valid_date("11-33-2018") is False
assert valid_date("02-23-2018") is True
assert valid_date("01-22-2018") is True
assert valid_date("12-00-2018") is False
assert valid_date("12-23-2018") is True
assert valid_date("11-20-20-2018") is False
assert valid_date("11-20-20-201-8") is False
assert valid_date("01-28-2012") == True
assert valid_date("01-35-2013") == False
assert valid_date("13-01-2013") == False
assert valid_date("12-00-2013") == False
assert valid_date("12-32-2013") == False
assert valid_date("01-01-2013") == True
assert valid_date("01-28-2000") == True
assert valid_date("01-32-20") == False
assert valid_date("01-32-200") == False
assert valid_date("01-32-20002") == False
assert valid_date("13-32-2000") == False
assert valid_date("13-32-20") == False
assert valid_date("13-32-200") == False
assert valid_date("13-32-20002") == False
assert valid_date("00-32-2000") == False
assert valid_date("00-32-20") == False
assert valid_date("00-32-200") == False
assert valid_date("00-32-20002") == False
assert valid_date("01-22-2000") == True
assert not valid_date("hi")
assert not valid_date("01-01-2017-02")
assert not valid_date("32-01-2017")
assert not valid_date("01-00-2017")
assert not valid_date("01-32-2017")
assert valid_date("12-01-2017")
assert valid_date("01-01-2017")
assert valid_date("02-28-2017")
assert valid_date("01-01-1992")
assert valid_date("01-01-0000")
assert valid_date("12-32-2010") == False
assert valid_date("02-29-2012") == True
assert valid_date("1-32-1999") == False
assert valid_date("-1-1-1999") == False
assert valid_date("01-01-1999") == True
assert valid_date("01-1999") == False
assert valid_date("01-02-2019") == True
assert valid_date("12-32-1999") == False
assert valid_date("01-32-1999") == False
assert valid_date("2-29-2012") == True
assert valid_date("30-15-2020") == False
assert valid_date("01-12-2001") == True
assert valid_date("12-01-2001") == True
assert valid_date("11-12-2001") == True
assert valid_date("02-28-2001") == True
assert valid_date("12-33-2001") == False
assert valid_date("05-33-2001") == False
assert valid_date("12-12-2000") == True
assert valid_date("12-12-2001") == True
assert valid_date("-12-12-2") == False
assert valid_date("12--12-2") == False
assert valid_date("02-00-2020") == False
assert valid_date("14-02-1991") == False
assert valid_date("12-00-1991") == False
assert valid_date("02-29-1992") == True
assert valid_date("05-32-1991") == False
assert valid_date("13-02-1991") == False
assert valid_date("03-03-1909") == True
assert valid_date("09/05/2019") == False
assert valid_date("09/05/19") == False
assert valid_date("11-10-2017") == True
assert valid_date("15-03-2001") == False
assert valid_date("03-15-2001") == True
assert valid_date("03-15-2000") == True
assert valid_date("12/05/2019") == False
assert valid_date("11-10-9999") == True
assert valid_date("11-10-2000") == True
assert valid_date("12-40-2019") == False
assert valid_date("32-10-2019") == False
assert valid_date("12-29-2000") == True
assert valid_date("11-12-2019") == True
assert valid_date("01-12-2019") == True
assert valid_date("2-28-1995") == True
assert valid_date("02-28-2000") == True
assert valid_date("12-13-2019") == True
assert valid_date("01-12-2009") == True
assert valid_date("13-01-2009") == False
assert valid_date("11-12-2018") == True
assert valid_date("11-10-2018") == True
assert valid_date("01-10-2018") == True
assert valid_date("02-10-2018") == True
assert valid_date("03-10-2018") == True
assert valid_date("04-10-2018") == True
assert valid_date("05-10-2018") == True
assert valid_date("06-10-2018") == True
assert valid_date("07-10-2018") == True
assert valid_date("08-10-2018") == True
assert valid_date("09-10-2018") == True
assert valid_date("12-10-2018") == True
assert valid_date("12-21-2012") == True
assert valid_date("12-15-2012") == True
assert valid_date("04-32-2012") == False
assert valid_date("12-15-2112") == True
assert valid_date("01-15-2017") == True
assert valid_date("01-05-2017") == True
assert valid_date("01-32-2017") == False
assert valid_date("01-15-2022") == True
assert valid_date("01-15-2017-10") == False
assert valid_date("01/15/2017") == False
assert valid_date("01 15 2017") == False
assert valid_date("01.15.2017") == False
assert valid_date("02-28-2010") == True
assert valid_date("02-29-2008") == True
assert valid_date("01-13-2014") == True
assert valid_date("01-32-2014") == False
assert valid_date("12-00-2014") == False
assert valid_date("12-32-2014") == False
assert valid_date("02-29-2014") == True
assert valid_date("01-0-2014") == False
assert valid_date("2-29-2020") == True
assert valid_date("3-32-2020") == False
assert valid_date("01-02-2020") == True
assert valid_date("00-11-2000") == False
assert valid_date("32-11-2000") == False
assert valid_date("30-00-2000") == False
assert valid_date("30-13-2000") == False
assert valid_date("29-02-2100") == False
assert valid_date("29-02-2001") == False
assert valid_date("02-34-2019") == False
assert valid_date("12-34-2019") == False
assert valid_date("13-11-2019") == False
assert valid_date("99-99-2019") == False
assert valid_date("01-40-2016") == False
assert valid_date("01-13-2012") == True
assert valid_date("01-50-2012") == False
assert valid_date("14-20-2018") == False
assert valid_date("01-12-2014") == True
assert valid_date("14-01-2018") == False
assert valid_date("01-56-2010") == False
assert valid_date("01-30-2010-1") == False
assert valid_date("-1-30-2010") == False
assert valid_date("13-30-2010") == False
assert valid_date("5-10-2015") == True
assert valid_date("5-0-2015") == False
assert valid_date("5-0-10") == False
assert valid_date("5-20-2015") == True
assert valid_date("02-29-2015") == True
assert valid_date("04-29-2018") == True
assert valid_date("04-29-2016") == True
assert valid_date("01-0-2013") == False
assert valid_date("32-01-2001") == False
assert valid_date("30-02-2001") == False
assert valid_date("29-02-2010") == False
assert valid_date("00-01-1990") == False
assert valid_date("31-30-1990") == False
assert valid_date("16-11-1234") == False
assert valid_date("16.11.1990") == False
assert valid_date("29-02-2000") == False
assert valid_date("1-5-2019") == True
assert valid_date("1-32-2019") == False
assert not valid_date('2011-01-35')
assert not valid_date('2011-13-01')
assert not valid_date('2011/01/01')
assert not valid_date('2011-01-01')
assert not valid_date('2011-04-31')
assert valid_date("14-30-2000") == False
assert valid_date("01-01-2020") == True
assert valid_date("01-12-2011") == True
assert valid_date("01-01-1970") == True
assert valid_date("12-25-2020") == True
assert valid_date("12-32-2015") == False
assert valid_date("1-32-2015") == False
assert valid_date("13-32-2015") == False
assert valid_date("14-30-2015") == False
assert valid_date("00-31-2015") == False
assert valid_date("11-32-2015") == False
assert valid_date("01-01-2015") == True
assert valid_date("02-01-2015") == True
assert valid_date("04-01-2015") == True
assert valid_date("05-01-2015") == True
assert valid_date("06-01-2015") == True
assert valid_date("8-2") == False
assert valid_date("8-01-2017") == True
assert valid_date("23-08-2017") == False
assert valid_date("13-08-2017") == False
assert valid_date("-08-23-2017") == False
assert valid_date("01-99-2010") == False
assert valid_date("01-30") == False
assert valid_date("0130-2010") == False
assert valid_date("31-13-2017") == False
assert valid_date("hello") == False
assert valid_date("01-12-2017") == True
assert valid_date("04-25-2017") == True
assert valid_date("12-20-2017") == True
assert valid_date("01-12-2018") == True
assert valid_date("01-12-2021") == True
assert valid_date("01-12-2022") == True
assert valid_date("01-02-2014") == True
assert valid_date("06-34-2020") == False
assert valid_date("13-31-2020") == False
assert valid_date("05-34-2020") == False
assert valid_date("05/32/2020") == False
assert valid_date("05/34/2020") == False
assert valid_date("01-02-1999") == True
assert valid_date("13-03-1999") == False
assert valid_date("99-01-1999") == False
assert valid_date("1-99-1999") == False
assert valid_date("00-00-1999") == False
assert valid_date("1-1-9999") == True
assert valid_date("02-15-2000") == True
assert valid_date("04-15-2000") == True
assert valid_date("05-15-2000") == True
assert valid_date("06-15-2000") == True
assert valid_date("07-15-2000") == True
assert valid_date("08-15-2000") == True
assert valid_date("09-15-2000") == True
assert valid_date("10-15-2000") == True
assert valid_date("11-15-2000") == True
assert valid_date("12-15-2000") == True
assert valid_date("13-31-2000") == False
assert valid_date("13-15-2000") == False
assert valid_date("03-32-2020") == False
assert valid_date("13-19-2020") == False
assert valid_date("01-53-2010") == False
assert valid_date("01-1-2010") == True
assert valid_date("11-32-2010") == False
assert valid_date("11-1-2010") == True
assert valid_date("02-29-2400") == True
assert valid_date("31-04-2009") == False
assert valid_date("32-04-2009") == False
assert valid_date("04-00-2009") == False
assert valid_date("2-28-1999") == True
assert valid_date("04-20-2020") == True
assert valid_date("13-31-2021") == False
assert valid_date("00-31-2021") == False
assert valid_date("00-00-2021") == False
assert valid_date("2-5-2021") == True
assert valid_date("2-50-2021") == False
assert valid_date("00-30-2000") == False
assert valid_date("13-30-2000") == False
assert valid_date("03-40-2000") == False
assert valid_date("12-45-2019") == False
assert valid_date("2-15-2019") == True
assert valid_date("12-15-2019") == True
assert valid_date("11-15-2019") == True
assert valid_date("13-15-2019") == False
assert valid_date("01-25-2013") == True
assert valid_date("01-01-2010") == True
assert valid_date("31-02-2001") == False
assert valid_date("33-09-2001") == False
assert valid_date("1-10-2010") == True
assert valid_date("10-1-2010") == True
assert valid_date("10/10/2010") == False
assert valid_date("10/10/10") == False
assert valid_date("10-10-2013") == True
assert valid_date("10-10-2090") == True
assert valid_date("10-10-2012") == True
assert valid_date("12-10-2010") == True
assert valid_date("11-10-2010") == True
assert valid_date("10-11-2010") == True
assert valid_date("10-12-2010") == True
assert valid_date("31-15-2019") == False
assert valid_date("2017-02-29") == False
assert valid_date("31-02-2019") == False
assert valid_date("30-02-2019") == False
assert valid_date("17-13-2019") == False
assert valid_date("17-00-2019") == False
