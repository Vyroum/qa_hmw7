import shutil

from selene import browser
from selenium import webdriver
import pytest
import os

if not os.path.exists("files"):
    os.mkdir("files")


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "files")

@pytest.fixture(scope='session', autouse=True)
def open_browser():
    driver_options = webdriver.ChromeOptions()

    prefs = {"download.default_directory": FILES_DIR,
    "download.prompt_for_download": False}
    driver_options.add_experimental_option("prefs", prefs)
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://filesamples.com'
    # browser.config.headless = True
    yield
    shutil.rmtree(FILES_DIR)
    browser.quit()