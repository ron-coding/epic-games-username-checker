import requests

def check_username(username):
    response = requests.get(f"https://www.epicgames.com/id/api/account/v1/displayName/{username}")
    return response.status_code == 404

username = input("Enter the username to check: ")
if check_username(username):
    print(f"The username '{username}' is available.")
else:
    print(f"The username '{username}' is taken.")
