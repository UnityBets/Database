import requests
response = requests.get('https://raw.githubusercontent.com/UnityBets/Database/main/members/python/members-python.data')
#print (response.status_code)
print (response.content)
