# Ask user for their name
name =input("what's your name?  ")

# Remove whitespace from str and capitalize user's name
name = name.strip().title()

# split user's name into first name and last name
first, last = name.split(" ")


# say hello to user
print(f'Hello ,{first}')
# print("hello, ", end="")
# print(name)

# Lets try to do it with sep
# print("hello, ", name, sep="???")
# print("hello ,\"friend\"")