from selenium import webdriver
from time import sleep
import os
from actions import Instactions

def main():
    user_username, user_password = os.getenv('USERNAME'), os.getenv('PASSWORD')

    # Make sure the env variables were given
    if not os.environ.get('USERNAME') or not os.environ.get('PASSWORD'):
        raise RuntimeError('\nUSERNAME or PASSWORD were not set')
    
    browser = webdriver.Chrome()
    instactions = Instactions(browser, user_username, user_password)

    instactions.login()
    instactions.access_feed()
    instactions.close_popup()
       

if __name__ == '__main__':
    main()