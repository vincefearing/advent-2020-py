def main():
    inFile = open("/mnt/e/advent-2020-py/day1/data/data.txt", "r")
    expenseReport = []

    for i in inFile:
        expenseReport.append(int(i.strip("/n")))
    
    for i in expenseReport:
        for j in expenseReport:
            temp = i + j
            if temp == 2020:
                print(i*j)

if __name__ == "__main__":
    main()