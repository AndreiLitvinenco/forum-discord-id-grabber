from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from var import variables as var

page_url = 'https://lspd.gta.world/memberlist.php?mode=searchuser&form=postform&field=username_list&select_single=1'
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

login_field.send_keys(var.user)
password_field.send_keys(var.password)
login_button.click()

driver.get(page_url)
find_input = driver.find_element(By.CSS_SELECTOR, '#username')
find_input.send_keys('Danica Ashford')
#driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]")
send_button = driver.find_element(By.CSS_SELECTOR, '#search_memberlist > div > fieldset > button')
send_button.click()

profile = driver.find_element(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username-coloured')
profile.click()