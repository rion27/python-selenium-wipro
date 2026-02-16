import requests
try:
    data={
  "category": "Platform",
  "name": "Rion",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85
}
    #make a post request to an api endpoint
    response=requests.put("https://videogamedb.uk:443/api/v2/videogame/1",json=data)
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