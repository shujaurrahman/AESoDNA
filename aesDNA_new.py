from _libs.getBinaries import Binary
from _libs.getDNAseq import DNA
from _libs.aes import AEScrypt
from random import shuffle
from os import mkdir as md
import time

shuff = list("abcdefghijklmnopqrstuvwxyz")
shuffle(shuff)
shuff = ''.join(shuff[:5])

text2op = input("For encryption press 1, decryption press 2: ")[0]

if (text2op == "1"):
    onWhat = input("Enter the pathname of the file to encrypt: ")
    start_encryption_time = time.time()
    try:
        file2en = str(open(onWhat, "r").read()).strip()
        f2bin = Binary(file2en).encode()
        bin2DNA = DNA(f2bin).encode()
        dname = "./assets/" + shuff
        md(dname)
        nameOfifile = dname + "/DNAencoded-" + shuff + ".txt"
        open(nameOfifile,"wb").write(bytes(bin2DNA,'utf-8'))
        print(AEScrypt(nameOfifile).encrypt())
        print("-"*60)
        print("Encrypted data in DNA: ")
        dn = open("output.txt", "w")
        dn.write(DNA(Binary(str(open(nameOfifile+".encrypted", "rb").read()).strip()).encode()).encode())
        dn.close()
        print("check ./output.txt")
        end_encryption_time = time.time()
        total_encryption_time = end_encryption_time - start_encryption_time
        print("total_encryption_time:", total_encryption_time, "sec")
    except:
        print("Permission error or file does not exists!")
elif (text2op == "2"):
    Start_Decryption_time = time.time()
    onWhat = input("Enter the pathname of the file to decrypt: ")
    onKey = input("Enter the key file: ")
    try:
        aes2DNA = AEScrypt(onWhat, onKey).decrypt()
        DNA2bin = DNA(aes2DNA).decode()
        bin2de = Binary(DNA2bin).decode()
        nameOfifile = onWhat.split(".encrypted")[0] + ".decrypted"
        open(nameOfifile, "w").write(bin2de)
        print("Decrypted file: " + str(nameOfifile))
        print("-"*60)
        print("Decrypted data: ")
        print(open(nameOfifile, "r").read())
        end_Decryption_time = time.time()
        total_decryption_time = end_Decryption_time - Start_Decryption_time
        print("total_Decryption_time:", total_decryption_time, "sec")
    except:
        print("Permission error or file does not exists!")
else:
    print("Please choose either 1 or 2")
