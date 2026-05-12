def main(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end=" ")  # Print the current row number in the same line with a space
        print()  # Move to the next line after each row

main(5)