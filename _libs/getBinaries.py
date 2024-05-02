class Binary:
    def __init__(self, string):
        self.string = string

    def encode(self):
        try:
            strin = str(self.string)
            binary = []

            tmpry = list(strin)
            for e in tmpry:
                for each in e:
                    # can be done like this
                    binary.append(format(ord(each),'b')) if len(format(ord(each), 'b'))==8 else binary.append('{:0>8}'.format(format(ord(each),'b')))

            encoded = ' '.join(binary)

            return encoded

        except:
            return "There is an error in your command"

    def decode(self):
        try:
            strin = str(self.string).split()
            def getMeThat(binDump):
                string = int(binDump, 2)

                # return
                return string

            bin_data = strin

            binPaded = []
            for item in bin_data:

                if len(item) == 8:
                    binPaded.append(item)
                elif 8 > len(item):
                    binPaded.append('{:0>8}'.format(item))
                else:

                    bin_data = ''.join(item)
                    for bit in range(0, len(bin_data), 8):
                        _byte = bin_data[bit:bit + 8]
                        binPaded.append(_byte)


            str_data = ''

            for one in binPaded:
                tmpry_data = one

                decDump = getMeThat(tmpry_data)
                str_data = str_data + chr(decDump)
            decoded = str_data

            return decoded

        except:
            return "Input must be a binary number"
