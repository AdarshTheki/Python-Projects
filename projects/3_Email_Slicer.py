# Email Slicer with python:-

email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your User Name is '{username}' and your domain is '{domain_name}'")
print(format_)