from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import re, time, json

def setup_driver() -> object:
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

def login(driver, username, password) -> None:
    login_url = 'https://lspd.gta.world/ucp.php?mode=login&redirect=index.php'
    driver.get(login_url)
    time.sleep(1)
    login_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.NAME, 'login')
    login_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

def search_profile(driver, officer_name, identifier):
    pattern = r'^([A-Za-z])\. (\w+)'
    match = re.match(pattern, officer_name, re.IGNORECASE)

    if match:
        letter = match.group(1)
        name = match.group(2)

        #print("Letter:", letter)
        #print("Name:", name)
        page_url = f'https://lspd.gta.world/memberlist.php?form=postform&field=username_list&select_single=1&mode=searchuser&first_char={letter.lower()}#memberlist'
        return search_profile_by_partial_name(driver, page_url, identifier, name)
    else:
        index = officer_name.find("/")
        if index != -1:
            name = officer_name[:index].strip()
            letter = None
            #print(name)
        page_url = 'https://lspd.gta.world/memberlist.php?form=postform&field=username_list&select_single=1&mode=searchuser#memberlist'
        return search_profile_by_full_name(driver, page_url, name)

def search_profile_by_partial_name(driver, page_url, identifier, name):
    driver.get(page_url)
    while True:
        rows = driver.find_elements(By.CSS_SELECTOR, '#memberlist > tbody > tr')

        for row in rows:
            username_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a')
            username = username_element.text.split('\n')
            profile_link = username_element.get_attribute('href')

            badge_element = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
            badge = badge_element.text

            username.append(badge)
            username.append(profile_link)

            #print(username)

            if name in username[0] and identifier in username[1]:
                profile = username[2]
                driver.get(profile)
                return str(profile)
            
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '#sort-results > div > div.pop-up-search-pagination > ul > li:last-child > a')
            next_button.click()
        except NoSuchElementException:
            break

def search_profile_by_full_name(driver, page_url, name):
    driver.get(page_url)
    
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    
    find_input = driver.find_element(By.CSS_SELECTOR, '#username')
    find_input.send_keys(name)
    send_button = driver.find_element(By.CSS_SELECTOR, '#search_memberlist > div > fieldset > button')
    send_button.click()
    
    profile = driver.find_element(By.CSS_SELECTOR, '#memberlist > tbody > tr > td:nth-child(1) > a.username-coloured')
    profile.click()
    return str(driver.current_url)

def get_roles(driver, page_url) -> list:
    driver.get(page_url)
    time.sleep(1)
    roles_button = driver.find_element(By.CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-heading.text-center.bg-profile > div.profile-display-content > div.group-buttons > div > button')
    roles_button.click()
    #time.sleep(2)
    data = driver.find_elements(By.CSS_SELECTOR, '#phpbb > div.btn-group.bootstrap-select.open > div > ul')
    result = []
    for i in data:
        result.extend(i.text.split('\n'))
        result.remove('Registered users')
    return result

def get_discord_id(driver, page_url) -> str:
    driver.get(page_url)
    data = driver.find_elements(By.CSS_SELECTOR, '#viewprofile > div.row > div > div > div.panel-body > ul > li')
    for i in data:
        result = i.text.split('\n')
        for line in result:
            if "Discord User ID:" in line:
                discord_id = line.split("Discord User ID:")[1].strip()
                driver.quit()
                return discord_id

def read_json():
    with open('known_users.json', 'r') as f:
        data = json.load(f)
    return data

def write_json(data, new_data):
    data.update(new_data)
    with open('known_users.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()
    return None
