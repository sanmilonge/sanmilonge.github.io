import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
    
        response.raise_for_status()
   
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = soup.find_all('h2')

        if not articles:
            print("No articles found.")
            return

        for i, article in enumerate(articles, start=1):
            title_tag = article.find('a')
            if title_tag and title_tag.text:
                title = title_tag.text.strip()  
                link = title_tag['href']        
                print(f"{i}. Title: {title}")
                print(f"   Link: {link}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

