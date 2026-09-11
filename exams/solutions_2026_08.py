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

sample_data = [
   {"person": "Robert Robinson",
    "sex": "male",
    "award": "Nobel Prize in Chemistry",
    "year": 1947,
    "birthDate": 1886,
    "birthPlace": "Rufford",
    "country": "United Kingdom",
    "deathDate": 1975
  },
   {"person": "Han Kang",
    "sex": "female",
    "award": "Nobel Prize in Literature",
    "year": 2024,
    "birthDate": 1970,
    "birthPlace": "Gwangju",
    "country": "South Korea"
  }]

# 2.1 the number of different awards
awards = len({item['award'] for item in nobel_data})
print(awards)

# 2.2 the names of all female laureates
females = [item['person'] for item in nobel_data if item['sex'] == 'female']
print(females)

# 2.3 the number of persons who are still alive (i.e. have no deathDate)
still_alive = len([item['person'] for item in nobel_data if not item.get('deathDate', False)])
print(still_alive)

# 2.4 how many prizes in each country
countries = {
    a: len([1 for item in nobel_data if item['country'] == a])
      for a in {item['country'] for item in nobel_data}
    }
print(countries)


# Q3

class Year:
    def __init__(self, year, is_bce=False):
        self.year = year
        self.is_bce = is_bce

    def normalise(self):
        return self.year * (-1 if self.is_bce else 1)

    def __str__(self):
        return str(self.year) + (' BCE' if self.is_bce else '')

    def __lt__(self, other):
        return self.normalise() < other.normalise()

# 3.1

y1 = Year(1954)      # birth of Sócrates, Brazilian footballer
y2 = Year(470, True) # birth of Socrates, Greek philosopher
print(y1, '<', y2, y1 < y2)
# 1954 < 470 BCE False

# 3.2

class YearSpan():
    def __init__(self, year1, year2):
        if year1 < year2:
            self.year1 = year1
            self.year2 = year2
        else:
            self.year1 = year2
            self.year2 = year1
    
    def __str__(self):
        diff = self.year2.normalise() - self.year1.normalise()
        return f'{self.year1} -> {self.year2} = {diff} years'

print(YearSpan(y1, y2))

# 3.3 

class EventYear(Year):
    def __init__(self, year, is_bce, desc):
        super().__init__(year, is_bce)
        self.desc = desc
    
    def __str__(self):
        return f'{super().__str__()}: {self.desc}'

print(YearSpan(ey1, ey2))

# Q4

# 4.1

req = make_request('https://example.com?user=42', 'GET')
resp = req.send()
if resp.status[0] != 200: resp = None

# 4.2

if h := get_header(resp, 'SessionID'):
  sid = h[1]

# 4.3

send_request('https://example.com/logout', 'POST', {'SessionID': sid}, None)

# 4.4

user_id = 0
while True:
  user_id += 1
  req = make_request(f'https://example.com?user={user_id}', 'GET')
  resp = req.send()
  if resp.status[0] != 200: continue
  if sid := get_header(resp, 'SessionID'):
    send_request('https://example.com/logout', 'POST', {'SessionID': sid[0]}, None)