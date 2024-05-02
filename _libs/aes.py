from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from tinyec import registry
import hashlib, secrets, binascii
import time
import random
import string







class AEScrypt:
    def __init__(self,string,keyFile="0"):
        self.string = string
        self.keyFile = keyFile

    def encrypt(self):
        try:
            curve = registry.get_curve('brainpoolP256r1')
            shared_ecckey = []
            start_time=time.time()
            privKey = secrets.randbelow(curve.field.n)
            print("Private key",privKey)
            Key1="{0:b}".format(int(privKey))
            K_len=len(Key1)
            if K_len % 255 == 0:
                print("The Secretkey1 in binary:",Key1)
            else:    
                for i in range(abs(255 - (K_len % 255))):
                    Key1 = Key1 + "0"
                print("The Secretkey1 in binary:",Key1)
            binary_list = [Key1[i: i+5] for i in range(0, len(Key1), 5)]
            DNA_encoding = {
                "00000":"A", 
                "00001":"B",
                "00010":"C",
                "00011":"D",
                "00100":"E",
                "00101":"F", 
                "00110":"G", 
                "00111":"H",
                "01000":"I",
                "01001":"J",
                "01010":"K",
                "01011":"L",
                "01100":"M",
                "01101":"N",
                "01110":"O",
                "01111":"P",
                "10000":"Q",
                "10001":"R",
                "10010":"S",
                "10011":"T",
                "10100":"U",
                "10101":"V",
                "10110":"W",
                "10111":"X",
                "11000":"Y",
                "11001":"Z",
                "11010":"1",
                "11011":"2",
                "11100":"3",
                "11101":"4",
                "11110":"5",
                "11111":"6",
            } 
            DNA_list = []
            for num in binary_list:
                for key in list(DNA_encoding.keys()):
                    if num == key:
                        DNA_list.append(DNA_encoding.get(key))

            DNA_str = "".join(DNA_list)
            print("The string represented by single-letter codes is :",DNA_str)
            end_time=time.time()
            total_time=end_time-start_time
            print("total time",total_time)



            strin = str(self.string)
            key = get_random_bytes(32)
            password = DNA_str
            key = PBKDF2(password, key, dkLen=32)
            f2en = strin
            buffSize = 65536
            keyF = str(f2en).split("-")[1].split(".txt")[0]
            keyF = "./assets/"+keyF+"/"+keyF+".key"
            ifile = open(f2en, 'rb')
            ofile = open(f2en + '.encrypted', 'wb')
            kfile = open(keyF,"wb")
            cipherText = AES.new(key, AES.MODE_CFB)

            ofile.write(cipherText.iv)
            kfile.write(key)
            buffer = ifile.read(buffSize)
            while len(buffer) > 0:
                ciphered_bytes = cipherText.encrypt(buffer)
                ofile.write(ciphered_bytes)
                buffer = ifile.read(buffSize)

            ifile.close()
            ofile.close()
            kfile.close()
            return "File has been encrypted\nEncrypted file: "+str(f2en+'.encrypted')+"\nKey file: "+keyF
        except: return "some error occured, try again!\nMost probably, file permission error"

    def decrypt(self):
        try:
            f2de = str(self.string)
            kfile = str(self.keyFile)
            
            ifile = open(f2de, 'rb')
            kFile = open(kfile,'rb')

            #ofile = open(f2de.split(".encrypted")[0] + '.decrypted', 'wb')

            iv = ifile.read(16)
            buffSize = 65536
            aes2DNA = []
            cipherText = AES.new(kFile.read(), AES.MODE_CFB, iv=iv)

            buffer = ifile.read(buffSize)
            while len(buffer) > 0:
                decrypted_bytes = cipherText.decrypt(buffer)
                aes2DNA.append(decrypted_bytes.decode('utf-8'))
                buffer = ifile.read(buffSize)

            ifile.close()
            kFile.close()

            return ''.join(aes2DNA)

        except: return "some error occured, try again!\nMost probably, file permission error"
