class validator:
    def validateFields(self, passport):

        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False

        for i in passport:
            temp = i.split(":")
            field = temp[0]
            value = temp[1]
            if field == "byr":
                byr = True
            elif field == "iyr":
                iyr = True
            elif field == "eyr":
                eyr = True
            elif field == "hgt":
                hgt = True
            elif field == "hcl":
                hcl = True
            elif field == "ecl":
                ecl = True
            elif field == "pid":
                pid = True
            elif field == "cid":
                cid = True
        
        if byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True:

            return True

        else:

            return False
    
    def validatePassport(self, passport):

        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
        for i in passport:
            field, value = i.split(":")
            if field == "byr":
                num = int(value)
                if len(value) == 4 and num >= 1920 and num <= 2002:
                    byr = True
                    print(value)
            elif field == "iyr":
                num = int(value)
                if len(value) == 4 and num >= 2010 and num <= 2020:
                    iyr = True
            elif field == "eyr":
                num = int(value)
                if num >= 2020 and num <= 2030:
                    eyr = True
            elif field == "hgt":
                unit = value[-2:]
                sub = value[0:-2]
                if sub.isnumeric():
                    num = int(sub)
                if unit == "cm":
                    if num >= 150 and num <= 193:
                        hgt = True
                elif unit == "in":
                    if num >= 59 and num <= 76:
                        hgt = True
            elif field == "hcl":
                sub = value[1:7]
                valid = False
                validNum = 0
                for i in sub:
                    if i >= "0" and i <= "9":
                        valid = True
                        validNum += 1
                    elif i >= "a" and i <= "f":
                        valid = True
                        validNum += 1
                    else:
                        valid = False
                if len(sub) == 6 and validNum == 6 and value[0] == "#":
                        hcl = True
            elif field == "ecl":
                if value == "amb" or value == "blu" or value == "gry" or value == "grn" or value == "hzl" or value == "oth" or value == "brn":
                    ecl = True
            elif field == "pid":
                if value.isnumeric() and len(value) == 9:
                    pid = True
            elif field == "cid":
                cid = True
                
        if byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True:

            return True

        else:

            return False