
import time
def get_time():
    return time.time()
print (get_time())

# import requests module 
import requests 
from requests.auth import HTTPBasicAuth 
# Making a get request 
response = requests.get('https://api.github.com / user, ', 
            auth = HTTPBasicAuth('user', 'pass')) 
# print request object 
print(response) 