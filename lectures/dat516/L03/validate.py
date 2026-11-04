import re

def is_date_valid(date):
    """
    Does the provided string represent a date in format YYYY-MM-DD?
    """

    # using regular string processing
    # return (
    #     len(date) == 10 and
    #     date[0:4].isdigit() and
    #     date[5:7].isdigit() and
    #     date[8:10].isdigit()
    # )

    # using a simple regular expression
    # return re.fullmatch(r'\d\d\d\d-\d\d-\d\d', date)

    # using a more complex regular expression
    # this tries to prevent invalid dates, such as 0000-67-42
    return re.fullmatch(r'(1|2)[0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|(1|2)[0-9]|30|31)', date)

# test code
assert is_date_valid('2026-11-03')
assert is_date_valid('2999-01-31')
assert not is_date_valid('2999-13-00')
assert not is_date_valid('0000-67-99')
assert not is_date_valid('03/11/26')
