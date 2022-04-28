# selenium stuff
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# email reading libraries
import poplib
import string, random
from io import StringIO
import email
import logging
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

# login info
SERVER = "pop.gmail.com"
USER = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# connecting to server
logging.debug('connecting to ' + SERVER)
server = poplib.POP3_SSL(SERVER)

# log in
logging.debug('log in')
server.user(USER)
server.pass_(PASSWORD)

# list the emails on the server
logging.debug('listing emails')
resp, items, octets = server.list()

# get the first email in the list
id, size = string.split(items[0])
resp, text, octets = server.retr(id)

# convert the list to a Message object
text = string.join(text, "\n")
file = StringIO.StringIO(text)
message = email.Message(file)

# read the message
print(message.fp.read())
