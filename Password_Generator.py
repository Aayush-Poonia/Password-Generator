import secrets
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    password = password + secrets.choice(characters)

print("Your secure password is:",password)