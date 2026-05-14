class Solution:
    def gcd(self, a, b):

        mini = min(a, b)
        maxi = max(a, b)

        while(maxi != 0 and mini != 0):

            temp = mini
            mini = maxi % mini
            maxi = temp

        return maxi


obj = Solution()

print(obj.gcd(48, 18))     # 6
print(obj.gcd(10, 0))      # 10
print(obj.gcd(0, 10))      # 10
print(obj.gcd(0, 0))       # 0
print(obj.gcd(5, 5))       # 5
print(obj.gcd(7, 13))      # 1
print(obj.gcd(24, 8))      # 8
print(obj.gcd(100, 25))    # 25
print(obj.gcd(270, 192))   # 6
print(obj.gcd(1, 999))     # 1