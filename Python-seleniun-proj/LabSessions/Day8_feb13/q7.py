import requests

try:
    # Send GET request with 2-second timeout
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )

    response.raise_for_status()

    users = response.json()

    for user in users:
        print(user["username"].upper())

except requests.exceptions.Timeout:
    print("Request timed out after 2 seconds")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
