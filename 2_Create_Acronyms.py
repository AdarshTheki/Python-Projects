# Create Acronyms Using Python:-

user = str(input("Enter a Phrase: "))
text = user.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)