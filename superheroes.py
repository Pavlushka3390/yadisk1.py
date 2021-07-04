import requests

search_url = "https://superheroapi.com/api/2619421814940190/search/"
character_name = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]


for character in character_name:
    get_char = requests.get(search_url + character['name'])
    character['intelligence'] = int(get_char.json()['results'][0]['powerstats']['intelligence'])
    print(character['name'])

print("самый умный персонаж:", sorted(character_name, key=lambda char: -char['intelligence'])[0]['name'])