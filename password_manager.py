from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def load_key():
    with open ("Key.key", "rb") as key_file:
        key = key_file.read()
    return key

master_pwd = input("Please enter the master password. ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user_pass = data.split("|")
                print("User: ", user_pass[0],"| Password: ",fer.decrypt(user_pass[1].encode()).decode())
    except Exception as e:
        print("An error Occured. Please review")

def add():
    name = input("Acccount name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        encrypted_pwd = fer.encrypt(pwd.encode())
        f.write(name + "|" + (encrypted_pwd.decode()) + "\n")


while True:
    mode = input("Would you like to new or view existing one. Please Enter: ")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Please enter valid choice")
        continue