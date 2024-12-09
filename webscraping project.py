import requests
from bs4 import BeautifulSoup

# requires the user to enter a url of their choosing
url = input('Enter a URL: ')

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find all of the headings and return as titles
    titles = soup.find_all('h2')

    # recognizes and prints each title
    for index, title in enumerate(titles, start=1):
        print(f'{index}. {title.get_text(strip=True)}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

