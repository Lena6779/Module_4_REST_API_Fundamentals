import requests

# --- GET a single post ---
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(f"Status Code: {response.status_code}")  # 200 = success
print(f"Content Type: {response.headers['Content-Type']}")
print()

post = response.json()
print(f"Post Title: {post['title']}")
print(f"Post Body: {post['body'][:80]}...")
print(f"Author (userId): {post['userId']}")

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

posts = response.json()
print(f"\nUser 1 has {len(posts)} posts:")
for post in posts[:3]:
    print(f"  [{post['id']}] {post['title'][:50]}...")

new_post = {
    "title": "My First API Post",
    "body": "This was created by sending a POST request!",
    "userId": 1,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

print(f"\nCreate Status: {response.status_code}")  # 201 = Created
created = response.json()
print(f"Created post with id: {created['id']}")
print(f"Title: {created['title']}")
