import bcrypt
import time
password = (input("Enter the password you wish to hash\n>>>"))
hash = b'password'
start = time.time()
hashed = bcrypt.hashpw(hash, bcrypt.gensalt(rounds=12))
end = time.time()
f = end - start
print(f)
print(hashed)

if bcrypt.checkpw(hash, hashed):
    print("login successful")
else:
    print("login failed")