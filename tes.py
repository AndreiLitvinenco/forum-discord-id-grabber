import re

# Input string
input_string = "N. Estera / Allprogamer"

# Define a regular expression pattern to match "A" and "Estera"
#pattern = r'^([A-Z])\. (\w+)'
pattern = r'^([A-Za-z])\. (\w+)'


# Use re.match to find the pattern in the input string
match = re.match(pattern, input_string)

if match:
    # Extract the matched groups
    letter = match.group(1)
    name = match.group(2)
    
    # Print the extracted values
    print("Letter:", letter)
    print("Name:", name)
    page_url = f'https://lspd.gta.world/memberlist.php?form=postform&field=username_list&select_single=1&mode=searchuser&first_char={letter.lower()}#memberlist'
    print(page_url)
else:
    # Try to extract name until "/ Allprogamer"
    index = input_string.find(" / ")
    if index != -1:
        name = input_string[:index]
    print(name)
    page_url = 'https://lsfd.gta.world/memberlist.php?form=postform&field=username_list&select_single=1&mode=searchuser&first_char=#memberlist'
    print(page_url)
