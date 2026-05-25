from typing import List
from collections import defaultdict


class Solution:

    # =====================================================
    # Approach 1 : HashMap
    # Time  : O(n)
    # Space : O(n)
    # =====================================================
    def removeDuplicates_hashmap(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        keys = list(hashmap.keys())

        for i in range(len(keys)):
            nums[i] = keys[i]

        return len(keys)


    # =====================================================
    # Approach 2 : Two Pointer Optimal
    # Time  : O(n)
    # Space : O(1)
    # =====================================================
    def removeDuplicates_optimal(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0

        j = 0

        for i in range(1, n):

            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1


# =========================================================
# DRIVER CODE
# =========================================================

test_cases = [

    # normal case
    [1,1,2],

    # multiple duplicates
    [0,0,1,1,1,2,2,3,3,4],

    # already unique
    [1,2,3,4,5],

    # all same
    [7,7,7,7],

    # single element
    [1],

    # empty array
    [],

    # negative numbers
    [-3,-3,-2,-1,-1,0,0],

    # large duplicate blocks
    [1,1,1,1,2,2,2,3,3,4,4,4],

]


sol = Solution()

for arr in test_cases:

    print("\nOriginal Array:", arr)

    # ---------------- HashMap ----------------
    nums1 = arr.copy()

    k1 = sol.removeDuplicates_hashmap(nums1)

    print("HashMap Approach")
    print("Unique Count :", k1)
    print("Modified Array:", nums1[:k1])



    # ---------------- Optimal ----------------
    nums2 = arr.copy()

    k2 = sol.removeDuplicates_optimal(nums2)

    print("Optimal Two Pointer Approach")
    print("Unique Count :", k2)
    print("Modified Array:", nums2[:k2])

    print("-" * 50)