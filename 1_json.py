#JSON
# JavaScript Object Notation
# JSON is a file extension for sharing data (information) between frontend and backend and between backend and backend. 
# JSON is very much similar to python dictionary having keys and values where keys must be string enclosed in doble quotation mark. and values can be following datatype.

'''
String:"Hello World" (must be enclosed in double quotation)
Number: 1,2,3.1415
Boolean: true,false (similar to python True and False)
Null:null (similar to python None)
Array:[1,2,"true","Hello"] (list)
Obejct:"address":{"city":"BKT","country":"Nepal"} (dict)
'''

# Example:
my_json_string = '''{
            "name":"ram",
            "age":24,
            "is_student":true,
            "phone":null,
            "courses":["python","django","drf"],
            "address":{"city":"BKT","country":"Nepal"} (dict)
}
'''

# from json to python dictionary
import json 
py_dict = json.loads(my_json_string)
print(py_dict)