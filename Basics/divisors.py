import math

class Solution:
    def getDivisors(self, n):

        arr = []

        for i in range(1, int(math.sqrt(n)) + 1):

            if n % i == 0:

                arr.append(i)

                if (n // i != i):
                    arr.append(n // i)

        return sorted(arr)


obj = Solution()

print(obj.getDivisors(1))      # [1]
print(obj.getDivisors(2))      # [1, 2]
print(obj.getDivisors(6))      # [1, 2, 3, 6]
print(obj.getDivisors(12))     # [1, 2, 3, 4, 6, 12]
print(obj.getDivisors(25))     # [1, 5, 25]
print(obj.getDivisors(36))     # [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(obj.getDivisors(49))     # [1, 7, 49]
print(obj.getDivisors(97))     # [1, 97]
print(obj.getDivisors(100))    # [1, 2, 4, 5, 10, 20, 25, 50, 100]