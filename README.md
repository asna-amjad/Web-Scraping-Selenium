# Web Scraping using Selenium

**This repository focuses on web scraping, extracting data from websites using Selenium in Python.**

## 1. Internet Speed & Twitter Complaint Bot - Automation Project

Internet Speed Twitter Bot

### Description

This project is a Python-based automation bot that checks internet speed using Speedtest and automatically posts a complaint on Twitter (X) if the speed is lower than the promised values. It demonstrates browser automation, dynamic data extraction, and interaction with real-world web applications.

### Features

* Checks internet speed (download & upload) using Speedtest
* Automates login process on Twitter (X)
* Handles multi-step authentication (username + password flow)
* Extracts real-time internet speed data
* Compares actual speed with promised speed
* Automatically posts a complaint tweet
* Uses environment variables for secure credential handling

### Tech Stack

* Python
* Selenium
* WebDriverWait (Explicit Waits)
* ChromeDriver
* python-dotenv

### How It Works

* Launches browser using Selenium WebDriver
* Navigates to Speedtest website and starts test
* Extracts download and upload speed results
* Handles login flow on X (Twitter)
* Enters credentials securely using environment variables
* Navigates to tweet composer
* Generates a dynamic complaint message using speed data
* Posts the tweet automatically

### Output

Prints internet speed (Download & Upload) in the console Automatically posts a complaint tweet on Twitter (X) including: 
Actual internet speed.
Promised internet speed
Complaint message to the provider


## 2. Instagram Follower Bot - Automation Project

### Description

This project is a Python-based automation bot that logs into Instagram, navigates to a target account, opens the followers list, and automatically follows users. It demonstrates browser automation, handling dynamic elements, and interacting with modal-based UI components.

### Features

* Automates Instagram login process
* Navigates to a target account’s followers list
* Handles pop-ups like “Save Login Info” and notifications
* Extracts and interacts with dynamically loaded follower elements
* Automatically clicks “Follow” buttons
* Implements scrolling through follower modal
* Performs repeated follow actions using loops
* Handles click interruptions and UI exceptions

### Tech Stack

* Python
* Selenium
* WebDriverWait (Explicit Waits)
* ChromeDriver

### How It Works

* Launches browser using Selenium WebDriver
* Logs into Instagram using provided credentials
* Handles post-login prompts (Save Info, Notifications)
* Navigates to the target account profile
* Opens followers list modal
* Identifies all “Follow” buttons on the page
* Clicks follow buttons in a loop
* Repeats process with scrolling to load more users
* Handles potential click interception errors

### Output

The bot:
* Logs into Instagram automatically
* Opens followers list of the target account
* Follows multiple users from the list
* Automates repetitive follow actions without manual effort


## 3. Data Entry Automation - Web Scraping Project

Zillow Data Entry Bot

### Description

This project is a Python-based automation script that scrapes property data (address, price, and links) from a Zillow clone website and automatically fills out a Google Form with the collected data. It demonstrates end-to-end automation combining web scraping and browser interaction.

### Features

* Scrapes property listings from a website
* Extracts addresses, prices, and property links
* Cleans and formats raw data (removes symbols and extra text)
* Stores data in structured Python lists
* Automates Google Form submission
* Submits multiple entries using a loop
* Performs end-to-end data pipeline automation

### Tech Stack

* Python
* Requests
* BeautifulSoup
* Selenium
* ChromeDriver
* Pandas (for data handling)

### How It Works

* Sends HTTP request to the website
* Parses HTML using BeautifulSoup
* Extracts property address, price, and link
* Cleans and formats extracted data
* Stores data in lists
* Launches browser using Selenium WebDriver
* Opens Google Form and fills form fields with scraped data
* Submits the form automatically and repeats process for all property listings

### Output

The script:
Collects property data (Address, Price, Link)
Automatically fills and submits Google Form responses
Creates multiple form entries corresponding to scraped listings
