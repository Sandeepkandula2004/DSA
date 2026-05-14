def countDigits(n):
        # code here
        c = 0
        while(n>0):
            c +=1
            n = int(n/10)
        return c

# Driver code
if __name__ == "__main__":
    n = 12345
    print(countDigits(n))

# Another way to do this is to use int(math.log10(n)) + 1 gives the number of digits in n.
