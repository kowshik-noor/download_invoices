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
# delayed task functionality
from time import sleep


# i couldn't get my code to successfully retrieve a login link, so i'll hardcode it

# check if we have a login link
# otherwise, get the login link
# if os.getenv("LOGIN_LINK") != "":
#     login_link = os.getenv('LOGIN_LINK')
# else:
    # # get the chromedriver running 
    # service = Service(executable_path=os.getenv('LOCATION'))
    # driver = webdriver.Chrome(service=service)

    # # go to the link that will take us to the sign in page
    # driver.get(os.getenv('LINK'))
    # driver.implicitly_wait(5)

#     # enter my email
#     email = driver.find_element(By.ID, 'email')
#     email.send_keys(os.getenv('EMAIL'), Keys.ENTER)
#     # after pressing enter, a login link will be sent to my email

#     # after a 60 secs, run the email scraping function in quickstart
#     sleep(60)
#     login_link = main()
#     os.environ["LOGIN_LINK"] = login_link

# print(login_link)

def login():
    # get the chromedriver running 
    service = Service(executable_path=os.getenv('LOCATION'))
    driver = webdriver.Chrome(service=service)

    # go to the login link that will take us to the account page
    driver.get(os.getenv('LINK'))
    driver.implicitly_wait(5)
    return driver

driver = login()