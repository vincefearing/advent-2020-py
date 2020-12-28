def main():
    with open("/mnt/e/advent-2020-py/day2/data/data.txt") as inFile:
        expenseReport = []
        expenseReport = inFile.read().splitlines()
        part1(expenseReport)
        
   
def part1(expenseReport):
    valid = 0
    for i in expenseReport:
        temp = i.split(" ")
        numRange = temp[0].split("-")
        key = temp[1][0]
        value = temp[2]
        count = value.count(key)
        if count >= int(numRange[0]) and count <= int(numRange[1]):
            valid += 1
    print(valid)

if __name__ == "__main__":
    main()