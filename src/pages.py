from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage:
    """
    Handles the Instagram homepage through a the.
    current driver that is supporting browser navigation.

    """

    def __init__(self, browser):
        self.browser = browser
        browser.get('https://www.instagram.com/accounts/login/')

    def login(self, username, password):
        """
        Fills Instagram login form get returned result.

        :Args:
         - username: A str, command name
         - password: A str, command name

        :Usage:
            Homepage.login('<user_username>', '<user_password>')

        :Returns:
            User's instagram feed.

        """
        try:
            username_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
            )
            password_input = self.browser.find_element_by_css_selector("input[name='password']")
            username_input.send_keys(username)
            password_input.send_keys(password)

        except TimeoutException:
            print('Timed out waiting for page to load')

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()


class FeedPage:
        """
        Handles the Instagram feed through a the.
        current driver that is supporting browser navigation.

        """
        def __init__(self, browser):
            self.browser = browser

        def access_feed(self, browser):
            """
            Switches to feed saving the homepage login session id
            and opening a dummy browser.

            https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session

            """
            url = browser.command_executor._url 
            session_id = browser.session_id
            browser = webdriver.Remote(command_executor=url,desired_capabilities={})
            browser.close()
            browser.session_id = session_id
            self.browser.get('https://www.instagram.com/')

        def close_popup(self):
            # Get rid of the first
            # pop up on the Instagram feed page.
            try:
                esc_popup = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
                )
                esc_popup.click()

            except TimeoutException:
                print('Timed out waiting for page to load')              