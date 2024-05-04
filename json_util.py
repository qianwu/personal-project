# This is a json util to help operate json data during testing 

import json

class json_solution:
    def __init__(self,json_data):
        self.json_data = json_data
    
    # usually we need to perpare json payload before sending to API
    def contruct_json_payload(self, data):
        return json.dumps(data)

    # parse json data
    def parse_json(self):
        return json.loads(self.json_data)

    # get value from json data, but if the value is under a list, we need to provide the index, otherwise, it will return the list, and if the value is a child node of a json object, we need to provide both the parent and child node
    def get_value_from_json(self, key, index=None, parent=None):
        data = json.loads(self.json_data)
        if parent:
            return data[parent][key]
        if index:
            return data[key][index]
        return data[key]

# json_string = '{"name":"John", "age":30, "city":"New York"}'
# json_util = json_solution(json_string)
# print(json_util.contruct_json_payload({"name":"John", "age":30, "city":"New York"}))
# print(json_util.parse_json())
# print(json_util.get_value_from_json("name"))
json_string = '{"name":["John", "Doe"], "age":30, "city":{"New York" : "NY"}}'
json_util = json_solution(json_string)
print(json_util.get_value_from_json("name",1,None))
print(json_util.get_value_from_json("New York",None,"city"))