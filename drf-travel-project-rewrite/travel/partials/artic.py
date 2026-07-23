import requests


def fetch_data_place_api(external_id):
    url = f'https://api.artic.edu/api/v1/places/{external_id}'
    response = requests.get(url)
    return response.json()