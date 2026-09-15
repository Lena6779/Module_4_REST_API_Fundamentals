import requests

# Discover the available resources
# JSONPlaceholder has: /posts, /comments, /albums, /photos, /todos, /users
resources = ["posts", "comments", "albums", "photos", "todos", "users"]

print("=== JSONPlaceholder Resource Map ===\n")
for resource in resources:
    response = requests.get(f"https://jsonplaceholder.typicode.com/{resource}")
    data = response.json()
    print(f"/{resource} — {len(data)} items")

# Get a specific user
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
user = response.json()
print(f"User: {user['name']}\n")

# Get that user's posts (nested resource)
response = requests.get("https://jsonplaceholder.typicode.com/users/1/posts")
posts = response.json()
print(f"User 1 has {len(posts)} posts")
print(f"First post: {posts[0]['title'][:50]}...\n")

# Get that user's todos (nested resource)
response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
todos = response.json()
completed = sum(1 for t in todos if t['completed'])
print(f"User 1 has {len(todos)} todos ({completed} completed)")

# Get all posts by user 3 using a query parameter
# This is an alternative to /users/3/posts
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3}  # requests converts this to ?userId=3
)
posts = response.json()
print(f"Posts by user 3: {len(posts)}")
print(f"  First: {posts[0]['title'][:40]}...")
print()

# Get all completed todos for user 1
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"userId": 1, "completed": "true"}
)
todos = response.json()
print(f"Completed todos for user 1: {len(todos)}")
for todo in todos[:3]:
    print(f"  ✓ {todo['title']}")
