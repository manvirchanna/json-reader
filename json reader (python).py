import requests as requests
def last_update():
    response = requests.get('API LINK')
    response = response.json()
    print("response: ",response)
    
    result = response["result"]
    print(result)
  
    return response

x=last_update()
print(x)
