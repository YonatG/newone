print("Welcome to my A M A Z I N G App!")
username = input("username: ")

w = "48 65 6c 6c 6f 20 7b 7d 21 20 49 20 61 6d 20 73 6f 20 68 61 70 70 79 20 79 6f 75 20 62 75 69 6c 74 20 74 68 69 73 20 63 6f 64 65 2e 0a 48 6f 70 65 20 79 6f 75 20 65 6e 6a 6f 79 20 4a 65 6e 6b 69 6e 73 21"

print(bytearray.fromhex(w).decode().format(username.title()))
