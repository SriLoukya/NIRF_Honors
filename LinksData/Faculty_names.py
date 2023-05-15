import requests
from bs4 import BeautifulSoup
import certifi



file = open('college_names.txt', 'w', encoding='utf-8') 

# Define the URL to search for papers
url = "https://www.iiit.ac.in/people/faculty/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the publication titles and links in the HTML content
titles = soup.find_all("a")


# Print the titles of all the publications
for title in titles:
    print(title.text.strip())
    # file.write(title.text.strip()+"\n")

