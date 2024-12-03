import pytest
import os
from zipfile import ZipFile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "files")

@pytest.fixture(scope="session", autouse=True)
def test_create_zip_file(zip_name="test.zip", directory=FILES_DIR):
    if os.path.exists(zip_name):
        os.remove(zip_name)

    with ZipFile(zip_name, 'w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, file_path[len(directory):])


    assert os.path.exists("test.zip")
    yield
    os.remove("test.zip")