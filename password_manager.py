master_pwd = input("What is the master password? ")

def view():
    with open("Passwords.txt", 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("Passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing onese? (view, add) Press q to quit ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue