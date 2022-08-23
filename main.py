import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.<NAME OF BROWSER>.service import Service

WEB_DRIVER_PATH = <PATH TO YOUR DESIRED WEB DRIVER>
INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"

SIMILAR_ACCOUNT = <USERNAME OF THE ACCOUNT WHOSE FOLLOWERS YOU WISH TO FOLLOW>
USERNAME = <YOUR USERNAME>
PASSWORD = <YOUR PASSWORD>

class InstaFollowerBot:
    def __init__(self):
        # Initialising web driver
        self.web_driver_service = Service(executable_path=WEB_DRIVER_PATH)
        self.driver = webdriver.<NAME OF BROWSER>(service=self.web_driver_service)
        self.driver.maximize_window()
        self.driver.get(INSTAGRAM_URL)

    def login(self):
        while True:
            try:
                # Username field
                username_field_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
                username_field_box = self.driver.find_element(By.XPATH, username_field_xpath)
                username_field_box.click()
                username_field_box.send_keys(USERNAME)
                # Password field
                password_field_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
                password_field = self.driver.find_element(By.XPATH, password_field_xpath)
                password_field.click()
                password_field.send_keys(PASSWORD)
                # Login button
                login_button_xpath = '//*[@id="loginForm"]/div/div[3]/button/div'
                login_button = self.driver.find_element(By.XPATH, login_button_xpath)
                login_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                save_info_not_now_xpath = '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button'
                save_info_not_now_button = self.driver.find_element(By.XPATH, save_info_not_now_xpath)
                save_info_not_now_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                close_popup_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'
                close_popup = self.driver.find_element(By.XPATH, close_popup_xpath)
                close_popup.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

    def find_followers(self):
        time.sleep(2)
        while True:
            try:
                search_box_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div'
                search_box = self.driver.find_element(By.XPATH, search_box_xpath)
                search_box.click()
                input_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input'
                input_box = self.driver.find_element(By.XPATH, input_xpath)
                input_box.send_keys(SIMILAR_ACCOUNT)
                time.sleep(5)
                input_box.send_keys(Keys.ENTER)
                time.sleep(1)
                input_box.send_keys(Keys.ENTER)
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                followers_count_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div'
                followers_count = self.driver.find_element(By.XPATH, followers_count_xpath)
                followers_count.click()
                time.sleep(1)
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
                for i in range(10):
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                    time.sleep(2)
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

    def follow(self):
        while True:
            try:
                all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
                for button in all_buttons:
                    try:
                        button.click()
                        time.sleep(1)
                    except ElementClickInterceptedException:
                        cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                        cancel_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break


bot = InstaFollowerBot()
bot.login()
bot.find_followers()
bot.follow()
