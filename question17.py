import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'

response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

news_titles = soup.find_all('h2')

print("List of Titles Found on Page:")
for title in news_titles:
    print(title.get_text().strip()) 
