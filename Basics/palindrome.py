class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        pal = 0
        y = x

        while y != 0:

            # Extract last digit
            temp = y % 10

            # Build reversed number
            pal = pal * 10 + temp

            # Remove last digit
            y = int(y / 10)

       
        return True if pal == x else False


# ---------------- DRIVER CODE ----------------

obj = Solution()

# Positive palindrome
print(obj.isPalindrome(121))         # True

# Negative number
print(obj.isPalindrome(-121))        # False

# Not a palindrome
print(obj.isPalindrome(123))         # False

# Number ending with zero
print(obj.isPalindrome(10))          # False

# Single digit number
print(obj.isPalindrome(7))           # True

# Even length palindrome
print(obj.isPalindrome(1221))        # True

# Odd length palindrome
print(obj.isPalindrome(12321))       # True

# Large palindrome
print(obj.isPalindrome(123454321))   # True

# Zero
print(obj.isPalindrome(0))           # True