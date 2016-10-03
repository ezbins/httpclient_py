#!/usr/bin/env python3

import urllib3
import json

http = urllib3.PoolManager()
value = int(35)
#print(type(value))

data ={'intValue':value} 
json_data = json.dumps(data).encode('utf-8')
print(json_data)

#傳送json data以binary 方式傳送
res = http.request(
    'POST',
    'http://localhost:8080/PythonServlet/Main',
    body=json_data,
    headers={'Content-Type':'application/json'})

print(res.status)
print(res.data)