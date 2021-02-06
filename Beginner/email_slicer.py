email=input("Enter your email id: ")

t=email.index("@")

user_name=email[:t]

domain_name=email[t+1:]

print("Your user name is '{}' and domain name is '{}' ".format(user_name,domain_name))

