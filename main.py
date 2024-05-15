from web_scraper import setup_driver, login, get_roles, get_discord_id
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    login_url = 'https://lspd.gta.world/ucp.php?mode=login&redirect=index.php'
    page_url = 'https://lspd.gta.world/memberlist.php?mode=viewprofile&u=916'
    username = os.getenv('user')
    password = os.getenv('password')
    driver = setup_driver()
    login(driver, login_url, username, password)
    roles = get_roles(driver, page_url)

    expected_roles = ['ASB: Recruitment and Employment Division', 'Civilian Employees', 'Civilian Supervisors']
    for role in expected_roles:
        if role in roles:
            print(role, "is in the list.")

    discord_id = get_discord_id(driver, page_url)
    if discord_id:
        print("Discord User ID:", discord_id)
    else:
        print("Discord User ID not found.")

    driver.quit()

if __name__ == "__main__":
    main()
