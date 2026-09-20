API Documentation
JSONPlaceholder

Base URL: https://jsonplaceholder.typicode.com

Authentication: None — no API key or token required.

Endpoints tested
Method	Path	Description	Example response shape
GET	/users/1	Fetch a single user by id	{ "id": 1, "name": str, "username": str, "email": str, "address": { "city": str, "geo": {...} }, "company": { "name": str } } — a flat object with two nested sub-objects
GET	/users	Fetch the full collection of users	[ {...user...}, {...user...}, ... ] — a JSON array of user objects (10 total)
GET	/posts?userId=3	Fetch posts filtered by query parameter	[ { "userId": 3, "id": int, "title": str, "body": str }, ... ] — array of flat post objects
GET	/users/1/posts	Fetch a nested resource — posts belonging to user 1	Same shape as above, but reached via a nested URL path instead of a filter
POST	/posts	Create a new post (not actually persisted — fake API)	Echoes the submitted body back with a new fake id added, e.g. { "title": str, "body": str, "userId": int, "id": 101 }
Rate limits observed

None. No 429 responses or rate-limit headers were seen during testing, even across repeated requests.

What surprised me

A GET for a nonexistent resource (/posts/99999) returns HTTP 404 with an empty JSON object {} as the body — not an error message field like {"error": "not found"}. This means status-code checking is essential; you can't rely on the response body to tell you something went wrong. Also notable: the same "posts by user 1" data is reachable two different ways — /posts?userId=1 (flat + filter) and /users/1/posts (nested path) — both return the same records.

PokeAPI

Base URL: https://pokeapi.co/api/v2

Authentication: None — no API key or token required.

Endpoints tested
Method	Path	Description	Example response shape
GET	/pokemon/pikachu	Fetch a single pokemon by name	{ "id": 25, "name": "pikachu", "height": int, "weight": int, "types": [ {"type": {"name": str}} ], "stats": [ {"stat": {"name": str}, "base_stat": int} ], "abilities": [ {"ability": {"name": str}, "is_hidden": bool} ], "sprites": {...} } — large object, 20+ top-level keys
GET	/pokemon/25	Fetch the same pokemon by numeric id	Identical response to /pokemon/pikachu — name and id are interchangeable lookups
GET	/pokemon?limit=5&offset=0	Fetch a paginated list of pokemon	{ "count": 1351, "next": "url or null", "previous": "url or null", "results": [ {"name": str, "url": str}, ... ] } — pagination envelope, not a bare list
GET	/pokemon/not-a-real-pokemon	Nonexistent resource — deliberate 404 test	No body at all on failure
Rate limits observed

None hit directly during testing, but PokeAPI applies fair-use rate limiting (no published hard number) — rapid, repeated requests without any delay can occasionally return 429 Too Many Requests.

What surprised me

Two things stood out compared to JSONPlaceholder:

The 404 response shape is different. JSONPlaceholder returns 404 with an empty JSON object {} as the body. PokeAPI returns 404 with no body at all — calling .json() on it without checking the status first throws a JSONDecodeError rather than giving you an empty dict to work with.
Nested data is referenced, not embedded. Fields like types, stats, and abilities don't contain full data — each entry is just a {name, url} reference (e.g. {"type": {"name": "electric", "url": "..."}}), and you'd need a separate request to that URL to get the full details for that type/stat/ability. This keeps individual pokemon payloads smaller but means fully resolving all of a pokemon's related data takes many follow-up requests — a very different tradeoff than JSONPlaceholder's flatter, fully self-contained objects.