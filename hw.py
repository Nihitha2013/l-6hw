import random
import string

print("Welcome to password generator game!")
length=int(input("Enter the length of pasaword:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
symbols=string.punctuation
all= lower+upper+number+symbols

temp=random.sample(all,length)
password="".join(temp)
print(password)