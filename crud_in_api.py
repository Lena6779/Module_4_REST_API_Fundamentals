import requests
import json 

# Step 1: GET-Read data

# GET a specific post
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"GET /posts/1")
print(f"Status: {response.status_code}")
post = response.json()
print(f"Title: {post['title'][:50]}...")
print()

# Step 2: POST-Create a new resource    
new_post = {                                  # Creates a new resource and we send data in that request body as seen below!
 "title": "My First API Post",
 "body": "This post was created using Python and the requests library!",
 "userId": 1
}

response = requests.post(
 "https://jsonplaceholder.typicode.com/posts",
 json=new_post # 'json=' automatically sets Content-Type to application/json
)

print(f"POST /posts")
print(f"Status: {response.status_code}") # 201 = Created
created = response.json()
print(f"Created post with ID: {created['id']}")
print(f"Title: {created['title']}")
print()

# Step 3: PUT-Replace a resource entirely
updated_post = { # Replaces the ENTIRE resource-Send ALL FIELDS
 "id": 1,
 "title": "Completely New Title",
 "body": "This body has been entirely replaced.",
 "userId": 1
}

response = requests.put(
 "https://jsonplaceholder.typicode.com/posts/1",
 json=updated_post
)

print(f"PUT /posts/1")
print(f"Status: {response.status_code}")
result = response.json()
print(f"Updated title: {result['title']}")
print()

# Step 4: PATCH-Update part of a resource
partial_update = { # Sends only the fields that are changed!
 "title": "Only the Title Changed"
}

response = requests.patch(
 "https://jsonplaceholder.typicode.com/posts/1",
 json=partial_update
)

print(f"PATCH /posts/1")
print(f"Status: {response.status_code}")
result = response.json()
print(f"Updated title: {result['title']}")
print(f"Body unchanged: {result['body'][:40]}...") # Original body preserved
print()

# Step 5: DELETE-Removes a resource
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(f"DELETE /posts/1")
print(f"Status: {response.status_code}")
print()