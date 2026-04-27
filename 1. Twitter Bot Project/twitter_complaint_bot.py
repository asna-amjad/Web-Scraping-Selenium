## Twitter Complaint Bot
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import os

load_dotenv("/Users/asnaamjad/Desktop/Web Scraping/Section 51/.env")

PROMISED_DOWN = 501
PROMISED_UP = 336
CHROME_DRIVER_PATH = "/opt/homebrew/bin/chromedriver"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


if not TWITTER_USERNAME or not TWITTER_PASSWORD:
    raise ValueError("Environment variables not loaded!")

# Create a class 
class InternetSpeedTwitterBot:
    def __init__(self, driver_path):    # In the init() method, create the Selenium driver and 2 other properties down and up
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    # Create two methods 
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        # self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]').click()

        sleep(40)

        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print(f"Download = {self.down} Mbps")
        print(f"Up = {self.up} Mbps")
        sleep(2)
        bot.tweet_at_provider()
        #pass

    def tweet_at_provider(self):
        #self.driver.maximize_window()
        self.driver.get("https://x.com/i/flow/login")

        wait = WebDriverWait(self.driver, 20)

        # 1. Email input
        email_input = wait.until(ec.element_to_be_clickable((By.NAME, "text")))
        email_input.send_keys(TWITTER_USERNAME)
        # Click Next (more reliable than ENTER)
        
        next_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
        next_button.click()
        sleep(5)

       # Step 2: Username verification (THIS IS YOUR CASE)
        try:
            username_input = wait.until(ec.element_to_be_clickable((By.NAME, "text")))
            
            # Important: check placeholder text to confirm it's username step
            if "phone" in username_input.get_attribute("outerHTML").lower():
                print("Username step detected")
            
            username_input.send_keys(TWITTER_USERNAME)  # ✅ FIXED
            username_input.send_keys(Keys.ENTER)

            sleep(5)
        
        except:
            print("No username step")


        # Password input
        password_input = wait.until(ec.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        sleep(5)


        tweet_box = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Post text']")))

        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} Mbps Down/{self.up} Mbps Up when I pay for {PROMISED_DOWN} Mbps Down/{PROMISED_UP} Mbps Up?")

        # tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div')
        # tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} Mbps Down/{self.up} Mbps Up when I pay for {PROMISED_DOWN} Mbps Down/{PROMISED_UP} Mbps Up?")
        # sleep(5)

        post_button = wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Post']")))
        post_button.click()
        
        # self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]').click()
        sleep(2)
        self.driver.quit()

# initialize object and call two methods in order
bot = InternetSpeedTwitterBot(driver_path=CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


