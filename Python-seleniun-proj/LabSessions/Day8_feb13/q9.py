import requests

try:
    # Open file in binary mode
    with open("sample.txt", "rb") as file:
        files = {
            "file": file
        }

        # Send POST request with file
        response = requests.post(
            "https://httpbin.org/post",
            files=files
        )

        response.raise_for_status()

        # Print server response
        print("Server Response:")
        print(response.json())

except FileNotFoundError:
    print("File not found. Please check the file path.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
