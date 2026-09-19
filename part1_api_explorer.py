import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, JSONDecodeError 

# Beginning of the first Public API 
BASE_URL = "https://jsonplaceholder.typicode.com"

def print_separator(title):
    """Prints a labeled divider so console output for each API is easy to tell apart."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# Reusable GET wrapper — timeout defaults to 5 seconds so a hung request fails fast instead of freezing the script indefinitely.
def safe_get(url, params=None, timeout=5):
    """Wraps a GET request with error handling for connection issues,
    timeouts, bad HTTP status codes, and unparseable JSON. Returns the
    parsed JSON on success, or None if anything went wrong."""
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()   # Turns 4xx/5xx into an exception
        return response.json()
    except ConnectionError:
        print(f"  [ERROR] Could not connect to {url}")
    except Timeout:
        print(f"  [ERROR] Request to {url} timed out")
    except HTTPError as e:
        print(f"  [ERROR] HTTP error for {url}: {e}")
    except JSONDecodeError:
        print(f"  [ERROR] Response from {url} was not valid JSON")
    return None

# ============================================================
# JSONPlaceholder — https://jsonplaceholder.typicode.com
# ============================================================

print_separator("JSONPlaceholder: single user")

user = safe_get(f"{BASE_URL}/users/1")
if user:
    print(user)

print_separator("JSONPlaceholder: all users (collection)")

users = safe_get(f"{BASE_URL}/users")
if users:
    print(f"Type of response: {type(users)}")
    print(f"Number of users: {len(users)}")
    print(users[0])

print_separator("JSONPlaceholder: query parameters")

# ?userId=3 filters the collection server-side. GET is safe/idempotent — it never modifies data, so repeating this request is always harmless.
posts = safe_get(f"{BASE_URL}/posts", params={"userId": 3})

if posts:
    print(f"Posts belonging to userId=3: {len(posts)}")
    print(posts[0])

print_separator("JSONPlaceholder: nested resource")

# /users/1/posts is a nested resource — the URL path itself expresses "this user's posts," instead of filtering a flat /posts endpoint.
nested_posts = safe_get(f"{BASE_URL}/users/1/posts")
if nested_posts:
    print(f"Posts by user 1 (via nested route): {len(nested_posts)}")
    print(nested_posts[0])

print_separator("JSONPlaceholder: POST (create)")

created_post = None

try:
    new_post = {"title": "My test post", "body": "Just practicing", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=5)
    response.raise_for_status()
    print(response.status_code)
    # Status 201 means a new resource was created.
    # POST is neither safe nor idempotent, since it creates a new resource every time it's called.
    created_post = response.json()
    print(created_post)

except ConnectionError:
    print("  [ERROR] Could not connect")
except Timeout:
    print("  [ERROR] Request timed out")
except HTTPError as e:
    print(f"  [ERROR] HTTP error: {e}")
except JSONDecodeError:
    print("  [ERROR] Response wasn't valid JSON")

print_separator("JSONPlaceholder: summary")

if user:
    print(f"User #1: {user['name']} ({user['username']}) — {user['email']}")
    print(f" Lives in: {user['address']['city']}")
    print(f" Works at: {user['company']['name']}")

if users:
    print(f"\nTotal users on the API: {len(users)}")

if posts:
    print(f"\nUser 3 has written {len(posts)} posts. Titles:")
    for p in posts:
        print(f"  - {p['title']}")

if nested_posts:
    print(f"\nUser 1 has written {len(nested_posts)} posts (via nested route)")

if created_post:
    print(f"\nCreated a new post with id {created_post['id']}: \"{created_post['title']}\"")

# Beginning of the second Public API 
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"


# ============================================================
# PokeAPI — https://pokeapi.co/api/v2
# ============================================================

print_separator("PokeAPI: single resource")

# Every PokeAPI resource has both a name and a stable numeric id 
# /pokemon/pikachu and /pokemon/25 are the same resource, two valid URLs for identifying it.
pikachu = safe_get(f"{POKEAPI_BASE_URL}/pokemon/pikachu")
if pikachu:
    print(f"name: {pikachu['name']}")
    print(f"id: {pikachu['id']}")
    print(f"height: {pikachu['height']}  weight: {pikachu['weight']}")

print_separator("PokeAPI: collection (paginated list)")

# Results is just {name, url} pairs, not full pokemon data — PokeAPI wraps its lists in a pagination envelope, unlike JSONPlaceholder's plain list for /users.

# limit/offset here work the same way ?userId=3 did earlier — query params, not part of the URL path, controlling what the server returns
page = safe_get(f"{POKEAPI_BASE_URL}/pokemon", params={"limit": 5, "offset": 0}) 

if page:
    print(f"Total pokemon in the API: {page['count']}")
    print(f"Next page URL: {page['next']}")
    print("Results (just name + url, not full data):")
    for p in page["results"]:
        print(f"  {p['name']}")

print_separator("PokeAPI: nested fields (types, stats, abilities)")

# Each type/stat/ability here is a {name, url} REFERENCE, not the full resource — PokeAPI keeps individual payloads smaller by making you fetch the full type/stat/ability data separately if you need it.
if pikachu:
    print("Types:")
    for t in pikachu["types"]:
        print(f"  {t['type']['name']}")

    print("Stats:")
    for s in pikachu["stats"]:
        print(f"  {s['stat']['name']}: {s['base_stat']}")

    print("Abilities:")
    for a in pikachu["abilities"]:
        hidden = " (hidden)" if a["is_hidden"] else ""
        print(f"  {a['ability']['name']}{hidden}")

print_separator("PokeAPI: error handling (404)")

# Unlike JSONPlaceholder, a nonexistent PokeAPI resource returns 404 with NO body at all.
# Safe_get's raise_for_status() catches this before we'd ever try (and fail) to call .json() on an empty response.
missing = safe_get(f"{POKEAPI_BASE_URL}/pokemon/not-a-real-pokemon")
print(f"Result: {missing!r}")

print_separator("PokeAPI: summary")

if pikachu:
    types_list = ", ".join(t["type"]["name"] for t in pikachu["types"])
    print(f"{pikachu['name'].title()} (#{pikachu['id']}) — type(s): {types_list}")
    print(f"  height: {pikachu['height']}  weight: {pikachu['weight']}")

if page:
    print(f"\nPokeAPI has {page['count']} pokemon total")
    names = ", ".join(p["name"] for p in page["results"])
    print(f"  First {len(page['results'])} in the list: {names}")