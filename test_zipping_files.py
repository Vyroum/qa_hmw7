from zipfile import ZipFile
from pypdf import PdfReader
from io import BytesIO, StringIO
from openpyxl import load_workbook
import csv



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
        data = StringIO(zip_archive.read("sample2.csv").decode('utf-8'))
        data_converted = csv.reader(data, delimiter=',')
        list(zip(*data_converted))
        for _ in data_converted:
            for row in data_converted:
                assert "Daniel Cabrera" in row


