from selenium import webdriver
from time import sleep
from pages import HomePage, Feed
import os


def login_page(browser, user_username, user_password):
    home_page = HomePage(browser)
    home_page.login(user_username, user_password)

    errors = browser.find_elements_by_css_selector("#error_message")
    assert len(errors) == 0

    return

def access_feed(browser):
    Feed(browser)

    return

def main():
    username, password = os.getenv('USERNAME'), os.getenv('PASSWORD')

    # Make sure the env variables were given
    if not os.environ.get('USERNAME') or not os.environ.get('PASSWORD'):
        raise RuntimeError('\nUSERNAME or PASSWORD were not set')
    
    browser = webdriver.Chrome()
    login_page(browser, username, password)
    access_feed(browser)
    

if __name__ == '__main__':
    main()