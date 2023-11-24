# Program: get_links.py
# Takes a website URL as input.
# Fetches the content of the webpage using requests.
# Parses the HTML content using BeautifulSoup.
# Extracts all unique links (that start with 'http') from the page.
# Writes these links to a CSV file named 'links_saved.csv'.


import requests
from bs4 import BeautifulSoup
import csv

def scrape_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        links = set()  # Using a set to avoid duplicate links

        # Find all anchor tags and extract href attributes
        for tag in soup.find_all('a', href=True):
            link = tag['href']
            # Filter out unwanted links and duplicates
            if link.startswith('http') and link not in links:
                links.add(link)

        # Write the links to a CSV file
        with open('links_saved.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for link in links:
                writer.writerow([link])

        print(f"Links extracted successfully and saved to 'links_saved.csv'.")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Get URL input from user
url_input = input("Enter the website URL: ")
scrape_links(url_input)
