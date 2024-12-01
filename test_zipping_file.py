import os.path
import time
from zipfile import ZipFile
import pypdf
import openpyxl
import selene
import requests
from selene import browser, query, by

from conftest import FILES_DIR

def test_downloading_files():
    browser.open("/formats/xlsx")
    xlsx_download_link = browser.element("[href='/samples/document/xlsx/sample2.xlsx']").get(query.attribute("href"))
    xlsx_content = requests.get(url=xlsx_download_link).content
    time.sleep(2)
    with open(os.path.join(FILES_DIR, "xlsx_sample.xlsx"), "wb") as xlsx_file:
        xlsx_file.write(xlsx_content)

    browser.open("/formats/pdf")
    pdf_download_link = browser.element("[href='/samples/document/pdf/sample2.pdf']").get(query.attribute("href"))
    pdf_content = requests.get(url=pdf_download_link).content
    time.sleep(2)
    with open(os.path.join(FILES_DIR, "pdf_sample.pdf"), "wb") as pdf_file:
        pdf_file.write(pdf_content)

    browser.open("/formats/csv")
    csv_download_link = browser.element("[href='/samples/document/csv/sample2.csv']").get(query.attribute("href"))
    csv_content = requests.get(url=csv_download_link).content
    time.sleep(2)
    with open(os.path.join(FILES_DIR, "csv_sample.csv"), "wb") as csv_file:
        csv_file.write(csv_content)

