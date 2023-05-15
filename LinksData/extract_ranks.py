import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read the list of links from the file into a Python list
with open('colleges_links_engineering.txt', 'r') as f:
    links = f.read().splitlines()

# # Initialize an empty list to store the data
all_data = []


i = 0 
# Loop through each link in the list
for link in links:
    
    # Send an HTTP GET request to the link
    print(link)
    response = requests.get(link)
    # Parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    
    # Find the table(s) in the HTML
    tables = soup.find_all('table')




    # Loop through each table in the HTML
    for table in tables:
        # Extract the headers from the table
        headers = [th.text.strip() for th in table.find_all('th')]

        # Extract the data from the table
        rows = []
        for tr in table.find_all('tr'):
            row = [td.text.strip() for td in tr.find_all('td')]
            if row:
                rows.append(row)

    
    print(headers)
    # print(rows)

    # print("\n")
    # print("\n")
    print("\n")
    print("\n")
    
    

    i=i+1 
    if i == 4:
        break
    
    
        
        # # Store the extracted data in a pandas DataFrame
        # data = pd.DataFrame(rows, columns=headers)
        
        # # Append the data to the all_data list
        # all_data.append(data)

# # Concatenate all the dataframes in the list into a single dataframe
# final_data = pd.concat(all_data, ignore_index=True)

# # Print the final dataframe
# print(final_data)

print("final")

# # Find all h3 elements in the HTML
# h3_tags = soup.find_all("h3",{"dir": "ltr"})

# # Extract the text content of each h3 element
# h3_headings = [h3.text for h3 in h3_tags]

# # Print the list of h3 headings
# for head in h3_headings:
#         print(head)




