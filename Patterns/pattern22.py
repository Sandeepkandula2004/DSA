def main(n):
    curr = n
    odd = n*2-3
    for i in range(n-1):
        for j in range(n,n-i,-1):
            print(j, end="")
        for k in range(odd+1):
            print(curr, end="")
        for l in range(n-i,n+1):
            print(l, end="")
        curr -= 1
        odd -= 2
        print()

    for i in range(n):
        for j in range(n,i+1,-1):
            print(j, end="")
        for k in range(odd+2):
            print(curr,end="")
        for l in range(i+2,n+1):
            print(l, end="")
        curr += 1
        odd += 2
        print()

main(5)