
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
assert valid_date("01-01-2022") == True
assert valid_date("02-29-2020") == True
assert valid_date("13-01-2022") == False
assert valid_date('13-01-2022') == False
assert valid_date("01-01-2020") == True
assert valid_date("13-01-2020") == False
assert valid_date("01-00-2022") == False
assert valid_date('02-29-2020') == True, 'Test Case 4 Failed'
assert valid_date('02-28-2021') == True, 'Test Case 5 Failed'
assert valid_date('00-01-2020') == False, 'Test Case 6 Failed'
assert valid_date('13-01-2020') == False, 'Test Case 7 Failed'
assert valid_date('01-32-2020') == False, 'Test Case 8 Failed'
assert valid_date('01-01-2020-') == False, 'Test Case 15 Failed'
assert valid_date('01-01-2020-01') == False, 'Test Case 16 Failed'
assert valid_date('01-01-2020-01-01') == False, 'Test Case 17 Failed'
assert valid_date('01-01-2020-01-01-01') == False, 'Test Case 18 Failed'
assert valid_date('01-01-2020-01-01-01-01') == False, 'Test Case 19 Failed'
assert valid_date("") == False
assert valid_date("00-01-2022") == False
assert valid_date("01-01-2023") == True
assert valid_date("02-28-2021") == True
assert valid_date("13-01-2021") == False
assert valid_date("12-32-2022") == False
assert valid_date("13-01-2022") == False, "Test case 3 failed"
assert valid_date("") == False, "Test case 5 failed"
assert valid_date("13-12-2022") == False
assert valid_date("12-12-2022") == True
assert valid_date('02-29-2020') == True
assert valid_date('13-01-2020') == False
assert valid_date("1-1-2020") == True
assert valid_date('00-01-2021') == False
assert valid_date('13-01-2021') == False
assert valid_date('01-00-2021') == False
assert valid_date('01-32-2021') == False
assert valid_date('01-01-2022') == True
assert valid_date("12-01-2022") == True
assert valid_date("02-28-2022") == True
assert valid_date("01-32-2022") == False
assert valid_date("00-01-2020") == False
assert valid_date('00-01-2022') == False
assert valid_date('01-00-2022') == False
assert valid_date('01-32-2022') == False
assert valid_date("02-29-2024") == True
assert valid_date("01-01-9999") == True
assert valid_date("02-28-2024") == True
assert valid_date("06-15-2022") == True
assert valid_date("12-32-2020") == False
assert valid_date("12-01-1000") == True
assert valid_date('13-01-2000') == False
assert valid_date('01-32-2000') == False
assert valid_date('00-01-2000') == False
assert valid_date('') == False
assert valid_date("13-31-2022") == False
assert valid_date("12-25-2022") == True
assert valid_date('12-00-2022') == False
assert valid_date('12-32-2022') == False
assert valid_date("00-01-2022") == False, "Test case 4 failed"
assert valid_date("01-00-2022") == False, "Test case 5 failed"
assert valid_date("") == False, "Test case 7 failed"
assert valid_date("01-01-2021") == True
assert valid_date("01-00-2020") == False
assert valid_date('02-29-2024') == True
assert valid_date('01-01-2022-') == False
assert valid_date('01/01/2022') == False
assert valid_date("13-12-2020") == False
assert valid_date("01-32-2020") == False
assert valid_date("06-15-2020") == True
assert valid_date('02-28-2022') == True
assert valid_date('01-01-2022-01') == False
assert valid_date('01-01-2022-01-01') == False
assert valid_date('01-01-2022-01-01-01') == False
assert valid_date('01-01-2022-01-01-01-01') == False
