from validator import validator

def main():
    with open("/mnt/e/advent-2020-py/day4/data/data.txt") as file:
        data = []
        passport = []
        validation = validator()
        validFields = 0
        validPassports = 0
        data = file.read().splitlines()
        for i in data:
            if len(i) != 0:
                line = i.split(" ")
                passport.extend(line)

            else:
                if validation.validatePassport(passport) == True:
                    validPassports += 1
                    passport.clear()
                passport.clear()
        #print(validFields)
        if validation.validatePassport(passport) == True:
                    validPassports += 1
                    passport.clear()
        print(validPassports)

if __name__ == "__main__":
    main()