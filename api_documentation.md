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