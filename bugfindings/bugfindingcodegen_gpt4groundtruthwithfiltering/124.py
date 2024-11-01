
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
assert 	valid_date('-1-12-2012') == False
assert 	valid_date('12-15-2012') == True
assert 	valid_date('12-15-2038') == True
assert valid_date('') == False
assert valid_date('-') == False
assert valid_date('01') == False
assert valid_date('02') == False
assert valid_date('01-02-2020') == True
assert valid_date('02-01-2020') == True
assert valid_date('1-01-2020') == True
assert valid_date('13-01-2020') == False
assert valid_date('13-01-20') == False
assert valid_date('13-01-2021') == False
assert 	valid_date("12-1-2012") == True
assert 	valid_date('12-28-2019') == True
assert 	valid_date('02-28-2019') == True
assert 	valid_date("13-31-2016") == False
assert 	valid_date("12-21-2016") == True
assert 	valid_date("12-18-2016") == True
assert 	valid_date("2-29-2003") == True
assert 	valid_date("12-01-2004") == True
assert 	valid_date("12-02-2004") == True
assert 	valid_date("12-01-2005") == True
assert 	valid_date("12-32-2004") == False
assert 	valid_date("2-02-2005") == True
