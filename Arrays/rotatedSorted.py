from typing import List

class Solution:

    # ---------------------------------------------------
    # Approach 1:
    # Generate every rotation and check if sorted
    # Time  : O(n^2)
    # Space : O(n)
    # ---------------------------------------------------
    def check_bruteforce(self, nums: List[int]) -> bool:

        flag = False
        n = len(nums)

        def isSorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        for i in range(n):

            new_arr = []

            # rotation
            new_arr += nums[i + 1:n]
            new_arr += nums[0:i + 1]

            if isSorted(new_arr):
                flag = True
                break

        return flag


    # ---------------------------------------------------
    # Approach 2:
    # Count number of decreasing points
    # Time  : O(n)
    # Space : O(1)
    # ---------------------------------------------------
    def check_optimal(self, nums: List[int]) -> bool:

        c = 0
        n = len(nums)
        if n <= 1:
            return True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                c += 1

        # circular check
        if nums[n - 1] > nums[0]:
            c += 1

        return False if c > 1 else True


    # ---------------------------------------------------
    # Approach 3:
    # Circular traversal using modulo
    # Time  : O(n)
    # Space : O(1)
    # ---------------------------------------------------
    def check_circular(self, nums: List[int]) -> bool:

        n = len(nums)

        if n <= 1:
            return True

        c = 0

        for i in range(2 * n - 1):

            if nums[i % n] <= nums[(i + 1) % n]:
                c += 1
            else:
                c = 0

            if c == n - 1:
                return True

        return False


# =======================================================
# DRIVER CODE
# =======================================================

test_cases = [

    # basic valid rotation
    [3, 4, 5, 1, 2],

    # already sorted
    [1, 2, 3, 4, 5],

    # invalid rotation
    [2, 1, 3, 4],

    # another invalid
    [3, 5, 4, 1, 2],

    # single element
    [1],

    # two elements valid
    [2, 1],

    # duplicates valid
    [1, 1, 1],

    # duplicates + rotation
    [2, 2, 3, 1, 2],

    # decreasing completely
    [5, 4, 3, 2, 1],

    # all same
    [7, 7, 7, 7],

    # edge
    [],
]

sol = Solution()

for nums in test_cases:

    print(f"\nArray: {nums}")

    print("Bruteforce :", sol.check_bruteforce(nums))
    print("Optimal    :", sol.check_optimal(nums))
    print("Circular   :", sol.check_circular(nums))