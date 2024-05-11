from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
load_dotenv()

page_url = 'https://lspd.gta.world/memberlist.php?mode=viewprofile&u=8173'
#page_url = 'https://lspd.gta.world/memberlist.php?mode=viewprofile&u=916'
login_url = 'https://lspd.gta.world/ucp.php?mode=login&redirect=index.php'

chrome_options = Options()
chrome_options.add_argument('--headless=new')

driver = webdriver.Chrome(options=chrome_options)
driver.get(login_url)

login_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.NAME, 'login')

login_field.send_keys(os.getenv('user'))
password_field.send_keys(os.getenv('password'))
login_button.click()

driver.get(page_url)

data = driver.find_elements(By. CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-body > ul > li')
for i in data:
    result = i.text.split('\n')
    for line in result:
        if "Discord User ID:" in line:
            discord_id = line.split("Discord User ID:")[1].strip()
            print("Discord User ID:", discord_id)
            break



