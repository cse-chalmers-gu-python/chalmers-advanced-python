# Get domain name from URL, using string processing
def get_domain(url):
  pos = url.index("://")
  url = url[pos + 3:]
  pos = url.index("/")
  url = url[:pos]
  return url

# Get query string arguments as dict from URL, using string processing
def get_query_params(url):
  pos = url.index("?")
  qs = url[pos + 1:]
  args = qs.split('&')
  kvs = {}
  for a in args:
    k,v = a.split('=')
    kvs[k] = urldecode(v)
  return kvs

def urldecode(url):
  return url.replace('%20', ' ').replace('%26', '&')

# ---

# Get domain name from URL, using urllib.parse library
def get_domain_2(url):
  purl = urlparse(url)
  return purl.netloc

# Get query string arguments as dict from URL, using urllib.parse library
from urllib.parse import urlparse, parse_qs
def get_query_params_2(url):
  purl = urlparse(url)
  return parse_qs(purl.query)

# Set/replace query string argument value in URL, using urllib.parse library
from urllib.parse import urlunparse, urlencode
def set_query_param(url, key, value):
  purl = urlparse(url)
  kvs = parse_qs(purl.query)
  kvs[key] = value
  qs = urlencode(kvs)
  purl = purl._replace(query=qs)
  return urlunparse(purl)

# ---

url = "http://www.example.com/films/search?title=The%20Matrix&year=1999"

# url = "http://www.example.com/films/search?title=Matrix&year=1999"
# url = "http://www.example.com/films/search?title=Tom&Jerry"
# url = "http://www.example.com/films/search?title=Tom%20%26%20Jerry&year=2000"

print(get_domain(url))
print(get_domain_2(url))

print(get_query_params(url))
print(get_query_params_2(url))

print(set_query_param(url, 'title', 'ser &trängen køn$t/g ut?'))

