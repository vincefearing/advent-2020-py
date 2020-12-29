def main():
    with open("/mnt/e/advent-2020-py/day3/data/data.txt") as file:
        treeMap = []
        treeMap = file.read().splitlines()
        print(treeCounter(treeMap, 1, 1) * treeCounter(treeMap, 3, 1) * treeCounter(treeMap, 5, 1) * treeCounter(treeMap, 7, 1) *  treeCounter(treeMap, 1, 2))

def treeCounter(treeMap, right, down):
    position = 0
    counter = 0
    
    for i in range(0,len(treeMap),down):
        temp = treeMap[i]
        if temp[position] == "#":
            counter += 1
        position += right
        if position >= len(temp):
            position = position - len(temp)
    return counter

if __name__ == "__main__":
    main()