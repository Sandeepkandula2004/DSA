class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


obj = Solution()

test_cases = [
    0,
    1,
    2,
    3,
    5,
    10,
    15,
    20,
    25,
    30
]

for i, n in enumerate(test_cases, 1):
    result = obj.fib(n)

    print(f"Test Case {i}")
    print("Input:", n)
    print("Output:", result)
    print()