import requests
from bs4 import BeautifulSoup
import os 
import PyPDF2
# import pandas as pd
# Make a request to the HTML page
response = requests.get("https://www.nirfindia.org/2022/EngineeringRanking.html")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all links in the HTML page
links = soup.find_all("a")

# Iterate over the links and download PDFs
for link in links:
    href = link.get("href")
    print(href)
    if href is not None and href.startswith("https://www.nirfindia.org/nirfpdfcdn/2022/pdf/") and href.endswith(".pdf"):
        # Make a request to the PDF URL and save the file
        response = requests.get(href)
        filename="2022/"+href.split("/")[-1]
        with open(filename, "wb") as f:
            f.write(response.content)

# filename={}
# code_institute={}
# csvs = os.listdir("2022/")
# for x in csvs :
#         filename[f"2022/{x}"]=x
        
# for file in filename.keys() :
#     if file.startswith("IR-E-C-1262") :
#         continue
#     pdf_file = open(file, 'rb')
#     read_pdf = PyPDF2.PdfReader(pdf_file)
#     number_of_pages = read_pdf.pages
#     page = read_pdf.pages[0]
#     page_content = page.extract_text()
#     #print(page_content.encode('utf-8'))
#     text=page_content.split(" ")
    
#     name=''
#     for i in range(15) :
#         print(text)
#         if text[16+i][0] == '[' :
#             code=text[16+i].split(']')
#             _,institute_code=code[0].split('[')
#             #print(institute_code)
#             break
#         name=name+text[16+i]+'_'
#     oldname=institute_code
#     newname=name
#     os.rename(f"2022/{oldname}.pdf",f"2022/{newname}.pdf")
#     #print(name)
#     code_institute[institute_code]=name  