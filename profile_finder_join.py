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

input_string = "C. Thompson / Allprogamer"
badge_nr = "44159"

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
    # Find all rows in the table
    rows = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr')
    
    for row in rows:
        # Find username within the row
        username_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a')
        username = username_element.text.split('\n')
        profile_link = username_element.get_attribute('href')
        
        # Find badge number within the row
        badge_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
        badge = badge_element.text
        
        # Extract only the first string of numbers from the badge
        #first_badge_number = badge.split('\n')[2] if badge else ""
        
        # Append badge number and profile link to username list
        username.append(badge)
        username.append(profile_link)
        
        print(username)
        
        # Check conditions for profile navigation
        if name in username[0] and badge_nr in username[1]:
            profile = username[2]
            driver.get(profile)
            break  # Exit the loop if condition met
        
    try:
        # Find and click on the next button
        next_button = driver.find_element(By.CSS_SELECTOR, '#sort-results > div > div.pop-up-search-pagination > ul > li:last-child > a')
        next_button.click()
    except NoSuchElementException:
        # If no next button found, exit the loop
        break

#memberlist > tbody > tr:nth-child(10) > td:nth-child(1) > a.username-coloured





#rows = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr')
#
## Iterate over each row
#for row in rows:
#    # Find username within the row
#    username_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a')
#    username = username_element.text.split('\n')
#    profile_link = username_element.get_attribute('href')
#    # Find badge number within the row
#    badge_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
#    badge = badge_element.text
#    
#    # Extract only the first string of numbers from the badge
#    badge_parts = badge.split('\n')
#    first_badge_number = badge_parts[0] if badge_parts else ""
#    username.append(first_badge_number)
#    username.append(profile_link)