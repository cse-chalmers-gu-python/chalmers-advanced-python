import json 

POPO = {    'pi': 3.141_592_653_589_793_238_462_6433,
            'small': 1.000_000_000_000_0008     }

JSON_OBJ = """ {    "pi": 3.1415926535897932384626433,
            "small": 1.0000000000000008     } """

json_obj = json.loads(JSON_OBJ)


print(POPO, type(POPO))
# print(JSON_OBJ, type(JSON_OBJ))
print(json_obj, type(json_obj))