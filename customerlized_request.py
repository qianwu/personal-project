# This is a class about customerlized request
# The company tech structure is as follows:
# user request from getway -> getway -> service -> dao -> db

import requests
import json

class customerlized_request:
    def __init__(self, method, path, h= {"Content-Type": "application/json;charset=UTF-8"}):
        self.path = path
        self.method = method.upper()
        self.h = h

    
    
    # get the request
    def get_request(self):
        return requests.get_request()
    
    # format the request
    def format_request(self):
        return self.request.format_request()
    
get_request = requests.get("https://jsonplaceholder.typicode.com/posts")
print(get_request.status_code)
for info in get_request.json():
    print(info)
   
 