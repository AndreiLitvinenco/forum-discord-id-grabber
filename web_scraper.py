from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

def login(driver, login_url, username, password):
    driver.get(login_url)
    login_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.NAME, 'login')
    login_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

def get_roles(driver, page_url):
    driver.get(page_url)
    roles_button = driver.find_element(By.CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-heading.text-center.bg-profile > div.profile-display-content > div.group-buttons > div > button')
    roles_button.click()
    time.sleep(2)
    data = driver.find_elements(By.CSS_SELECTOR, '#phpbb > div.btn-group.bootstrap-select.open > div > ul')
    result = []
    for i in data:
        result.extend(i.text.split('\n'))
    return result

def get_discord_id(driver, page_url):
    driver.get(page_url)
    data = driver.find_elements(By.CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-body > ul > li')
    for i in data:
        result = i.text.split('\n')
        for line in result:
            if "Discord User ID:" in line:
                discord_id = line.split("Discord User ID:")[1].strip()
                return discord_id
    return None
