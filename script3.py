import secrets
import string
import sys

input_value = sys.argv[1]

# Use the input value in your script
print(f"The entered value is: {input_value}")
print("")
print("")

# define the combinations by calling characters from string
alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

combination = alphabets + numbers + symbols

# fix the length of password
length = int(input_value)

# generating the password
password = ''
for i in range(length):
    password += ''.join(secrets.choice(combination))

# here you the password you got!
print(password)
