import requests

try:
    # Send GET request
    response=requests.get("https://jsonplaceholder.typicode.com/users")

    # Check if request was successful
    if response.status_code==200:
        users=response.json()

        # Loop through users and print name and email
        for user in users:
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
