def main(n):
    char = 65
    for i in range(n+1):
        temp = char
        for j in range(i):
            print(chr(temp), end=" ")
            temp += 1
        print()
main(4)