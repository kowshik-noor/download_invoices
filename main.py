# selenium stuff
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# gmail program
from quickstart import main
# loading from the .env file
import os
from dotenv import load_dotenv
load_dotenv()

# get the chromedriver running \
# service = Service(executable_path=os.getenv('LOCATION'))
# driver = webdriver.Chrome(service=service)

# # go to the link to get the invoices
# driver.get(os.getenv('LINK'))
# driver.implicitly_wait(5)

# # enter my email
# email = driver.find_element(By.ID, 'email')
# email.send_keys(os.getenv('EMAIL'), Keys.ENTER)
# after pressing enter, a login link will be sent to my email