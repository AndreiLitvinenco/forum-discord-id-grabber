from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from var import variables as var
import time
from dotenv import load_dotenv
import os
load_dotenv()

page_url = 'https://lspd.gta.world/memberlist.php?mode=viewprofile&u=916'
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
roles_button = driver.find_element(By.CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-heading.text-center.bg-profile > div.profile-display-content > div.group-buttons > div > button')
roles_button.click()

time.sleep(2)
data = driver.find_elements(By.CSS_SELECTOR, '#phpbb > div.btn-group.bootstrap-select.open > div > ul')
for i in data:
    result = i.text.split('\n')
    print(result)
    #print(i.text)



#   roles = ['ASB: Recruitment and Employment Division', 'Civilian Employees', 'Civilian Supervisors']
#   for i in range(len(roles)):
#       if roles[i] in result:
#           print(roles[i], "is in the list.")