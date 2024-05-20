import json

# Load existing JSON data
with open('data.json', 'r') as file:
    existing_data = json.load(file)

# Define new user data
new_user_data = {
    "NewUser2": {
        "id": "123456789",
        "url": "https://example.com/newuser"
    }
}

# Update existing data with new user data
existing_data.update(new_user_data)

# Write back to the JSON file
with open('data.json', 'w') as file:
    json.dump(existing_data, file, indent=4)  # indent for pretty formatting
