
import random
import string
print("Welcome to password generated")
password_size=int(input("How many letter do you want in passworld:: "))
password=""
symbol_in_password=int(input("How many symbol do you want in password:: "))
symbol="".join(random.sample(string.punctuation,symbol_in_password))
password=password+symbol
number_in_password=int(input("How many number do you want in password:: "))
number="".join(random.sample(string.digits,number_in_password))
password=password+number
remanining_size=password_size-(symbol_in_password+number_in_password)
for i in range(remanining_size):
    if i%2==0:
        upper_case="".join(random.choice(string.ascii_uppercase))
        password=password+upper_case
    else:
        lower_case="".join(random.choice(string.ascii_lowercase))
        password=password+lower_case
password=password.split(" ")
random.shuffle(password)
password="".join(password)
print(password)
