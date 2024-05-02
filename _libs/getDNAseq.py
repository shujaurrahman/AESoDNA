class DNA:
    def __init__(self, string):
        self.string = string
        self.dic = {"A":"00","C":"01","G":"10","T":"11"}
    def encode(self):
        try:
            strin = ''.join(str(self.string).split())
            dna = []
            tmpry = strin
            for atgc in range(0,len(tmpry),2):
                #print(tmpry[atgc:atgc+2])
                _chr = str(tmpry[atgc:atgc+2])
                if _chr in ["00", "10"]:
                    res = int(_chr,2) ^ int("01",2)
                    res = ('{:0>2b}'.format(res))

                else:
                    res = int(_chr,2) ^ int("10",2)
                    res = ('{:0>2b}'.format(res))
                    if res == "01": dna.append("A")
                    if res == "11": dna.append("A")

                dna.append(list(self.dic.keys())[list(self.dic.values()).index(res)])

               # dna.append(list(self.dic.keys())[int(str(tmpry[atgc:atgc+2]),2)])        
            
            return ''.join(dna)
        except:
            return "error occured in DNA encoding"

    def decode(self):
        try:
            strin = ''.join(str(self.string).split())
            dna = []
            tmpry = strin
            for atgc in range(len(tmpry)):
                if tmpry[atgc] == "A" and tmpry[atgc+1]=="T":
                    dna.append("01")
                    atgc+=1
                elif tmpry[atgc] == "A" and tmpry[atgc+1]=="C":
                    dna.append("11")
                    atgc+=1

                else:
                    if tmpry[atgc-1] == "A":
                        pass
                    else: 
                        res = int(str(self.dic.get(tmpry[atgc])),2)
                        binD = '{:0>2b}'.format(res)
                        binD = str(binD)
                        res = int(binD,2) ^ int("01",2)
                        res = '{:0>2b}'.format(res)
                        dna.append(str(res))
                        
                #print(list(self.dic.values())[int(tmpry[atgc],2)])
               # dna.append(list(self.dic.values())[atgc])        
            return ''.join(dna)
        except:
            return "error occured in DNA decoding"
