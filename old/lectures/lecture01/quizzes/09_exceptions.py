def convert(s):
    try:
        return int(s)
    except ValueError:
        return "value error"
    except Exception:
        return "generic error"

print(convert("not a number"))

"""
What is the output of this program?

A. "not a number"
B. "value error"
C. "generic error"
D. Error: ambiguous exception handling
"""
