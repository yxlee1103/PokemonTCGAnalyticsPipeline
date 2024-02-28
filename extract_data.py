import requests
import pandas as pd

url = 'https://api.pokemontcg.io/v2/cards'
headers = {
    'X-Api-Key': 'cd2aa4e3-d663-4fa4-8f99-3c74d7c9f61c'
}

response = requests.get(url, headers=headers)
data = pd.DataFrame()

if response.status_code == 200:
    for i in range(1, 100):
        response = requests.get(url, headers=headers, params={'page': i})
        temp_data = pd.DataFrame(response.json()['data'])
        data = data._append(temp_data, ignore_index=True)

else:
    print("Failed to fetch data:", response.status_code)

data.to_csv('pokemon_tcg_cards.csv', index=False)
