from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

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
    
    def access_feed(self):
        """
        Switches to feed saving the homepage login session id
        and opening a dummy browser.

        https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session

        """
        url = self.browser.command_executor._url 
        session_id = self.browser.session_id

        browser = webdriver.Remote(command_executor=url,desired_capabilities={})
        browser.close()
        browser.session_id = session_id
        browser.get('https://www.instagram.com/')

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



