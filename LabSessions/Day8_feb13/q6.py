import requests

try:
    # Send GET request to fetch all users
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()   # Raise error if request fails

    users = response.json()

    # Print usernames in uppercase
    for user in users:
        print(user["username"].upper())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
