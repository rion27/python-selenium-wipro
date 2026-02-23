from asyncio import timeout

import requests
from requests.auth import HTTPBasicAuth


try:
    #make a get request to an api endpoint
    headers={
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    response=requests.get("https://fakestoreapi.com/carts",auth=HTTPBasicAuth(username='username',password='password'),timeout=5,headers=headers)
    print(response)

    #check if the status code is 200 ok
    if response.status_code==200:
        print("Status code is 200 ok")
        #parse the json file
        data=response.json()
        print(data)
    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")