from typing import List
import copy


# ---------------- REVERSE METHOD ---------------- #

class ReverseSolution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return

        k %= n

        nums[:n-k] = nums[:n-k][::-1]
        nums[n-k:] = nums[n-k:][::-1]
        nums.reverse()


# ---------------- EXTRA ARRAY METHOD ---------------- #

class ExtraArraySolution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return

        k %= n

        new_arr = []
        new_arr += nums[n-k:n]
        new_arr += nums[0:n-k]

        for i in range(n):
            nums[i] = new_arr[i]


# ---------------- DRIVER CODE ---------------- #

test_cases = [
    # normal case
    ([1,2,3,4,5,6,7], 3),

    # k = 0
    ([1,2,3,4], 0),

    # k = n
    ([1,2,3,4], 4),

    # k > n
    ([1,2,3,4,5], 8),

    # single element
    ([10], 5),

    # two elements
    ([1,2], 1),

    # duplicates
    ([1,1,1,2,2,3], 2),

    # negative numbers
    ([-1,-2,-3,-4], 2),

    # empty array
    ([], 3),
]


print("-------- TESTING REVERSE METHOD --------\n")

for arr, k in test_cases:
    nums = copy.deepcopy(arr)

    ReverseSolution().rotate(nums, k)

    print(f"Original: {arr}")
    print(f"k = {k}")
    print(f"Rotated : {nums}")
    print("-" * 40)


print("\n-------- TESTING EXTRA ARRAY METHOD --------\n")

for arr, k in test_cases:
    nums = copy.deepcopy(arr)

    ExtraArraySolution().rotate(nums, k)

    print(f"Original: {arr}")
    print(f"k = {k}")
    print(f"Rotated : {nums}")
    print("-" * 40)