import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=['Clg_Name', 'Year', 'Branch', 'Category', 'Open_Rank', 'Close_Rank'])

# link = "https://engineering.careers360.com/articles/jee-main-cutoff-for-nit-calicut"

with open('colleges_links_engineering.txt', 'r') as f:
    links = f.read().splitlines()

for link in links:
    
    clg_name = link.removeprefix("https://engineering.careers360.com/articles/jee-main-cutoff-for-")
    print(clg_name)
    
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')


    tables = soup.find_all('table')

    table_2022 = tables[0]

    # Extract the headers from the table
    headers = [th.text.strip() for th in table_2022.find_all('th')]

    # Extract the data from the table
    rows = []
    branch = ""
    for tr in table_2022.find_all('tr'):
        row = [td.text.strip() for td in tr.find_all('td')]
        if len(row) < 4:
            continue
        # print(row)
        # print("\n")
        if len(row) == 6:
            branch = row[0]
            
            if row[2].isnumeric() and row[3].isnumeric():
                data = pd.DataFrame({'Clg_Name':[clg_name],
                        'Year':[2022],
                        'Branch': branch,
                        'Category': [row[1]],
                        'Open_Rank': [row[2]],
                        'Close_Rank': [row[3]]
                    })
                df = df._append(data)
        else:
                    
            if row[1].isnumeric() and row[2].isnumeric():
                data = pd.DataFrame( {'Clg_Name':[clg_name],
                        'Year':[2022],
                        'Branch': branch,
                        'Category': [row[0]],
                        'Open_Rank': [row[1]],
                        'Close_Rank': [row[2]]
                    })
                df = df._append(data)

print(df)
df.to_csv('ranks.csv', index=False)


