# Create Acronyms Using Python:-

user = input("Enter a Phrase: ").split()
a = ""
for i in user:
    a = a + str(i[0]).upper()
print(f"user: {a}")

