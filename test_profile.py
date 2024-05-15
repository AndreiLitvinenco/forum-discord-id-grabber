from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
load_dotenv()

page_url = 'https://lspd.gta.world/memberlist.php?mode=searchuser&form=postform&field=username_list&select_single=1'
login_url = 'https://lspd.gta.world/ucp.php?mode=login&redirect=index.php'


#   -------------------------------------------------------
#                      Testing runner
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#   -------------------------------------------------------

driver.get(login_url)

login_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.NAME, 'login')

login_field.send_keys(os.getenv('user'))
password_field.send_keys(os.getenv('password'))
login_button.click()

driver.get(page_url)

table1 = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username-coloured')
table2 = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username')
table = table1 + table2
#table3 = driver.find_elements(By.CLASS_NAME, '#memberlist > tbody > tr > td:nth-child(1)')
badges = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(3)')
#for i in table2:
#    names = table1.append(i)
#for j, badge in zip(names, badges):
#    print(j.text)

rows = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr')

# Iterate over each row
for row in rows:
    # Find username within the row
    username_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a')
    username = username_element.text.split('\n')
    profile_link = username_element.get_attribute('href')
    # Find badge number within the row
    badge_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
    badge = badge_element.text
    
    # Extract only the first string of numbers from the badge
    badge_parts = badge.split('\n')
    first_badge_number = badge_parts[0] if badge_parts else ""
    username.append(first_badge_number)
    username.append(profile_link)
    
    # Print the username and the first badge number
    print(username)


driver.quit()

