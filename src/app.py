from selenium import webdriver
from time import sleep
from pages import LoginPage, FeedPage
import os


def login(browser, user_username, user_password):
    login_page = LoginPage(browser)
    login_page.login(user_username, user_password)

    errors = browser.find_elements_by_css_selector("#error_message")
    assert len(errors) == 0

    feed = FeedPage(browser)
    feed.access_feed(browser)
    feed.close_popup()

    sleep(5)

    return

def main():
    username, password = os.getenv('USERNAME'), os.getenv('PASSWORD')

    # Make sure the env variables were given
    if not os.environ.get('USERNAME') or not os.environ.get('PASSWORD'):
        raise RuntimeError('\nUSERNAME or PASSWORD were not set')
    
    browser = webdriver.Chrome()
    login(browser, username, password)
    

if __name__ == '__main__':
    main()