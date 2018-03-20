#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--password-store=basic')
options.binary_location = "/path/to/exec/chromium-browser"
browser = webdriver.Chrome(chrome_options=options)
browser.get("url/to/Discord")

try:
	email_textEdit = WebDriverWait(browser,10).until(
		EC.presence_of_element_located((By.ID,"emailID"))
	)
#email_textEdit = browser.find_element_by_id("register-email")
	email_textEdit.send_keys("emailAddressorUsername")
	password_textEdit = browser.find_element_by_id("passwordID")
	password_textEdit.send_keys("")#Put cursor here
finally:
	print("Logged onto Discord...")


