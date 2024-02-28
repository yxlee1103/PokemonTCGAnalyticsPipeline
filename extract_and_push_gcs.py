import requests
import pandas as pd

url = 'https://api.pokemontcg.io/v2/cards'
headers = {
    'X-Api-Key': 'cd2aa4e3-d663-4fa4-8f99-3c74d7c9f61c'
}
response = requests.get(url, headers=headers)
data = pd.DataFrame()
csv_filename = 'pokemon_tcg_cards.csv'


# Get data from API to csv
if response.status_code == 200:
    for i in range(1, 3):
        response = requests.get(url, headers=headers, params={'page': i})
        temp_data = pd.DataFrame(response.json()['data'])
        data = data._append(temp_data, ignore_index=True)

else:
    print("Failed to fetch data:", response.status_code)

data.to_csv(csv_filename, index=False, header=None)

from google.cloud import storage
# Check
if not(data.empty):    
        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Upload the CSV file to GCS
        bucket_name = 'pokemon_tcg_data'
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCS

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)

        print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
else:
    print("No data available from the API.")
