def main(n):
    print("*"*n, end="")
    print()
    for j in range(n-2):
        print("*", end="")
        for i in range(n-2):
            print(" ", end="")
        print("*", end="")
        print()
    print("*"*n)
main(2)