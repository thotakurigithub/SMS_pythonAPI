import requests
from requests import request

url = 'https:www.fast2sms.com/dev/bulkV2'
payload ="sender_id= TXTIND &message=Alert! There is an Intruder in IT Dept.&route=v3&numbers=8500826897,9445002522"
headers = {
    'authorization': "",
    'Content-TYPE': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
}

response = requests.request("POST",'https://www.fast2sms.com/dev/bulkV2?authorization=oqvgGxm1Sa5ZuC4itTPKMDRbF3y6eNEkWQfc8JjlABHzYdUOrVpzUXGVZy3TkwHMPR7Oo84urJW920LQ&route=&sender_id=&message=&variables_values=&flash=0&numbers=',data=payload,headers=headers)
print(response.text)




