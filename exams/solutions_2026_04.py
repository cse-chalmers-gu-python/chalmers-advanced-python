# Q1

{4,5,6}.add(5)
# None
# NoneType

{n%3 for n in range(1, 10, 3)}
# {1}
# set

# set([[1, 2, 2, 1]])
# TypeError
# unhashable type list (mutable also accepted, and "set cannot contain a list")

(lambda x, y: y(x, x+1))(2, max)
# 3
# int

set([1, 2, 2, 1])
# {1, 2} (duplications in set also accepted, because they are valid set expressions)
# set

'a cat' is 'a cat'
# True
# bool

# {m: m%3 in range(1,4)}
# NameError  (syntax error with missing for also accepted)
# m is not defined

len({print(n) for n in range(1, 100) if 10 < n < 20})
# 1
# int


# Q2

sweng = {
    'farmor': ['grandmother', 'granny'],
    'mormor': ['grandmother', 'granny'],
    'mor': ['mother', 'mum'],
    'mamma': ['mother', 'mum'],
    'bror': ['brother'],
    'broder': ['brother'],
}

# 2.1
engsw = {
  en: [sv for sv, ens2 in sweng.items() if en in ens2]
      for ens in sweng.values() for en in ens
      }

# 3p if ens is used as the key and last 'for' is omitted: this is the main point of the question

engswe_alternative = {
  eng: [swe for swe in sweng if eng in sweng[swe]]
       for englist in sweng.values() for eng in englist
      }

print(engsw)

# 2.2

# the number of distinct English words
eng_words: int = len({ en for ens in sweng.values() for en in ens })
print(eng_words)

# the average length of Swedish words
swe_length: float = sum([len(sv) for sv in sweng.keys()]) / len(sweng)
print(swe_length)

# the number of Swedish words that have the same word as one of its translations
same_words: int = len([sv for sv, ens in sweng.items() if sv in ens])
print(same_words)

same_words_alternative: int = len({sv for sv, ens in sweng.items() for en in ens if sv==en})
print(same_words_alternative)


# Q3

class Date:
    def __init__(self, month, day):
        self._month = month
        self._day = day
        
    def __str__(self):
        return f'{self._day}/{self._month}'
         
    def __lt__(self, other):
        return (self._month, self._day) < (other._month, other._day)

# 3.1

date1 = Date(4, 20)
date2 = Date(10, 14)

print(date1, '<', date2, date1 < date2)

# 20/4 < 14/10 True

# 3.2

class Time:
  def __init__(self, hour, minute):
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
      raise ValueError
    self._hour = hour
    self._minute = minute

  def __str__(self):
    return f'{self._hour}:{self._minute}'
  
  def __lt__(self, other):
    return (self._hour, self._minute) < (other._hour, other._minute)

# 3.3

class DateTime(Date, Time):
    def __init__(self, month, day, hour, minute):
        Date.__init__(self, month, day)
        Time.__init__(self, hour, minute)
    
    def date(self):
        return Date(self._month, self._day)
    
    def time(self):
        return Time(self._hour, self._minute)

    def __str__(self):
        return f'{self.date()} at {self.time()}'

    def __lt__(self, other):
        return (self.date(), self.time()) < (other.date(), other.time())

datetime1 = DateTime(4, 20, 22, 35)
datetime2 = DateTime(10, 14, 13, 45)
print(datetime1, '<', datetime2, datetime1 < datetime2)
# 20/4 at 22:35 < 14/10 at 13:45 True

# ---

# Q4

from typing import Iterator

class Elem:
    tag: str
    attrs: dict[str, str]
    elems: list["Elem | str"]

    def __init__(
        self,
        tag: str,
        attrs: dict[str, str] = {},
        elems: list["Elem | str"] = []
    ):
        self.tag = tag
        self.attrs = attrs
        self.elems = elems

    def __str__(self) -> str:
        attrs_str = " " + " ".join([ f"{k}=\"{v}\"" for k,v in self.attrs.items() ]) if self.attrs else ""
        elems_str = "".join([ str(e) for e in self.elems ])
        return f"<{self.tag}{attrs_str}>{elems_str}</{self.tag}>"

    def __eq__(self, other) -> bool:
        return self.tag == other.tag and self.attrs == other.attrs and self.elems == other.elems

    def add_item(self, elem: "Elem") -> None:
        self.elems.append(elem)

class Document:
    prolog: str | None
    root: Elem

    def __str__(self) -> str:
        return (self.prolog + "\n" if self.prolog else "") + str(self.root)

    def __eq__(self, other) -> bool:
        return self.prolog == other.prolog and self.root == other.root

    def iter_tag(self, tagname: str) -> Iterator[Elem]:
        def r(node: Elem):
            if node.tag == tagname:
                yield node
            for elem in node.elems:
                if type(elem) == Elem:
                    yield from r(elem)
        yield from r(self.root)

    def iter_attr(self, key: str, value: str) -> Iterator[Elem]:
        def r(node: Elem):
            if node.attrs.get(key) == value:
                yield node
            for elem in node.elems:
                if type(elem) == Elem:
                    yield from r(elem)
        yield from r(self.root)

    def iter_text(self) -> Iterator[str]:
        def r(node: Elem):
            for elem in node.elems:
                if type(elem) == Elem:
                    yield from r(elem)
                elif type(elem) == str:
                    yield elem
        yield from r(self.root)

class ParseError(Exception):
    ...

# Read file contents and parse as HTML
# Throws IOError if file cannot be read
# Throws ParseError if contents cannot be parsed as HTML
def parse_file(filepath: str) -> Document: ...

# Parse string as HTML
# Throws ParseError if string cannot be parsed as HTML
def parse_string(raw: str) -> Elem: ...

# ---

# 4.1

doc_str = """\
<!DOCTYPE html>
<html lang="en">
    <body>
        <p>This text is <strong>bold</strong></p>
        <p role="footer">Here is more text</p>
    </body>
</html>
"""

doc = Document()
doc.prolog = "<!DOCTYPE html>"
doc.root = Elem(
    "html",
    {"lang": "en"},
    [
        Elem("body", elems=[
            Elem("p", elems=[
                "This text is ",
                Elem("strong", elems=["bold"]),
            ]),
            Elem("p", {"role": "footer"}, ["Here is more text"]),
        ]),
    ]
)

print(doc)

# Alterntatively, assuming `doc.html` contains the HTML above:
# doc = parse_file("doc.html")

"""
Grading guide (4p)

- Correct type/use of class 1
- Prolog included 1
- Attributes included 1
- Tags & content included 1

OK to assume file and use parse_file(), if stated and used correctly.
"""

# 4.2

def count_paras(doc):
    return len(list(doc.iter_tag("p")))

print(count_paras(doc))

"""
Grading guide (4p)

- Function (not method) 1
- Uses iter_tag() 1
- Loops or converts to list (iterator has no len()) 1
- Returns correct value 1
"""

# 4.3

# (implementation above)

print(doc)

"""
Grading guide (6p)

- Implement one method per class 1
- Document.__str__ 2
    - calls str() on root elem 1
    - handles prolog 1
- Elem.__str__ 3
    - handles attributes 1
    - handles tag (including closing) 1
    - calls str() on subelements 1

Assuming iter_text() gives rendered HTML is OK, if used correctly.
"""

# 4.4

# dummy re-implementation, not part of solution
def parse_string(raw: str) -> Elem: return doc.root

def test(elem: Elem) -> None:
    s = str(doc.root)
    elem2 = parse_string(s)
    assert elem2 == elem

test(doc.root)

"""
Grading guide (2p)

- Calls str() and parse_string() 1
- Assertion 1

Ok to start from string and check opposite direction.
Any attempt at an assertion is OK, no particular syntax or library expected.
"""
