
verse = "South of the river, you stop n' you hold everything.\
A band is blowing Dixie, double-four time. \
You feel all right when you hear that music ring."

"""
Which comprehension below produces the list:
["South", "Dixie", "You"]
"""

a = [ word for word in verse.split(' ') if word[0].isupper() ]
b = [ word for word in verse.split() if word.isupper() ]
c = [ word.isupper() for word in verse.split(' ') ]
d = [ word for word in verse if word.split().isupper() ]
