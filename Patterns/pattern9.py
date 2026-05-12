def main(n):
    c = 1
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")  # Print spaces for left padding
        print("* " * c)
        c += 2
    c = (n*2)-1
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ", end=" ")  # Print spaces for left padding
        print("* " * c)
        c -= 2
main(4)
            