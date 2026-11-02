
# This a Python object (dict)
py_obj = {
  "pi": 3.1415926535897932384626433,
  "small": 1.0000000000000008
}
assert type(py_obj) == dict

# This is JSON, i.e. a string representation of the same data
raw_json = """
{
  "pi": 3.1415926535897932384626433,
  "small": 1.0000000000000008
}
"""
assert type(raw_json) == str

# Parsing the JSON string gives us another Python object (dict) equal to the first one
import json
py_obj_2 = json.loads(raw_json)
assert type(py_obj_2) == dict
print(py_obj_2)
assert py_obj_2 == py_obj

# Note how conversion from JSON number to Python float reduces precision
assert json.loads("3.1415926535897932384626433") == 3.141592653589793
