import requests
import json


BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. GET request for a specific user from JSONPlaceholder
print("=" * 60)
print("1. GET /users/1")
response = requests.get(f"{BASE_URL}/users/1")
req = response.request  # Capture the actual sent request for inspecting headers/body
print(f"{response.request.method} {response.request.url}")

print("Request Headers:")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")

print("Request Body")
if req.body:         # Holds the JSON payload as bytes for POST/PATCH, None otherwise
    print(req.body)
else:
    print("(none)")

print(f"Status: {response.status_code} {response.reason}")
print("Response Headers:")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Content-Length: {response.headers.get('Content-Length')}")

print("Response Body:")
print(response.text)
print(f"Elapsed Time: {response.elapsed.total_seconds() * 1000:.2f} ms") # Includes conversion to miliseconds

# 2. POST request creating a new post 
print("=" * 60)
print("2. POST request for creating a new post")
new_post = {
    "title": "Request Anatomy",
    "body": "Testing a POST request",
    "userId": 1
}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
req = response.request # Capture the actual sent request for inspecting headers/body
print(f"{response.request.method} {response.request.url}")

print("Request Headers:")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")

print("Request Body")
if req.body: # Holds the JSON payload as bytes for POST/PATCH, None otherwise
    print(req.body)
else:
    print("(none)")

print(f"Status: {response.status_code} {response.reason}")
print("Response Headers:")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Content-Length: {response.headers.get('Content-Length')}")

print("Response Body:")
print(response.text)
print(f"Elapsed Time: {response.elapsed.total_seconds() * 1000:.2f} ms") # Includes conversion to miliseconds

# 3. PATCH request updating a post's title
print("=" * 60)
print("3. PATCH request updating a post's title")
updated_data = {
    "title": "Updated Title via PATCH"
}
response = requests.patch(f"{BASE_URL}/posts/1", json=updated_data)
req = response.request # Capture the actual sent request for inspecting headers/body
print(f"{response.request.method} {response.request.url}")

print("Request Headers:")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")

print("Request Body")
if req.body: # Holds the JSON payload as bytes for POST/PATCH, None otherwise
    print(req.body)
else:
    print("(none)")

print(f"Status: {response.status_code} {response.reason}")
print("Response Headers:")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Content-Length: {response.headers.get('Content-Length')}")

print("Response Body:")
print(response.text)
print(f"Elapsed Time: {response.elapsed.total_seconds() * 1000:.2f} ms") # Includes conversion to miliseconds