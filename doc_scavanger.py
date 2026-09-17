import requests

url = "https://api.github.com/search/repositories"

params = {                   # Becomes the URL query string '?q=org:google&sort=stars&order=desc&per_page=3'
    "q": "org:google", # q is short for "query"
    "sort": "stars",
    "order": "desc",
    "per_page": 3,
}

response = requests.get(url, params=params)
response.raise_for_status()  # Raises an exception on 4xx/5xx instead of failing silently
data = response.json()

for repo in data["items"]: # data["items"] is a list of dicts-one per repo that gets looped through
    name = repo["name"]
    description = repo["description"] or "No description"
    stars = repo["stargazers_count"]
    language = repo["language"] or "Unknown"
    print(f"{name}\n  Description: {description}\n  Stars: {stars}\n  Language: {language}\n")

remaining = response.headers.get("X-RateLimit-Remaining")
print(f"Remaining rate limit: {remaining}")