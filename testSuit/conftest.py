import pytest
from selenium import webdriver
import validators


url = input("Please enter the link of your site ")


@pytest.fixture(scope="module", autouse=True)
def browser():
    print("\nstart chrome browser for test...")
    browser = webdriver.Chrome()
    if validators.url(url):
        browser.get(url)
    else:
        print(f"The link {url} is incorrect, please enter the correct link")
    browser.maximize_window()

    yield browser
    print("\nTest completed. Quit browser..")
    browser.quit()
