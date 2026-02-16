import requests
import json

try:
    # Send GET request
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()  # Raise error if request fails

    # Convert response to JSON
    posts = response.json()

    # Save JSON data to file
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)

    print("Posts saved successfully to posts.json")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
