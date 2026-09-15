import requests 

"""Status Code Families With Meaning:
1xx-Informational "I received your request and I'm working on it." (Rare — you'll almost never see these.)
2xx-Success "Everything worked. Here's what you asked for."
3xx-Redirection "What you want has moved. Go look over there instead."
4xx-Client error "You made a mistake in your request."
5xx-Server error "I made a mistake trying to handle your request."
"""
BASE_URL = "https://jsonplaceholder.typicode.com"

def categorize_status_codes(status_code):
    """Return a human-readable category for an HTTP status code"""
    if 200 <= status_code < 300:
        return "Success"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Other"

def report(method, uri, response, description):
    """Print the method, uri, response, and description for a HTTP request"""
    print(f"{method} {uri}")
    print(f"Status: {response.status_code} ({categorize_status_codes(response.status_code)})")
    print(f"Description: {description}")
    print() # For spacing between blocks

# 1. GET /posts/1 - should succeed
uri = f"{BASE_URL}/posts/1"
response = requests.get(uri)
report("GET", uri, response, "Request succeeded-resource returned")

# 2. GET /posts/99999
uri = f"{BASE_URL}/posts/99999"
response = requests.get(uri)
report("GET", uri, response, "Resource not found - no post exists with this ID")


# 3. POST /posts with valid data, should create
uri = f"{BASE_URL}/posts"
new_post = {
    "title": "Status Detective",
    "body": "Testing POST creates a resource",
    "userId": 1
}
response = requests.post(uri, json=new_post)
report("POST", uri, response, "Resource created successfully")

# 4. DELETE /posts/1 - should succeed
uri = f"{BASE_URL}/posts/1"
response = requests.delete(uri)
report("Delete", uri, response, "Resource deleted successfully")

# 5. GET /invalidendpoint -BAD URI
uri = f"{BASE_URL}/invalidendpoint"
response = requests.get(uri)
report("GET", uri, response, "Endpoint DOES NOT exist - invalid URI")

# 6. GET /users/1/todos - nested resource
uri = f"{BASE_URL}/users/1/todos"
response = requests.get(uri)
report("GET", uri, response, "Request succeeded - nested resource (todos belonging to user 1 returned)")