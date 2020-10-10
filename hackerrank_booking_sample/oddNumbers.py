def getOddNumbers(l, r):
    return [num for num in range(l, r+1) if num%2!=0]

if __name__ == '__main__':
    l = int(input().strip())
    r = int(input().strip())

    print ("\n".join(map(str, getOddNumbers(l, r))))