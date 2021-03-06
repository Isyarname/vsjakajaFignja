def binarySearch(sortedList: list, item):
    low = 0
    high = len(sortedList)-1
    tryValue = 0
    while low <= high:
        mid = (low + high) // 2
        guess = sortedList[mid]
        tryValue += 1
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            print(tryValue)
            return mid
    return None



if __name__ == "__main__":
    l = list(range(0, 100))
    binarySearch(l, 56)