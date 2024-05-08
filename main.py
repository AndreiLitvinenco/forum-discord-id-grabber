from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from var import variables as var

page_url = 'https://lspd.gta.world/memberlist.php?mode=viewprofile&u=8173'
login_url = 'https://lspd.gta.world/ucp.php?mode=login&redirect=index.php'

chrome_options = Options()
chrome_options.add_argument('--headless=new')

driver = webdriver.Chrome(options=chrome_options)
driver.get(login_url)

login_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.NAME, 'login')

login_field.send_keys(var.user)
password_field.send_keys(var.password)
login_button.click()

driver.get(page_url)

result = driver.find_element(By. CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-body > ul > li:nth-child(12)')
print(result.text[17:35])
