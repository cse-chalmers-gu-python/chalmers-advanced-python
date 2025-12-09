import re
import sys

# python3 regexample.py ../../lecture-notes/python-guide.md


url = re.compile(r"http[s]?://[\S]+")
dig = re.compile(r"\d+")
dig4 = re.compile(r"\d{4}")
year = re.compile(r"[1][9][0-9][0-9]|[2][0][0-2][0-9]")
fun = re.compile(r"^[ ]*def .+")

ex = url

# print(ex)

with open(sys.argv[1]) as file:
    nr = 0
    for line in file:
        nr += 1
        if matches := ex.findall(line):
            print(nr, ':', matches)

 
# (?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))

# https://gist.github.com/gruber/249502

