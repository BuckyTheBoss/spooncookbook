import requests
from django.conf import settings

search_url = 'https://api.spoonacular.com/recipes/complexSearch'
auth_string = f'?apiKey={settings.SPOONACULAR_KEY}'

def search_recipe(text):
    response = requests.get(search_url+auth_string, params={'query': text})
    if response.status_code == 200:
        data = response.json()['results']
        return data

def get_recipe(id):
    url = f'https://api.spoonacular.com/recipes/{id}/information'
    response = requests.get(url + auth_string)
    if response.status_code == 200:
        data = response.json()
        return data