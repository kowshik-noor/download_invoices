import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()

# get the chromedriver running \
service = Service(executable_path=os.getenv('LOCATION'))
driver = webdriver.Chrome(service=service)

# go to the link to get the invoices
driver.get(os.getenv('LINK'))

# enter my login info using my email
