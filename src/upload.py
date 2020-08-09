from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class Instaupload:
    """
    Handles the Instagram upload requests at the
    current driver that is supporting browser navigation.

    :Args:
    - browser: An webdriver object, command name
    - username: A str, command name
    - password: A str, command name

    :Usage:
        Instaupload('<user_username>', '<user_password>')

    """
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

        # Change driver to mobile emulation
        mobile_emulation = { "deviceName": "Nexus 5" }

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.browser = webdriver.Remote(command_executor=self.browser.command_executor._url,
        desired_capabilities = chrome_options.to_capabilities())

    
    def post_photo(self, caption=None):
        """
        Switches to android mobile viewport to allow special post requests.

        https://stackoverflow.com/questions/52864531/posting-uploading-an-image-to-instagram-using-selenium-not-using-an-api/52870733
        https://realpython.com/primer-on-python-decorators/#decorating-classes

        """

        self.browser.get('https://www.instagram.com/')

        self.browser.get('https://www.instagram.com/accounts/login/')

        sleep(2)
        self.browser.find_element_by_name("username").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password)
        sleep(3)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(5)
        self.browser.get('https://www.instagram.com/' + self.username)
        sleep(3)

        post_button = self.browser.find_elements_by_css_selector("""#react-root > section > nav.NXc7H.f11OC > div > div > div.KGiwt > div > div > div.q02Nz._0TPg""")
        post_button[0].click()
        sleep(1)
    
        form = self.browser.find_element_by_xpath("//input[@type='file']")
        form.send_keys('/Users/arthurquintao/Desktop/instabot-img/test01.jpg')
        
        try:
            next_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Next']"))
            )
            next_button.click()

            if caption != None:
                caption_area = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//textarea"))
                )
                caption_area.send_keys(caption)

                self.browser.find_element_by_xpath("//button[text()='Share']").click()

        except TimeoutException:
            print('Timed out waiting for page to load')
