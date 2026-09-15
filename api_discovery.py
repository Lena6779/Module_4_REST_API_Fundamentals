import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
print(response.status_code)
data = response.json()
print(data.keys())

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(response.status_code)
data = response.json()
print(data['name'], data['id'])

response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
data = response.json()
print(data['types'])
print(data['abilities'])

response = requests.get("https://pokeapi.co/api/v2/type/12/")
print(response.status_code)
print(response.json().keys())

response = requests.get("https://pokeapi.co/api/v2/pokemon")
data = response.json()
print(data.keys())
print(data['count'])
print(len(data['results']))
print(data['results'][:3])
print(data['next'])

response = requests.get("https://pokeapi.co/api/v2/pokemon", params={"limit": 5, "offset": 10})
data2 = response.json()
print(len(data2['results']))
print(data2['results'])

response = requests.get("https://pokeapi.co/api/v2/ability/65/")
print(response.status_code)