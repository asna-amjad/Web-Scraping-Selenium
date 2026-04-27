# Web Scraping using Selenium

**This repository focuses on web scraping, extracting data from websites using Selenium in Python.**

## 1. Internet Speed & Twitter Complaint Bot - Automation Project

Internet Speed Twitter Bot

### Description

This project is a Python-based automation bot that checks internet speed using Speedtest and automatically posts a complaint on Twitter (X) if the speed is lower than the promised values. It demonstrates browser automation, dynamic data extraction, and interaction with real-world web applications.

### Features

Checks internet speed (download & upload) using Speedtest
Automates login process on Twitter (X)
Handles multi-step authentication (username + password flow)
Extracts real-time internet speed data
Compares actual speed with promised speed
Automatically posts a complaint tweet
Uses environment variables for secure credential handling

### Tech Stack

Python
Selenium
WebDriverWait (Explicit Waits)
ChromeDriver
python-dotenv

### How It Works

Launches browser using Selenium WebDriver
Navigates to Speedtest website and starts test
Extracts download and upload speed results
Opens Twitter (X) login page
Handles login flow including optional username verification step
Enters credentials securely using environment variables
Navigates to tweet composer
Generates a dynamic complaint message using speed data
Posts the tweet automatically

### Output

The bot:

Prints internet speed (Download & Upload) in the console Automatically posts a complaint tweet on Twitter (X) including: Actual internet speed.

Promised internet speed
Complaint message to the provider
