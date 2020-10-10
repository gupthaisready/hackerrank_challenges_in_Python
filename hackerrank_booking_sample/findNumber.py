

def findNumber(arr, k):
    if k in arr:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findNumber(arr, k)

    print(result + '\n')