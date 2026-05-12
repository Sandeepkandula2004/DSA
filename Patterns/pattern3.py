def main(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j, end=" ")  # Print numbers in the same line with a space
        print()  # Move to the next line after each row

main(5)