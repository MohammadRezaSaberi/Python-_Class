password = "1234"
attempts = 0

while True:
    entered_password = input("Enter your password: ")
    if len(entered_password) != 4:
        print("The password must be 4 digits.")
        continue
    if entered_password == password:
        print("Correct password.")
        attempts = 0
    elif entered_password == password[::-1]:
        print("Police informed.")
        attempts = 0
    else:
        attempts += 1
        if attempts >= 3:
            print("Account locked.")
            attempts = 0
        else:
            print(f"Access Denied , Incorrect password. You have {3 - attempts} attempts left.")
