import requests

response = requests.get("https://api.github.com/user")
print(response.status_code)

response = requests.get("https://api.github.com/users/octocat")
print(response.status_code)

def create_auth_headers(api_key, auth_type):
    if auth_type == "bearer":
        return {"Authorization": f"Bearer {api_key}"}
    elif auth_type == "api-key":
        return {"Authorization": f"api-key {api_key}"}
    else:
        return None # Unrecognized auth_type 

# TESTING FUNCTION (WITH CORRECT DATA)
print("Test 1: ")
result = create_auth_headers("my_test_key_598", "bearer")
print(result)

# TESTING FUNCTION (WITH CORRECT DATA)
print("Test 2: ")
result = create_auth_headers("my_test_key_467", "api-key")
print(result)

# TESTING FUNCTION (WITH WRONG DATA)
print("Test 3: ")
result = create_auth_headers("my_test_key_467", "")
print(result)