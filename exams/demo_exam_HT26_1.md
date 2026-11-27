# Demo exam HT26-1

## Instructions

Write your answers in Inspera. You can of course use separate sheets of paper to draft and experiment, but only the answers in Inspera will be graded. Your answers can and should be short.

Python interpreters such as Self Practice are not available. Hence you have to reason about the answers on your own.
Using pencil and paper is a good aid for this.

You are allowed to have with you one A4 paper, hand-written on both sides, with whatever information you want.

The exam has a total of 60 points. You will need at least:

- 24 points to pass with grade 3
- 36 points for grade 4
- 48 points for grade 5

The exam grade will also be the final grade for the course.

## Q1: Information extraction and storage (20p)

> Tests the ability to reason about complex expressions and their types, the use of comprehensions,
> data structures for information storage, and regular expressions.
>
> Format: 20 one-point multiple-choice questions (no negative marking).

Consider the `nobel_data` data structure below, where each dictionary in the list stores the record for one Nobel laureate.
This data will be used for several questions in this section.

```python
nobel_data = [
    {
        "name": "Charles K. Kao",
        "sex": "male",
        "award": "Nobel Prize in Physics",
        "date": "2009-01-01",
        "country": "People's Republic of China"
    },
    ...
]
```

### 1.1

We want to obtain the names of all countries which have Nobel laureates, without duplicates. Which of the following comprehensions will do this?

a. `( record['country'] for record in nobel_data )`  
b. `[ record['country'] for record in nobel_data ]`  
c. `{ record['country'] for record in nobel_data }`  
d. `{ record for record in nobel_data['country'] }`  

<details markdown="1">
<summary>Solution</summary>

c. `{ record['country'] for record in nobel_data }`

</details>

### 1.2

We want to count how many awards go to each country. Which of the following comprehensions will create a dictionary where keys are country names and values are count of awards?

```python
# a.
country_count = [
    (record['country'], nobel_data.count(record))
    for record in nobel_data
]

# b.
countries = [record['country'] for record in nobel_data]
country_count = {
    country: countries.count(country)
    for country in set(countries)
}

# c.
countries = [record['country'] for record in nobel_data]
country_count = {
    country: len(country)
    for country in countries
}

# d.
country_count = {
    record['country']: len(nobel_data)
    for record in nobel_data
}
```

<details markdown="1">
<summary>Solution</summary>

```python
# b.
countries = [record['country'] for record in nobel_data]
country_count = {country: countries.count(country) for country in set(countries)}
```

</details>

### 1.3

We want to validate that all awards dates in `nobel_data` are correct. Our criteria is: year can be from 1900-2026, month can be from 01-12, and day can be from 01-31. Which of the following regular expressions correctly matches such dates?

a. `r"^19[0-9]{2}|20[0-9]{2}$-^0[1-9]|1[0-2]$-^0[1-9]|[1-2][0-9]|30|31$"`  
b. `r"(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|30|31)"`  
c. `r"^19[0-9]{2}|20[0-9][0-6]$-^0[1-9]|1[0-2]$-^0[1-9]|[1-2][0-9]|30|31$"`  
d. `r"(19[0-9]{2}|20([0-1][0-9]|2[0-6]))-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|30|31)"`  

<details markdown="1">
<summary>Solution</summary>

d. `r"(19[0-9]{2}|20([0-1][0-9]|2[0-6]))-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|30|31)"`  

</details>

### 1.4

Assuming all dates are valid, we want to filter only the dates where the month is either February or December.
Which of the following regular expressions should we partially match on?

a. `r'\d{4}-(02|12)-'`  
b. `r'\d{4}-[02|12]{2}-'`  
c. `r'\d{4}-02|12-'`  
d. `r'\d{4}-[01]{2}-'`  

<details markdown="1">
<summary>Solution</summary>

a. `r'\d{4}-(02|12)-'`  

</details>

### 1.5

What is the type of the value of this expression?

```python
{ record['award'].split()[-1] for record in nobel_data }
```

a. `list`  
b. `dict`  
c. `set`  
d. an error will be raised  

<details markdown="1">
<summary>Solution</summary>

c. `set`

</details>

### 1.6

What is the value of `result`?

```python
result = { 0 if x % 2 else x for x in range(6) }
```

a. `{0, 0, 2, 0, 4, 0}`  
b. `[0, 2, 4]`  
c. `{0, 2, 4}`  
d. `[0, 1, 2, 3, 4, 5]`  

<details markdown="1">
<summary>Solution</summary>

c. `{0, 2, 4}`

</details>

### 1.7

What is the value of `pairs`?

```python
pairs = [(x, y) for x in range(2) for y in range(x, 2)]
```

a. `[(0, 0), (0, 1), (1, 1)]`  
b. `[(0, 0), (1, 0), (1, 1)]`  
c. `[(0, 1), (1, 2)]`  
d. `[(0, 0), (0, 1), (1, 0), (1, 1)]`  

<details markdown="1">
<summary>Solution</summary>

a. `[(0, 0), (0, 1), (1, 1)]`

</details>

### 1.8

What is printed to the console?

```python
items = ["a", "b"]
other = items
other.append("c")
print(items)
```

a. `["a", "b"]`  
b. `["c"]`  
c. `["a", "b", "c"]`  
d. an error will be raised  

<details markdown="1">
<summary>Solution</summary>

c. `["a", "b", "c"]`

</details>

### 1.9

What is the value of `result`?

```python
data = {"a": 1, "b": 2}
result = data.get("c", 0) + data["a"]
```

a. `0`  
b. `1`  
c. `2`  
d. `KeyError`  

<details markdown="1">
<summary>Solution</summary>

b. `1`

</details>

### 1.10

We have a matrix with integers, with type `list[list[int]]`.
We want to find the sum of all its entries.
Which expression performs this sum correctly?

a. `sum([item for row in matrix for item in row])`  
b. `sum({item for row in matrix for item in row})`  
c. `sum[item for row in matrix for item in row]`  

<details markdown="1">
<summary>Solution</summary>

a. `sum([item for row in matrix for item in row])`  

</details>

### 1.11

In context of `nobel_data`, we have built the following expression to collect names of all Swedish people who have ever won Nobel award (28 people total).  

```python
swedish = [record['name'] for record in nobel_data if record['country'] == 'Sweden']`
```

What is the correct type annotation for `swedish`?

a. `list[str]`  
b. `list[list[str]]`  
c. `list[bool]`  
d. error  

<details markdown="1">
<summary>Solution</summary>

a. `list[str]`  

</details>

### 1.12

What is printed by following code?

```python
import re
print(re.findall(r"\s+", "Nobel Prize in Physics"))
```

a. `["1", "2", "3"]`  
b. `[' ', ' ', ' ']`  
c. `["Nobel Prize in Physics"]`  
d. `["Nobel", "Prize", "in", "Physics"]`  

<details markdown="1">
<summary>Solution</summary>

b. `[' ', ' ', ' ']`

</details>

### 1.13

What is the value of `groups`?

```python
import re
match = re.search(r"([A-Z]+)-(\d+)", "ID-204")
groups = match.groups()
```

a. `("ID", "204")`  
b. `["ID", "204"]`  
c. `("ID-204",)`  
d. `None`  

<details markdown="1">
<summary>Solution</summary>

a. `("ID", "204")`

</details>

### 1.14

What is printed to the console?

```python
print(re.search(r"([A-Za-z]+)\s(\S+)\s(\w+)\s(\D+)", "Nobel Prize in Physics").groups())
```

a. an error  
b. `('Nobel', 'Prize', 'Physics')`  
c. `('Nobel', 'Prize', 'in', 'Physics')`  
d. `None`

<details markdown="1">
<summary>Solution</summary>

c. `('Nobel', 'Prize', 'in', 'Physics')`

</details>

### 1.15

What is printed to the console?

```python
data = {"x": [1, 2, 3], "y": [3, 4, 6, 8]}
len_count = { key: len(values) for key, values in data.values() }
print(len_count)
```

a. `{'x': 3, 'y': 4}`  
b. `{'x': 6, 'y': 21}`  
c. an error  
d. `{}`

<details markdown="1">
<summary>Solution</summary>

c. an error

</details>

For questions 16-20, we use a shortened example of the previous data `nobel_data`, called `mini_data`:

```python
mini_data = [
    {"name": "Anna", "sex": "female", "award": "Physics", "date": "2020-01-01", "country": "Sweden"},
    {"name": "Bertil", "sex": "male", "award": "Chemistry", "date": "2021-01-01", "country": "Sweden"},
    {"name": "Carl", "sex": "male", "award": "Physics", "date": "2020-01-01", "country": "Norway"},
    {"name": "Dina", "sex": "female", "award": "Physics", "date": "2021-01-01", "country": "Sweden"},
]
```

### 1.16

What is the value of `awards`?

```python
awards = {
    country: {record['award'] for record in mini_data if record['country'] == country}
    for country in {record['country'] for record in mini_data}
}
```

a. `{'Sweden': {'Physics', 'Chemistry'}, 'Norway': {'Physics'}}`  
b. `{'Sweden': {'Physics'}, 'Norway': {'Physics', 'Chemistry'}}`  
c. `{'Sweden': ['Physics', 'Chemistry', 'Physics'], 'Norway': ['Physics']}`  
d. `{'Physics': {'Sweden', 'Norway'}, 'Chemistry': {'Sweden'}}`

<details markdown="1">
<summary>Solution</summary>

a. `{'Sweden': {'Physics', 'Chemistry'}, 'Norway': {'Physics'}}`

</details>

### 1.17

What is the value of `counts`?

```python
counts = {
    year: len({record['country'] for record in mini_data if record['date'][:4] == year})
    for year in {record['date'][:4] for record in mini_data}
}
```

a. `{'Sweden': 2, 'Norway': 1}`  
b. `{'2020': 2, '2021': 1}`  
c. `{'2020': 1, '2021': 2}`  
d. `{'Sweden', 'Norway'}`

<details markdown="1">
<summary>Solution</summary>

b. `{'2020': 2, '2021': 1}`

</details>

### 1.18

What is printed to the console?

```python
n_data = [n for n in mini_data]
print((n_data is mini_data), (n_data[0] is mini_data[0]))
```

a. `True True`  
b. `False True`  
c. `True False`  
d. `False False`

<details markdown="1">
<summary>Solution</summary>

b. `False True`

</details>

### 1.19

What is printed to the console?

```python
print({record['country']: record['name'] for record in mini_data})
```

a. `{'Sweden': 'Anna', 'Norway': 'Carl'}`  
b. `{'Sweden': ['Anna', 'Bertil', 'Dina'], 'Norway': ['Carl']}`  
c. `{'Sweden': 'Bertil', 'Norway': 'Carl'}`  
d. `{'Sweden': 'Dina', 'Norway': 'Carl'}`  

<details markdown="1">
<summary>Solution</summary>

d. `{'Sweden': 'Dina', 'Norway': 'Carl'}`

</details>

### 1.20

What is the value of `pairs`?

```python
pairs = [
    (female['name'], male['name'])
    for female in mini_data if female['sex'] == 'female'
    for male in mini_data if male['sex'] == 'male'
]
```

a. `[('Anna', 'Carl'), ('Dina', 'Bertil')]`  
b. `[('Anna', 'Bertil'), ('Dina', 'Carl')]`  
c. `[('Anna', 'Carl'), ('Bertil', 'Dina')]`  
d. `[('Anna', 'Bertil'), ('Anna', 'Carl'), ('Dina', 'Bertil'), ('Dina', 'Carl')]`

<details markdown="1">
<summary>Solution</summary>

d. `[('Anna', 'Bertil'), ('Anna', 'Carl'), ('Dina', 'Bertil'), ('Dina', 'Carl')]`

</details>

## Q2: Object-oriented design and testing (20p)

> Tests the understanding of object-oriented design in the context of complex data structures such as graphs.
> Also tests the ability to reason about buggy code and apply testing techniques.
>
> Format: 5 four-point questions.

Here is the implementation of a graph as Python class, using an adjacency dictionary as its internal datatype.
Watch out! The code is incomplete and/or buggy.

```python
class Graph:
    """an undirected graph"""

    def __init__(self):
        self.adjdict = {}

    def add_edge(self, a, b):
        """add b as neighbour of a and a as neighbour of b"""
        self.adjdict[a] = self.adjdict.get(a, set())
        self.adjdict[a].add(b)
        self.adjdict[b] = self.adjdict.get(b, set())
        self.adjdict[b].add(a)

    def get_edges(self):
        """return the set of edges, not including (a, b) if (b, a) is included"""
        edges = set()
        for a in self.adjdict:
            for b in self.adjdict[a]:
                edges.add((a, b))
```

### 2.1 (4p)

What is printed when running this code?

```python
G = Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 2)

print("adj:", G.adjdict)
print("edges:", G.get_edges())
```

<details markdown="1">
<summary>Solution</summary>

```python
adj: {1: {2}, 2: {1, 2, 3}, 3: {2}}
edges: None
```

</details>

### 2.2 (4p)

The current implementation of `get_edges()` is buggy.
First write what the method should return, given the previous example.
Then provide a fixed version of the method, which does what its docstring says it should.

<details markdown="1">
<summary>Solution</summary>

Correct return value: `{(2, 3), (1, 2), (2, 2)}`

```python
def get_edges(self):
    """return the set of edges, not including (a, b) if (b, a) is included"""
    edges = set()
    for a in self.adjdict:
        for b in self.adjdict[a]:
            if (b, a) not in edges:    ## line 1/2 to be added
                edges.add((a, b))
    return edges                       ## line 2/2 to be added
```

</details>

### 2.3 (4p)

Provide two simple tests for this class, ensuring that:

1. edges are not directed
2. the same edge cannot be added multiple times

<details markdown="1">
<summary>Solution</summary>

```python
# edges are not directed
G1 = Graph()
G1.add_edge("A", "B")
G2 = Graph()
G2.add_edge("B", "A")
assert G1.adjdict == G2.adjdict

# same edge cannot be added multiple times
G = Graph()
G.add_edge("A", "A")
G.add_edge("A", "A")
assert len(G.get_edges()) == 1
```

</details>

### 2.4 (4p)

Come up with a property-based test for this class which uses both the `add_edge()` and `get_edges()` methods.
The exact syntax is not important, but you must clearly describe your test data and state the property in an unambiguous way.
Does this property always hold for your fixed implementaion?

<details markdown="1">
<summary>Solution</summary>

```python
from hypothesis import given, strategies 

@given(strategies.characters(), strategies.characters())
def test_edges_not_directed(x, y):
    G = Graph()
    G.add_edge(x, y)
    G.add_edge(y, x)
    assert len(G.get_edges()) == 1

test_ignore_duplicate_edges()
```

Explanation: for any two vertices x and y, adding edge x-y and then edge y-x only results in one edge.  
This property holds for our fixed implementation.
</details>

### 2.5 (4p)

We now want to implement weighted graphs, by inheriting from the `Graph` class.
Provide a stub implementation of this new class, showing:

1. What additional instance variables are needed, and how they are initialised.
2. What additional methods are needed, with their signatures (implementations not required).
3. What methods from the superclass need to be overridden (if any).

<details markdown="1">
<summary>Solution</summary>

```python
class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()
        self.weightdict = {}
    def set_weight(self, a, b, w): ...
    def get_weight(self, a, b): ...
```

</details>

## Q3: Typing and APIs (20p)

> Tests the ability to understand and use type annotations and library APIs.
> A fake API for a real-world task is provided, which much be used in a type-correct way.
>
> Format: 5 four-point questions.

Below is the API for a (fictitious) Python library for making HTTP requests.
All answers in this section should make use of this API, respecting the documented types.
You cannot assume any methods or attributes not mentioned in the API.

### Type annotation syntax

| Expression         | Explanation                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| `x: T`             | Variable `x` has type `T`                                                      |
| `def f(x: T) -> U` | Function `f` takes a parameter `x` of type `T` and returns a value of type `U` |
| `T ❘ U`            | Either type `T` or type `U`                                                    |
| `list[T]`          | A list of items of type `T`                                                    |
| `dict[T, U]`       | A dictionary with keys of type `T` and values of type `U`                      |
| `tuple[T, U]`      | A tuple with first item of type `T` and second item of type `U`                |

### HTTP Library API

```python
class URL:
    """A URL object"""

    # initialise URL object from string
    def __init__(self, url: str)
    
    # a URL's scheme, e.g. 'http' or 'https'
    scheme: str
    
    # full domain name and path
    path: str
    
    # query string parameters as key/values
    params: dict[str, str]

class Request:
    """An HTTP request"""

    # URL to send request to
    url: URL
    
    # HTTP method, e.g. GET/POST/PATCH
    method: str
    
    # request headers as a list of tuples of strings
    headers: list[tuple[str, str]]
    
    # request payload as raw string (or None)
    body: str | None
    
    # send this Request and return a Response
    def send(self) -> Response

class Response:
    """An HTTP response"""

    # status code and text explanation, e.g. (404, "Not Found")
    status: tuple[int, str]
    
    # response headers as a list of tuples of strings
    headers: list[tuple[str, str]]
    
    # response payload as a raw string (or None)
    body: str | None

# Construct and return a Request object without sending it
def make_request(
    url: str | URL,
    method: str,
    headers: dict[str, str] | None = None,
    body: str | None = None
) -> Request

# Send an HTTP request, returning True if a response was received
def send_request(
    url: str | URL,
    method: str,
    headers: dict[str, str] | None,
    body: str | None
) -> bool

# Add a header to a Request object
def add_header(
    req: Request,
    key: str,
    value: str,
) -> None

# Get header corresponding to key in a Request or Response object
# Returns header as key/value pair, or None
def get_header(
    r: Request | Response,
    key: str
) -> tuple[str,str] | None
```

### 3.1 (4p)

Send a `GET` request to `https://example.com` with query string parameter `user=42`. Store the response in a variable named `resp` if its status code is 200. Otherwise, `resp` should be set to `None`.

<details markdown="1">
<summary>Solution</summary>

```python
url = URL('https://example.com')
url.params = {'user': '42'}
req = make_request(url, 'GET')
resp = req.send()
if resp.status[0] != 200: resp = None
```

</details>

### 3.2 (4p)

Check if your response from 3.1 contains a header with key `SessionID`. If so, store the corresponding header value in a variable named `sid`.

<details markdown="1">
<summary>Solution</summary>

```python
if h := get_header(resp, 'SessionID'):
  sid = h[1]
```

</details>

### 3.3 (4p)

Now send a `POST` request to `https://example.com/logout`. This request should have a header with key `SessionID` and value obtained from 3.2 above.

<details markdown="1">
<summary>Solution</summary>

```python
send_request('https://example.com/logout', 'POST', {'SessionID': sid}, None)
```

</details>

### 3.4 (4p)

Write an endless loop which enumerates over user IDs from 1 upwards and for each user ID repeats the steps above, i.e.:

1. Make a GET request with the user ID in the query string (3.1)
1. Get the session ID from the corresponding response (3.2)
1. Send a POST request to logout the user with that session ID (3.3)

Make sure to handle the errors mentioned above (non-200 status codes and missing session headers). The loop should continue with the next user ID when such an error is encountered.

<details markdown="1">
<summary>Solution</summary>

```python
user_id = 0
while True:
  user_id += 1
  req = make_request(f'https://example.com?user={user_id}', 'GET')
  resp = req.send()
  if resp.status[0] != 200: continue
  if sid := get_header(resp, 'SessionID'):
    send_request('https://example.com/logout', 'POST', {'SessionID': sid[0]}, None)
```

</details>

### 3.5 (4p)

We want to add a new function `remove_header` which given a request or response object and a header name, removes that header from the object in place.
If the header doesn't exist, it should complete silently without error.
Write the signature for this function, with type annotations, as in the API above.

<details markdown="1">
<summary>Solution</summary>

```python
def remove_header(
    r: Request | Response,
    key: str,
) -> None
```

</details>
