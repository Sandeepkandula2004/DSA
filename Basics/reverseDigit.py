class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        y = abs(x)

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while(y > 0):

            # Extract last digit
            temp = y % 10

            if rev < INT_MIN/10 or rev > INT_MAX/10:
                return 0

            # Append digit
            rev = rev * 10 + temp

            # Remove last digit
            y = int(y / 10)

        # Restore sign
        if x < 0:
            return -rev
        else:
            return rev


# ---------------- DRIVER CODE ----------------

obj = Solution()

# Normal positive number
print(obj.reverse(123))          # 321

# Normal negative number
print(obj.reverse(-123))         # -321

# Number ending with zero
print(obj.reverse(120))          # 21

# Zero
print(obj.reverse(0))            # 0

# Palindrome number
print(obj.reverse(121))          # 121

# 32-bit overflow positive
print(obj.reverse(1534236469))   # 0

# 32-bit overflow negative
print(obj.reverse(-1534236469))  # 0

# INT_MAX boundary
print(obj.reverse(2147483647))   # 0

# INT_MIN boundary
print(obj.reverse(-2147483648))  # 0