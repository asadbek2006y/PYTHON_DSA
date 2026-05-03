password = input("Enter your password: ")

while len(password) < 6:
    print("Password must be at least 6 characters long.")
    password = input("Enter your password: ")
print("Password accepted.")