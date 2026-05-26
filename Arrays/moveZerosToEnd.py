from typing import List
import copy


# ---------------- COUNTING METHOD ---------------- #

class CountingSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        c = 0

        # count zeros
        for i in range(n):
            if nums[i] == 0:
                c += 1

        j = 0

        # move non-zeros forward
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # fill remaining with zeros
        while c:
            nums[j] = 0
            j += 1
            c -= 1


# ---------------- OPTIMIZED SWAP METHOD ---------------- #

class OptimizedSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                # avoid unnecessary self swaps
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]

                j += 1


# ---------------- DRIVER CODE ---------------- #

test_cases = [

    # normal case
    [0,1,0,3,12],

    # all zeros
    [0,0,0,0],

    # no zeros
    [1,2,3,4],

    # single zero
    [0],

    # single non-zero
    [5],

    # zeros at end
    [1,2,3,0,0],

    # zeros at beginning
    [0,0,1,2,3],

    # alternating zeros
    [0,1,0,2,0,3,0,4],

    # duplicates
    [1,0,1,0,1,0],

    # negative numbers
    [0,-1,0,-2,-3],

    # empty array
    [],
]


# ---------------- TEST COUNTING METHOD ---------------- #

print("===== COUNTING METHOD =====\n")

for arr in test_cases:

    nums = copy.deepcopy(arr)

    CountingSolution().moveZeroes(nums)

    print(f"Original : {arr}")
    print(f"Output   : {nums}")
    print("-" * 40)


# ---------------- TEST OPTIMIZED METHOD ---------------- #

print("\n===== OPTIMIZED SWAP METHOD =====\n")

for arr in test_cases:

    nums = copy.deepcopy(arr)

    OptimizedSolution().moveZeroes(nums)

    print(f"Original : {arr}")
    print(f"Output   : {nums}")
    print("-" * 40)