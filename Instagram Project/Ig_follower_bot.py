### Instagram Follower Bot Project

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException

# STEP 1 - Get your Instagram Credentials
SIMILAR_ACCOUNT = "katieleathley"
USERNAME = "my_username"
PASSWORD = "my_password"
CHROME_DRIVER_PATH = "/opt/homebrew/bin/chromedriver"

# STEP 2 - Create a Class
class InstaFollower:
    def __init__(self, driver_path):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()                  # This creates a configuration object where you can customize how Chrome launches
        chrome_options.add_experimental_option("detach", True)      # This tells Chrome: do NOT close the browser when the Python script finishes
        self.driver = webdriver.Chrome(options=chrome_options)      # Opens Chrome using your custom settings

    # Create three methods login(), find_followers(), and follow()
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        wait = WebDriverWait(self.driver, 20)

        # 1. username input
        username_input = wait.until(ec.presence_of_element_located((By.NAME, "email")))
        username_input.send_keys(USERNAME)
        # 2. password input
        password_input = wait.until(ec.presence_of_element_located((By.NAME, "pass")))
        password_input.send_keys(PASSWORD)

        password_input.send_keys(Keys.ENTER)
        sleep(4)

        # Savie login Info - "Not Now"
        save_login = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login:
            save_login.click()
        sleep(1)

        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        wait = WebDriverWait(self.driver, 20)

        followers_link = wait.until(ec.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{SIMILAR_ACCOUNT}/followers')]")))
        followers_link.click()

        modal = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        #modal = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        #modal = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     sleep(2)

    def follow(self):
        wait = WebDriverWait(self.driver, 10)

        for i in range(5):
            buttons = self.driver.find_elements(By.XPATH, "//button")
            for button in buttons: # Do scroll and follow process 5 times (5 iterationss of this loop)
                try:
                    if button.text == "Follow":
                        button.click()
                        sleep(1)
                except:
                    pass

            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")      # This scrolls the page all the way down
            #wait.until(ec.presence_of_element_located((By.XPATH, "//button")))                 # This is a stability pause after scrolling 
            
        ### -------- This block of Code not working ------- ###
            # except ElementClickInterceptedException:
            #     try:
            #         self.driver.find_element(By.XPATH, "//button[contains(text(),'Cancel') or contains(text(),'Not Now')]").click()
            #     except:
            #         pass

# initialize object and call two methods in order
bot = InstaFollower(driver_path=CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
