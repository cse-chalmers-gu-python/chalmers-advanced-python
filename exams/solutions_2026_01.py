# 1

# 1.1
[4,5,6].append(7)
# type: `NoneType`
# value: `None`

# 1.2
{ m: max(2, m) for m in range(1,4) }
# type: `dict`
# value: `{1: 2, 2: 2, 3: 3}`

# 1.3
set("hello")
# type: `set`
# value: `{'e', 'h', 'l', 'o'}` (order not important)

# 1.4
(lambda x: x.x())(True)
# AttributeError
# 'bool' object has no attribute 'x'

# 1.5
set() == []
# type: `bool`
# value: `False`

# 1.6
{1,2} is {2,1}
# type: `bool`
# value: `False`

# 1.7
len({'cat','dog'}.add('fish'))
# TypeError
# object of type 'NoneType' has no len()

# 1.8
[c for c in "hello" if c != 'l'][3]
# IndexError
# list index out of range

"""
Grading guide (2p each)
- 1p for type / error
- 1p for value / explanation
"""

# ---

# 2

tramnetwork = {
  "stops": {
    "Östra Sjukhuset": {
      "lat": 57.7224618,
      "lon": 12.0478166
    },
  },

  "lines": {
    "1": [
      "Östra Sjukhuset",
      "Tingvallsvägen",
    ],
  },

  "times": {
    "Östra Sjukhuset": {},
    "Tingvallsvägen": {
      "Östra Sjukhuset": 1
    },
  }
}

# 2.1

longest_line_1 =  max(tramnetwork["lines"], key=lambda l: len(tramnetwork["lines"][l]))
# iterating over a dict gives its keys

longest_line_2 = max([ line for line in tramnetwork["lines"] ], key=lambda l: len(tramnetwork["lines"][l]))


"""
Grading guide (6p)
- Must be an expression
- Value should be a single string
"""

# 2.2

terminals = {
  stop for stops in tramnetwork["lines"].values()
        for stop in [stops[0], stops[-1]]
}

"""
Grading guide (6p)
- Must be an expression
- Value should be a set of strings
- Tuples of (start,end) stops is a possible interpretation, accepted
"""

# ---

# 3

class Lst():
    def __init__(self):
        self.item = None
        self.next = None

    def append(self, x):
        if not self.item:
            self.item = x
        else:
            if not self.next:
                self.next = Lst()
            self.next.append(x)

# 3.1

l = Lst()
l.append(42)
l.append("foo")
l.append(True)

"""
Grading guide (3p)
...
"""

# 3.2

"""
>>> Lst().append(4).append(4)
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    Lst().append(4).append(4)
    ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'append'
"""

# Fix:
def append(self):
    ...
    return self

"""
Grading guide (3p)
- Must indicate that it will give an error
- Not necessary to explain error correctly
"""

# 3.3

def items(self):
    if not self.item:
        return []
    if self.next:
      return [self.item] + self.next.items()
    else:
      return [self.item]

"""
Grading guide (6p)
- Returning a list is ok
- Implementation as generator (using yield) also ok
"""

# 3.4

def __len__(self):
    if not self.item:
        return 0
    elif not self.next:
        return 1
    else:
        return 1 + len(self.next)

"""
Grading guide (4p)
- Must implement `__len__(self)`
- Ok to reuse items() from 3.3
"""

# ---

# 4

# An HTTP header
class Header:
  key: str
  value: str

# An HTTP response
class Response:

  # status code as a number
  status: int
  
  # text explanation of status code
  status_message: str
  
  # a list of Header objects
  headers: list[Header]
  
  # response payload as a raw string (or None)
  body: str | None
  
  # parse payload as JSON and return dict (or raise JSONDecodeError)
  def json(self) -> dict: ...

# An HTTP request
class Request:

  # URL to send request to
  url: str
  
  # HTTP method as string
  method: str
  
  # a list of Header objects
  headers: list[Header]
  
  # request payload as raw string (or None)
  body: str | None
  
  # send request and return Response object
  def send(self) -> Response: ...

# Construct and return a Request object without sending it
# headers is a dictionary of strings or None (default None)
# body is a string or None (default None)
def make_request(
  url: str,
  method: str,
  headers: dict[str, str] | None = None,
  body: str | None = None
) -> Request: ...

# Send a request, returning a Response object
# headers is a dictionary of strings or None (default None)
# body is a string or None (default None)
def send_request(
  url: str,
  method: str,
  headers: dict[str, str] | None = None,
  body: str | None = None
) -> Response: ...

# Add a header to a Request object (update in-place, return None)
def add_header(
  req: Request,
  key: str,
  value: str,
) -> None: ...

# Get header value corresponding to key in a Request or Response object (or None)
def get_header(
  r: Request | Response,
  key: str
) -> str | None: ...

# 4.1

resp = send_request('http://www.example.com/tasks', 'GET', {'TaskId': '123'})
ok = resp.status == 200

"""
Grading guide (4p)
- Header should be in a dict
- Value in dict should be a string
- `status` attribute in response is an int
- `body` doesn't need to be mentioned
"""

# 4.2

import json
obj = resp.json()
obj['status'] = 'done'
req = make_request('http://www.example.com/tasks', 'POST', body=json.dumps(obj))

"""
Grading guide (4p)
- Hardcoding the body is ok
- If parsing JSON:
  - Must use either using `.json()` or `json.loads()`
  - using `str()` does not produce JSON (single quotes); must use `json.dumps()`
- `body` must be a string
- `body` argument must be named if `headers` is omitted
- Must call `make_request`
"""

# 4.3

add_header(req, 'Cache', 'False')
resp = req.send()
if v := get_header(resp, 'CacheStatus'):
  print(v)

"""
Grading guide (4p)
- `add_header` updates in place, without return
- Value in header must be a string
- Not important what exactly is printed (can be header value, header, or entire response)
"""

# 4.4

def bulk_get(url: str, n: int) -> list[Response]:
  return [ send_request(url, 'GET', {'RequestNum': str(i+1)}) for i in range(n) ]

"""
Grading guide (4p)
- Value in header must be a string
- Must return a list of `Response` objects, or yield them
- Ok if numbering is 0..n-1 instead of 1..n
"""
