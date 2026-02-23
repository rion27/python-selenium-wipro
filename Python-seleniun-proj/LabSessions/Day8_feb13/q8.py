import requests

# Create a Session object
session = requests.Session()

# First request: set a cookie
response1 = session.get("https://httpbin.org/cookies/set?username=rion")

print("After setting cookie:")
print(response1.text)

# Second request: retrieve cookies
response2 = session.get("https://httpbin.org/cookies")

print("\nCookies stored in session:")
print(response2.json())
