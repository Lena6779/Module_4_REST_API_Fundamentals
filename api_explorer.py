import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# ============================================================
# TASK 1: GET all users
# GET requests retrieve data from the server — no body needed.
# ============================================================
print("TASK 1: All users")
print("-"* 40)

response = requests.get(f"{BASE_URL}/users")
print(f"Status Code: {response.status_code}")

users = response.json()
print(f"Items returned: {len(users)}")
for user in users:
    print(f"{user['name']} - {user['email']}")

# ============================================================
# TASK 2: GET posts by user #3
# Query parameters (?key=value) filter the results server-side.
# ============================================================

print("\nTask 2: Posts by User #3")
print("-" * 40)

response = requests.get(f"{BASE_URL}/posts", params={"userId": 3})
print(f"Status Code: {response.status_code}")

posts = response.json()
print(f"Items returned: {len(posts)}")
for post in posts:
    print(f"[{post['id']}] {post['title']}")

# ============================================================
# TASK 3: GET comments on post #1 (nested resource)
# /posts/1/comments means "comments belonging to post 1"
# ============================================================

print("TASK 3: GET all comments on post #1")
print("-" * 40)

response = requests.get(f"{BASE_URL}/posts/1/comments")
print(f"Status Code: {response.status_code}")

comments = response.json()
print(f"Items returned: {len(comments)}")
for comment in comments:
    print(f"[{comment['name']}] {comment['email']}")

# ============================================================
# TASK 4: POST a new post
# POST creates a new resource. Send data in the json= parameter.
# JSONPlaceholder simulates this — returns a realistic response but doesn't persist.
# ============================================================

print("\nTASK 4: Create a New Post (POST)")
print("-" * 40)

new_post = {
    "title": "My first API Post",
    "body": "This was created by sending a POST request!",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(f"Status Code: {response.status_code}")

created = response.json()
print(f"Created post id: {created['id']}")
print(f"Title: {created['title']}")