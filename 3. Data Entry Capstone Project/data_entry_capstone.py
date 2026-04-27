## Data Entry Capstone Project (Web Scraping)

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/opt/homebrew/bin/chromedriver"

# Create empty lists
zillow_link =[]
zillow_address = []
zillow_price = []

website = "https://appbrewery.github.io/Zillow-Clone/"

r = requests.get(website)
soup = BeautifulSoup(r.content, "html.parser")
property_list = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")  

# for loop to go through each link on zillow page
for item in property_list:
    address_tag = item.find("div").find("a")   
    address = address_tag.text.strip()
    final_address = " ".join(address.replace("|", "").split())
    zillow_address.append(final_address)

    link = address_tag["href"]
    zillow_link.append(link)

    price = item.find("span", class_="PropertyCardWrapper__StyledPriceLine").text.strip().split("/")[0].split("+")[0]
    zillow_price.append(price)

chrome_options = webdriver.ChromeOptions()                  # This creates a configuration object where you can customize how Chrome launches
chrome_options.add_experimental_option("detach", True)      # This tells Chrome: do NOT close the browser when the Python script finishes
driver = webdriver.Chrome(options=chrome_options)           # Opens Chrome using your custom settings


# Fill out Google Form with Responses from lists
for fill in range(len(zillow_link)):
    driver.get("https://forms.gle/Fgp1pewMdQ5Pk8gf9")
    time.sleep(2)

    property_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # sumbit response
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")

    property_address.send_keys(zillow_address[fill])
    property_price.send_keys(zillow_price[fill])
    property_link.send_keys(zillow_link[fill])
    submit_button.click()

    # fill out another response
    another_response = driver.find_element(By.LINK_TEXT, "Submit another response").click()

print("Google form Reponses filled successfully")
