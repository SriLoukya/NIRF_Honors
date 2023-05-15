import requests
from bs4 import BeautifulSoup
import os 
import PyPDF2

filename={}
code_institute={}
csvs = os.listdir("2022/")
for x in csvs :
        filename[f"2022/{x}"]=x
        
for file in filename.keys() :
   
    # if not file.startswith("IR-E-C-1412") :
    #     continue
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = read_pdf.pages
    page = read_pdf.pages[0]
    page_content = page.extract_text()
    #print(page_content.encode('utf-8'))
    text=page_content.split(" ")
    print(file)
    name=''
    for i in range(15) :
        # print(text)
        # print(text[16+i])
        if text[16+i]!=' ':
            if text[16+i][0] == '[' :
                code=text[16+i].split(']')
                _,institute_code=code[0].split('[')
                #print(institute_code)
                break
            name=name+text[16+i]+'_'
    oldname=institute_code
    newname=name
    os.rename(file,f"2022/{newname}.pdf")
    #print(name)
    code_institute[institute_code]=name  