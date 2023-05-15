import pdfplumber
import pandas as pd
import os
# Open the PDF file
# scan directory for pdfs

for file in os.listdir("2022/") :
    if file.endswith(".pdf") :
        filename="2022/"+file
        print(filename)
        with pdfplumber.open(filename) as pdf:
            # Create an empty list to store the tables
            all_tables = []

            # Iterate over each page
            for page in pdf.pages:
                # Extract all tables on the current page
                tables = page.extract_tables()

                # Add the tables to the all_tables list
                all_tables.extend(tables)

        # Process each table
        i=0
        for table in all_tables:
            # Do something with the table data
            print(table)
            df = pd.DataFrame(all_tables[i])
            # create directory if not exists
            if not os.path.exists("data/"+file.split(".pdf")[0]):
                # create
                os.makedirs("data/"+file.split(".pdf")[0])
            filename="data/"+file.split(".pdf")[0]+"/"
            filename += f"table_{i}.csv"
            df.to_csv(filename, index=False)
            i+=1
