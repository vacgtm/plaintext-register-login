import os, time, random, string

crypto_name = "fagcoin"
crypto_worth_usd = 582.12
plain_text_fn = "identifiers.txt"
def create_identifier(length):
    chars = string.ascii_letters + string.digits
    pwd = ''
    for i in range(length):
        pwd+=random.choice(chars)
    return pwd


def read():
    with open(plain_text_fn, 'r') as f:
        return f.read().splitlines() # make it a table

def login():
    os.system("cls")
    identifiers = read()
    print(identifiers)
    b = input("enter your identifier: ")
    if b in identifiers:
        hub()
    else:
        os.system("cls")
        print("identifier doesnt exist returning in 3 seconds...")
        time.sleep(3)
        return login()


def register():
    os.system("cls")
    a = create_identifier(16)

    with open(plain_text_fn, 'a') as f:
        f.write(a + '\n')
    
    print(f"account created!\nidentifier: {a}\nwait 3 seconds to login...")
    time.sleep(3)
    login()

def login_or_register():
    os.system("cls")
    choice = input("login or register: ")
    if choice.lower() == "login":
        login()
    elif choice.lower() == 'register':
        register()

def hub():
    os.system("cls")
    print("you have successfully logged in")
    input()


login_or_register()
