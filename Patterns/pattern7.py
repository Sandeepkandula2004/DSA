def main(n):
    c = 1
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")  # Print spaces for left padding
        print("* " * c)
        c += 2
main(5)