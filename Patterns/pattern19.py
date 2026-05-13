def main(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end="")
        for k in range(i):
            print("  ", end="")
        for l in range(n-i):
            print("*", end="")
        print()
    for i in range(n):
        for m in range(i+1):
            print("*", end="")
        for s in range(n-i-1):
            print("  ", end="")
        for o in range(i+1):
            print("*", end="")
        print()
main(5)