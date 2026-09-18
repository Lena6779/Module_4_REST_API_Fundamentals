import requests

class APIClient:
    """A simple API client — similar to how you'd organize a Postman collection."""
    
    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.default_headers = headers or {}
    
    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        headers = {**self.default_headers, **kwargs.pop("headers", {})}
        response = requests.request(method, url, headers=headers, **kwargs)
        return {
            "status": response.status_code,
            "reason": response.reason,
            "time_ms": response.elapsed.total_seconds() * 1000,
            "data": response.json() if response.text else None,
            "headers": dict(response.headers),
        }
    
    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)
    
    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)
    
    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)
    
    def patch(self, path, **kwargs):
        return self._request("PATCH", path, **kwargs)
    
    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)


class JSONPlaceholderClient(APIClient):
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com")
    
    def get_user(self, user_id):
        """Get a specific user's profile."""
        result = self.get(f"/users/{user_id}")
        return result["data"]

    def get_user_posts(self, user_id):
        """Get all posts by a specific user."""
        result = self.get("/posts", params={"userId": user_id})
        return result["data"]

    def create_post(self, user_id, title, body):
        """Create a new post for a user."""
        result = self.post("/posts", json={"title": title, "body": body, "userId": user_id})
        return result["data"]

    def search_posts(self, query):
        """Search posts by title (client-side filtering)."""
        result = self.get("/posts")
        all_posts = result["data"]
        return [post for post in all_posts if query.lower() in post["title"].lower()]








# ----Tests----

# Test 1
client = JSONPlaceholderClient()
user = client.get_user(5)
print(user)

# Test 2
posts = client.get_user_posts(5)
print(len(posts))

# Test 3
new_post = client.create_post(5, "Learning REST APIs", "Practice post from my client.")
print(new_post["id"])

# Test 4 
matches = client.search_posts("qui")
print(len(matches))