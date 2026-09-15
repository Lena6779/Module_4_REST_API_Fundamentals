import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

# NOTE on design choice:
# The assignment says step 2 (READ) should use the ID returned by the POST
# in step 1. However, JSONPlaceholder is a mock API - it accepts POST
# requests and returns a realistic-looking response (including a fake new
# ID, usually 201), but it never actually saves the new resource. That
# means a GET on that fake ID would just return 404, and every step after
# it (UPDATE, READ AGAIN, DELETE, VERIFY) would fail the same way.
#
# To keep the rest of the CRUD cycle demonstrable against real data, this
# script instead runs steps 2-6 against todo ID 1, one of JSONPlaceholder's
# 200 pre-seeded todos that actually exists. This shows realistic 200
# responses for READ/UPDATE/DELETE, at the cost of not literally reusing
# the ID from step 1's response.

# Step 1: CREATE 
# Create a new todo 
new_todo = {
    "title": "Complete Module 4",
    "completed": False,
    "userId": 1
}

response = requests.post(BASE_URL, json=new_todo)
print(f"POST {BASE_URL}")
print(f"Status: {response.status_code}")
created = response.json()
print(f"Created todo with ID: {created['id']}")
print(f"Title: {created['title']}")
print()

# Step 2: READ
# GET a specific todo
uri = f"{BASE_URL}/1"
response = requests.get(uri)
print(f"GET {uri}")
print(f"Status: {response.status_code}")
todo = response.json()
print(f"Title: {todo['title'][:50]}...")  # Important note: todo never is actually saved so the real id1 is actually printed 
print()

# Step 3: UPDATE
# PATCH the todo to mark it as completed where before it was False(Not completed)
updated_data = {
    "completed": True
}

uri = f"{BASE_URL}/1"
response = requests.patch(uri, json=updated_data)
print(f"PATCH {uri}")
print(f"Status: {response.status_code}")
updated_todo = response.json()
print(f"Completed: {updated_todo['completed']}")
print()

# Step 4: READ AGAIN
# GET the todo again to verify the update that was just made
uri = f"{BASE_URL}/1"
response = requests.get(uri)
print(f"GET {uri}")
print(f"Status: {response.status_code}")
todo = response.json()
print(f"Completed: {todo['completed']}")
print()

# Step 5: DELETE
# Delete the todo 
uri = f"{BASE_URL}/1"
response = requests.delete(uri)
print(f"DELETE {uri}")
print(f"Status: {response.status_code}")
print()

# Step 6: VERIFY
# Try to GET the deleted todo and handle the response it gives you
uri = f"{BASE_URL}/1"
response = requests.get(uri)
print(f"GET {uri}")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("Todo still returned (JSONPlaceholder doesn't persist deletes)")
    print("Thus the original resource is still served even after the DELETE step!")
elif response.status_code == 404:
    print("Confirmed: todo no longer exists.")