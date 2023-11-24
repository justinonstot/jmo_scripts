# Example usage
# parse_csv('input.csv', 'urls_parsed.csv')


import csv
from urllib.parse import urlparse

def extract_tld(url):
    """
    Extract the top-level domain from a URL.
    """
    try:
        parsed_url = urlparse(url)
        # Extract the domain and strip 'www.'
        domain = parsed_url.netloc.split('www.')[-1]
        return domain
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
        return None

def parse_csv(input_file, output_file):
    """
    Parse URLs from the input CSV file and save TLDs to the output CSV file.
    """
    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row:  # Check if row is not empty
                url = row[0]
                tld = extract_tld(url)
                if tld:
                    writer.writerow([tld])

        print(f"TLDs have been extracted and saved to '{output_file}'.")

