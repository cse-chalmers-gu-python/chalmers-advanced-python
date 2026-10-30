
# This is not JSON, it is a Python object (POPO)
popo = {
  "pi": 3.1415926535897932384626433,
  "small": 1.0000000000000008
}


# This is JSON, i.e. a string representation
rawjson = """
{
  "pi": 3.1415926535897932384626433,
  "small": 1.0000000000000008
}
"""

# Parsing the JSON string gives us a Python object
import json
popo_from_json = json.loads(rawjson)
print(popo_from_json)
print(popo_from_json == popo)
