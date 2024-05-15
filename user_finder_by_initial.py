from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import re
import time
load_dotenv()

login_url = 'https://lspd.gta.world/ucp.php?mode=login&redirect=index.php'

#   -------------------------------------------------------
#                      Headless runner
#chrome_options = Options()
#chrome_options.add_argument('--headless=new')
#driver = webdriver.Chrome(options=chrome_options)
#   -------------------------------------------------------

#   -------------------------------------------------------
#                      Testing runner
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#   -------------------------------------------------------

input_string = "S. Roberts / Allprogamer"
badge = "4263"

pattern = r'^([A-Za-z])\. (\w+)'

match = re.match(pattern, input_string, re.IGNORECASE)

if match:
    letter = match.group(1)
    name = match.group(2)
    
    print("Letter:", letter)
    print("Name:", name)
    page_url = f'https://lspd.gta.world/memberlist.php?form=postform&field=username_list&select_single=1&mode=searchuser&first_char={letter.lower()}#memberlist'
else:
    index = input_string.find("/")
    if index != -1:
        name = input_string[:index].strip()
        letter = "s" # FOR TESTING ONLY
        print(name)
    page_url = f'https://lspd.gta.world/memberlist.php?form=postform&field=username_list&select_single=1&mode=searchuser&first_char={letter.lower()}#memberlist'


print(page_url)

driver = webdriver.Chrome(options=chrome_options)
driver.get(login_url)
time.sleep(1)
login_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.NAME, 'login')

login_field.send_keys(os.getenv('user'))
password_field.send_keys(os.getenv('password'))
login_button.click()

driver.get(page_url)


#table = driver.find_elements(By. CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username')
#href = driver.find_element(By. CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username').get_attribute('href')
#next_button = driver.find_element(By.CSS_SELECTOR, '#sort-results > div > div.pop-up-search-pagination > ul > li:nth-child(12) > a')
#time.sleep(1)
#for i in table:
#    print(i.text)
#    print(i.get_attribute('href'))
#next_button.click()
#href = driver.find_element(By. CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username').get_attribute('href')
#table = driver.find_elements(By. CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username')
#next_button = driver.find_element(By.CSS_SELECTOR, '#sort-results > div > div.pop-up-search-pagination > ul > li:nth-child(12) > a')
#time.sleep(1)
#for i in table:
#    print(i.text)
#    print(i.get_attribute('href'))

while True:
    table1 = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username-coloured')
    table2 = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username')
    table = table1 + table2
    forum_discord_display = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr:nth-child(10) > td:nth-child(3)')
    #table = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username-coloured')
    for i in table:     
        print(i.text)
        print(i.get_attribute('href'))
        if re.search(name, i.text):
            profile = i.get_attribute('href')
            driver.get(profile)
            break

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '#sort-results > div > div.pop-up-search-pagination > ul > li:last-child > a')
        next_button.click()
        #time.sleep(1)
    except NoSuchElementException:
        break

#memberlist > tbody > tr:nth-child(10) > td:nth-child(1) > a.username-coloured