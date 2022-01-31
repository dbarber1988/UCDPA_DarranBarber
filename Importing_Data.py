# Importing data from a CSV file saved locally on my laptop into Python as a Pandas DataFrame.
import pandas as pd
df = pd.read_csv(r'C:\Users\Darren\Documents\Professional Development\Intro to data analytics UCD\Assignment\AnnualTicketSales.csv')
print(df.head())
print(df.shape)
print(df.info())


# Importing data from an IMDB API (JSON) related to their top 250 movies and converting it into a Pandas DataFrame.
import pandas as pd
import requests
url = 'https://imdb-api.com/en/API/Top250Movies/k_52mnkeby'
r = requests.get(url)
text = r.text
json_data = r.json()

df1 = pd.DataFrame(json_data)
print(df1.head())


# Importing data into Python by scraping the web and parsing it/prettifying it.
from bs4 import BeautifulSoup
import requests
url = 'https://www.empireonline.com/movies/features/best-movies-2021/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html.parser")
pretty_soup = soup.prettify()
print(pretty_soup)