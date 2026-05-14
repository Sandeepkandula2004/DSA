import math

class Solution:

    def isPrime(self, n):

        if n == 1:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):

            if n % i == 0:
                return False

        return True


obj = Solution()

print(obj.isPrime(1))     # False
print(obj.isPrime(2))     # True
print(obj.isPrime(3))     # True
print(obj.isPrime(4))     # False
print(obj.isPrime(5))     # True
print(obj.isPrime(9))     # False
print(obj.isPrime(17))    # True
print(obj.isPrime(25))    # False
print(obj.isPrime(97))    # True
print(obj.isPrime(100))   # False