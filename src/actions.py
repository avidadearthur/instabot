from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import functools

def _keep_id(func):
    @functools.wraps(func)
    def wrapper_decorator(self, *args, **kwargs):
        """
        Switches to new window saving the session id
        and opening a dummy browser.

        https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
        https://realpython.com/primer-on-python-decorators/#decorating-classes

        """
        # Open new window after login
        if func.__name__ == "login":
            value = func(self, *args, **kwargs)

        
        url = self.browser.command_executor._url 
        session_id = self.browser.session_id

        browser = webdriver.Remote(command_executor=url,desired_capabilities={})
        browser.close()
        browser.session_id = session_id
        if func.__name__ == "login":
            browser.get('https://www.instagram.com/')

        # Open new window before calling function
        if func.__name__ != "login":
            value = func(self, *args, **kwargs)

        return value
    return wrapper_decorator

class Instactions:
    """
    Handles the Instagram actions through a the
    current driver that is supporting browser navigation.

    :Args:
    - browser: An webdriver object, command name
    - username: A str, command name
    - password: A str, command name

    :Usage:
        Instactions('<webdriver>', '<user_username>', '<user_password>')

    """
    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password

    @_keep_id
    def login(self):
        """
        Fills Instagram login form and goes to users's feed

        """
        self.browser.get('https://www.instagram.com/accounts/login/')

        try:
            username_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
            )
            password_input = self.browser.find_element_by_css_selector("input[name='password']")

            username_input.send_keys(self.username)
            password_input.send_keys(self.password)

        except TimeoutException:
            print('Timed out waiting for page to load')

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        # Look for error elements    
        errors = self.browser.find_elements_by_css_selector("#error_message")
        assert len(errors) == 0
    
    @_keep_id
    def access_feed(self):
        self.browser.get('https://www.instagram.com/')

    def close_popup(self):
        """
        Get rid of the first pop up on the Instagram feed page.

        """
        try:
            esc_popup = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
            )
            esc_popup.click()

        except TimeoutException:
            print('Timed out waiting for page to load')

    @_keep_id
    def get_followers(self, username, num=None):
        """
        Handles the Instagram actions through a the
        current driver that is supporting browser navigation.

        :Args:
        - username: A str, username of whom the list will be made
        - max: An int, max size of list

        :Usage:
            Instactions('<user_username>', '<max_list_size>')

        :Returns:
            List of followers of the selected user

        https://stackoverflow.com/questions/47211939/scroll-down-list-instagram-selenium-and-python/50313947

        """
        self.browser.get('https://www.instagram.com/' + username)
        followers_link = self.browser.find_element_by_css_selector('ul li a')

        followers_link.click()
        try:
            followers_list = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role=\'dialog\'] ul"))
            )
            followers_list.click()

        except TimeoutException:
            print('Timed out waiting for page to load')

        length = self.browser.execute_script("return (document.getElementsByTagName('ul')[2]).getElementsByTagName('li').length")

        while True:
            last_length = length
            index = length - 1
            sleep(2)
            self.browser.execute_script("(document.getElementsByTagName('ul')[2]).getElementsByTagName('li')[arguments[0]].scrollIntoView(true)", index)
            sleep(2)
            length = self.browser.execute_script("return (document.getElementsByTagName('ul')[2]).getElementsByTagName('li').length")

            if last_length == length or length > num:
                break
            
        followers = []
        for user in followers_list.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == num):
                break
        return followers


