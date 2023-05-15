# import requests
# from bs4 import BeautifulSoup

# # Open the file 'example.txt' for writing
# file = open('colleges_links.txt', 'w')
# url = "https://engineering.careers360.com/articles/jee-main-cutoff"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# links = []

# for link in soup.find_all("a"):
#     href = link.get("href")
#     if href and not href.startswith("#"):
#         links.append(href)


# for i in links:
#     if i.startswith("https://www.careers360.com/university/") and i.endswith("/cut-off"):
#         file.write(i)
#         print(i)

# # Close the file
# file.close()

import requests
from bs4 import BeautifulSoup

# Open the file 'colleges_links.txt' for writing
file = open('colleges_links_engineering.txt', 'w')

url = "https://engineering.careers360.com/articles/jee-main-cutoff"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
links = []

for link in soup.find_all("a"):
    href = link.get("href")
    if href and not href.startswith("#"):
        links.append(href)

for i in links:
    if i.startswith("https://engineering.careers360.com/articles/jee-main-cutoff") and i.endswith("/cut-off"):
        file.write(i + "\n")  # Add newline character at the end of each URL
        print(i)

# Close the file
file.close()

