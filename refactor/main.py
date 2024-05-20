from forum_functions import setup_driver, login, search_profile, get_roles, get_discord_id, read_json, write_json
from dotenv import load_dotenv
import os

def main():
    #officer_name = 'Stella Roberts / Allprogamer'
    #identifier = '4263'
    data = read_json()
    officer_name = input('Insert the name of the officer you want to find\n')
    identifier = input('Insert the identifier of the officer you want to find\n')

    #print(officer_name, identifier)
    driver = setup_driver()
    login(driver, os.getenv('user'), os.getenv('password'))
    profile_url = search_profile(driver, officer_name, identifier)
    roles = get_roles(driver, profile_url)
    discord_id = get_discord_id(driver, profile_url)

    print("Roles:", roles)
    print("Discord ID:", discord_id)
    print("User profile:", profile_url)

    new_data = {officer_name:{
        "id": discord_id,
        "url": profile_url}}
    write_json(data, new_data)

if __name__ == '__main__':
    load_dotenv()
    while True:
        main()

