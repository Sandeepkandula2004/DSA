def main(n):
    curr_num = 1
    iter = 1
    for i in range(1, n + 1):
        for j in range(iter):
            print(curr_num, end="")
            curr_num += 1
        iter += 1
        print()
main(4)
