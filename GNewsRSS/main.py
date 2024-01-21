import feedparser
import sys
import urllib.parse
import requests

def display_news_with_query(query):
    max_results = 10
    url = f'https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    feed = feedparser.parse(response.text)
    
    sorted_entries = sorted(feed.entries, key=lambda entry: entry.published_parsed, reverse=True)
    
    print('Feed Link:', feed.feed.link)
    print('Number of items:', len(feed.entries))
    print()
    
    for entry in sorted_entries[:max_results]:
        print(f"Title: {entry.title}")
	    #print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print("--------------")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Missing search parameter.")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:]).replace(" ", "+")
    display_news_with_query(query)


#https://news.google.com/rss?hl=<LANGUAGE_CODE>&gl=<COUNTRY_CODE>&ceid=<COUNTRY_CODE>:<LANGUAGE_CODE>
#https://news.google.com/rss/search?q='+query+'&hl=en-IN&gl=IN&ceid=IN:en
