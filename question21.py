import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'


response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('h2')
    
with open('content.txt', 'w', encoding='utf-8') as file:
    for article in articles:
        file.write(article.get_text().strip() + '\n')

print("Content has been written to 'content.txt'.")
