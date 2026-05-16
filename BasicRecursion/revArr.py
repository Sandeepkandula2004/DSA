class Solution:
    def reverseArray(self, arr, i=0, j=None):
        if j is None:
            j = len(arr) - 1

        if i >= j:
            return arr

        arr[i], arr[j] = arr[j], arr[i]

        return self.reverseArray(arr, i + 1, j - 1)


obj = Solution()

test_cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [10, 20, 30, 40, 50],
    [-1, -2, -3, -4],
    [7, 7, 7, 7],
    [1, 0, 1, 0, 1],
    list(range(1, 11))
]

for i, arr in enumerate(test_cases, 1):
    original = arr[:]
    result = obj.reverseArray(arr)

    print(f"Test Case {i}")
    print("Original:", original)
    print("Reversed:", result)
    print()