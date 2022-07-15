from cryptography.fernet import Fernet
import os

keyf = open('key.key' , 'wb')
key = Fernet.generate_key()
keyf.write(key)
keyf.close()