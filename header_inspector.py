import requests

"""A utility tool that inspects and compares headers across different API endpoints"""

# Design choice: using a for loop to run the header-check function once per endpoint, instead of writing three separate function calls (one per URL)

def inspect_headers_reponse(url):
    response = requests.get(url)

    print(response.status_code)
    print(response.headers)

    content_type = response.headers.get("Content-Type", "Not specified")
    content_length = response.headers.get("Content-Length", "Not specified")
    print(f"Content-Type: {content_type}")
    print(f"Content-Length: {content_length}")

    caching_headers = ["Cache-Control", "ETag", "Last-Modified", "Expires", "Age", "Vary"]
    present_caching = [h for h in caching_headers if h in response.headers]
    print("Caching headers present:", present_caching)

    rate_limit_headers = ["X-RateLimit-Limit", "X-RateLimit-Remaining", "X-RateLimit-Reset", "Retry-After"]
    present_rate_limit = [h for h in rate_limit_headers if h in response.headers]
    print("Rate-limiting headers present:", present_rate_limit)

    print("Total number of response headers:", len(response.headers))

endpoints = [                                            # My list of endpoints 
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://httpbin.org/get",
]

for url in endpoints:
    print(f"{url}")
    inspect_headers_reponse(url)

def post_with_header():
    url = "https://httpbin.org/post"
    payload = {"student": "Lena","module": "Module 4"}
    custom_headers = {"X-Student-Name": "Lena"}         # Custom header format given to use "X-Student-Name" then our name

    response = requests.post(url, json=payload, headers=custom_headers)
    print(response.status_code)
    print(response.json())

post_with_header()