import requests;

url = 'https://pokeapi.co/api/v2/'

def findUrl (name):
    new_url = f'{url}pokemon/{name}'
    print("name : ",name)
    print("new_url : ",new_url)
    response = requests.get(new_url);
    # print(type(response.status_code))
    if response.status_code == 200:
        print("your are inside succes case ")
        return response.json()
        
    else:
        print(f"The url fail with an status code {response.status_code}")

data = findUrl("pikachu");

if data:
    print(data["name"])