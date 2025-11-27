import requests as r
url = 'https://www.cse.chalmers.se/~aarne/'
req = r.get(url)
print(req.status_code)
print(req.headers)
print(req.text)
