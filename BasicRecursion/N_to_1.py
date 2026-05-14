def printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n - 1)
printNumbers(5)