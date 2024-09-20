import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.cnn.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the article elements
    articles = soup.find_all('h3', class_='cd__headline')

    # Loop through the articles and extract the titles and URLs
    for article in articles:
        # Get the article title
        title = article.get_text(strip=True)
        
        # Get the URL for the article
        link = article.find('a')['href']
        
        # Ensure the URL is complete
        if link.startswith('/'):
            link = 'https://www.cnn.com' + link
        
        # Print the title and URL
        print(f'Title: {title}')
        print(f'URL: {link}\n')

else:
    print(f'Failed to retrieve the website. Status code: {response.status_code}')
