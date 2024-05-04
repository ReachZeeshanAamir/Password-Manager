from cryptography.fernet import Fernet, MultiFernet

def write_key():
    key1 = Fernet.generate_key()
    key2 = Fernet.generate_key()
    with open("E:\\Projects\\Python\\Projects\\Apps\\keyy.key", "wb") as key_file:
        key_file.write(key1)
        key_file.write(b'\n')  # Add a newline to separate keys
        key_file.write(key2)

def read_keys():
    keys = []
    with open("E:\\Projects\\Python\\Projects\\Apps\\keyy.key", "rb") as key_file:
        for line in key_file:
            keys.append(line.strip())
    return keys

stored_keys = read_keys()
key1 =  stored_keys[0].decode()
key2 =  stored_keys[1].decode()
fer = MultiFernet([key1, key2])

def view():
    with open("E:\\Projects\\Python\\Projects\\Apps\\password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if data:  # Check if the line is not empty
                user, passw = data.split("|")
                decrypted_passw = fer.decrypt(passw.encode()).decode()
                print(f"User: {user}\nPassword:",{decrypted_passw})


def addpass():
    name = input("Account Name: ")
    pwd = input("Enter password: ")
    encrypted_pwd = fer.encrypt(pwd.encode())
    with open("E:\\Projects\\Python\\Projects\\Apps\\password.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.decode()) + "\n")



while True:
    mode = input("Whould you like to add a new password or review existing one?(view/add/ press q to exit): ").lower()
    if mode == "q":
        break
    elif mode  == "view":
        view()
    elif mode == "add":
        addpass()
    else:
        print("Not a valid mode.")
        continue
