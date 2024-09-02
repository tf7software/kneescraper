import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse
import re
from tqdm import tqdm
import sys
import random

def get_page_links(base_url):
    """Fetch all links from the base URL."""
    links = set()
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                links.add(full_url)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return links

def extract_emails(text):
    """Extract emails from text."""
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def extract_phone_numbers(text):
    """Extract phone numbers from text."""
    return re.findall(r'\+?\d[\d -]{8,}\d', text)

def extract_numbers(text):
    """Extract sequences of numbers from text."""
    return re.findall(r'\b\d+\b', text)

def find_pages_with_keywords(links, keywords, extract_option):
    """Find pages with titles or content containing specific keywords."""
    result = []
    for link in tqdm(links, desc="Processing", unit="link"):
        try:
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else ''
            body = soup.get_text()
            if any(keyword.lower() in title.lower() for keyword in keywords):
                entry = {'url': link, 'title': title}
                if extract_option:
                    if extract_option == 'emails':
                        entry['emails'] = ', '.join(extract_emails(body))
                    elif extract_option == 'phone':
                        entry['phone_numbers'] = ', '.join(extract_phone_numbers(body))
                    elif extract_option == 'numbers':
                        entry['numbers'] = ', '.join(extract_numbers(body))
                result.append(entry)
        except requests.RequestException as e:
            print(f"Request failed for {link}: {e}")
        except Exception as e:
            print(f"Error processing {link}: {e}")
        if stop_flag[0]:
            break
    return result

def find_random_pages(links, num_entries):
    """Find a specified number of random pages from the list of links."""
    return random.sample(links, min(len(links), num_entries))

def main():
    global stop_flag
    stop_flag = [False]

    base_url = input("Enter the base domain URL: ").strip()
    keywords = input("Enter keywords to search for (comma-separated) or leave blank: ").strip()
    keywords = [kw.strip() for kw in keywords.split(',')] if keywords else []
    num_entries = int(input("Enter the number of entries to search for (10-1000): ").strip())
    extract_option = input("Do you want to extract emails, phone numbers, or strings of numbers? (Enter 'emails', 'phone', 'numbers', or leave blank for none): ").strip()

    if extract_option not in ['', 'emails', 'phone', 'numbers']:
        print("Invalid extraction option. Exiting.")
        return

    print("Starting the scraping process. Type '*FIN' to stop early.")
    links = get_page_links(base_url)
    
    if keywords:
        pages = find_pages_with_keywords(links, keywords, extract_option)
    else:
        pages = [{'url': url} for url in find_random_pages(links, num_entries)]

    if len(pages) > num_entries:
        pages = pages[:num_entries]
    
    df = pd.DataFrame(pages)
    df.to_csv('scraped_pages.csv', index=False)
    print(f"Results saved to scraped_pages.csv")

    # Listen for early stop input
    while True:
        user_input = input()
        if user_input.strip() == "*FIN":
            stop_flag[0] = True
            break

    # If the script was stopped early, save the collected data
    if stop_flag[0]:
        df = pd.DataFrame(pages)
        df.to_csv('scraped_pages.csv', index=False)
        print(f"Process stopped early. Results saved to scraped_pages.csv")

if __name__ == '__main__':
    main()
