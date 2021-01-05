def main():

    rows = []
    columns = []
    row = 0
    column = 0
    ID = 0

    for i in range(128):
        rows.append(i)

    for i in range(8):
        columns.append(i)

    with open("/mnt/e/advent-2020-py/day5/data/data.txt") as file:
        data = file.read().splitlines()

        for i in data:
            if len(i) != 0:
                rowPass = i[0:7]
                colPass = i[7:]
                low = 0
                high = len(rows) - 1
                mid = 0
                for i in rowPass:

                    if low <= high:

                        mid = (high + low) // 2
                        if i == "F":
                            high = mid
                        elif i == "B":
                            low = mid
                    row = rows[mid]
                
                low = 0
                high = len(columns) - 1
                mid = 0
                for i in colPass:
        
                    if low <= high:

                        mid = (high + low) // 2
                        if i == "L":
                            high = mid
                        elif i == "R":
                            low = mid
                    column = columns[mid]

            temp = (row * 8) + column
            if temp > ID:
                ID = temp
                if ID == 854:
                    print(i)        

    print(ID)

def binarySearch(list):

    low = 0
    high = len(list) - 1
    mid = 0
    
    if low <= high:
        mid = (high + low) // 2
        if i == "F":
            high = mid
        elif i == "B":
            low = mid
    else:
        row = rows[low]


if __name__ == "__main__":
    main()