import requests
try:
    data={
    "name": "Apple Macbook Pro 16 (updated name)"
}
    #make a post request to an api endpoint
    response=requests.patch("https://api.restful-api.dev/objects/ff8081819c5368bb019c55a715300478",json=data)
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