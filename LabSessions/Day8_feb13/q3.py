import requests

try:
    # Data to send in POST request
    payload = {
        "title": "My New Post",
        "body": "This is a test post",
        "userId": 1
    }

    # Send POST request
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    # Verify status code
    if response.status_code == 201:
        print("Status code is 201 - Resource created successfully")
        print("Response JSON:", response.json())
    else:
        print(f"Failed! Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
