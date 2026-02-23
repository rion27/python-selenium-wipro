import requests

try:
    # Send GET request with query parameter userId=2
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": 2}
    )

    # Check if request was successful
    if response.status_code == 200:
        posts = response.json()

        # Print number of posts returned
        print(f"Number of posts for userId=2: {len(posts)}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
