import random
# Enter the length of the password which you need
passlen=int(input("Enter the length of the password which you need:"))
# Make a string of the all the charcaters present in your keyboard
s="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+=-,./;[]<>"
# Use random and sample
p="".join(random.sample(s,passlen))
# Prinitng or getting the password

print(p)