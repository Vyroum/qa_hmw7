from zipfile import ZipFile
from pypdf import PdfReader
from io import BytesIO
from io import TextIOWrapper
from openpyxl import load_workbook
import csv
import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "Files")


def test_create_zip_file(zip_name="test.zip", directory=FILES_DIR):
    if os.path.exists(zip_name):
        os.remove(zip_name)

    with ZipFile(zip_name, 'w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, file_path[len(directory):])

    assert os.path.exists("test.zip")


def test_pdf_file():
    with ZipFile("test.zip", 'r') as zip_archive:
        pdf_file_archived = BytesIO(zip_archive.read("sample1.pdf"))
        content = PdfReader(pdf_file_archived)
        page = content.pages[0]
        assert "AAO-HNSF" in page.extract_text(0)


def test_xlsx_file():
    with ZipFile("test.zip", 'r') as zip_archive:
        xslx_file = load_workbook(zip_archive.open("sample2.xlsx"))
        sheet = xslx_file['Sheet1']
        assert sheet['D2'].value == "Farm subsidies"


def test_csv_file():
    with ZipFile("test.zip", 'r') as zip_archive:
        with zip_archive.open("sample2.csv", 'r') as csv_content:
            csv_process = String
            for row in reader:
                assert "Chad Bradford" in reader



