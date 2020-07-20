import json
from getpass import getpass

def get_password():
    password = getpass("Please enter your password: ")
    password2 = getpass("Please confirm your password: ")
    if password == password2:
        return password
    else:
        print("Passwords do not match. Please try again")
        return get_password()

sender = input("Please enter YOUR email address: ")

password = get_password()
print(password)

destination = input("Please enter the address to send to: ")

txt_file = open('message.txt')
try:
    message = txt_file.read()
finally:
    txt_file.close()

creds = {
   "to" : {
       "address" : destination
   },
   "from" : {
       "address" : sender,
       "password" : password
   },
   "message" : message
}



with open('creds.json', 'w') as outfile:
    json.dump(creds, outfile)
