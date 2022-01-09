# Importing data from an IMDB API (JSON) related to their top 250 movies and converting it into a Pandas DataFrame
import pandas as pd
import requests
url = 'https://imdb-api.com/en/API/Top250Movies/k_52mnkeby'
r = requests.get(url)
text = r.text
json_data = r.json()

df = pd.DataFrame(json_data)
print(df.head())


