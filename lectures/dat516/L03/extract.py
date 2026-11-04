import re

date_regex = re.compile(r"(1|2)[0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|(1|2)[0-9]|30|31)")

def extract_dates(text):
    return date_regex.finditer(text)

text = """
The academic year 2026/2027
Sign-up for re-sit examination days in August are from Monday 2026-07-06 to Sunday 2026-08-02. \
The re-sit examinations are from Monday 2025-08-17 to Saturday 2026-08-29.
"""

for date in extract_dates(text):
    print(date[0])
