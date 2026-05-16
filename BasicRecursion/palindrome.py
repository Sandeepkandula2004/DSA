class Solution:
    def isPalindrome(self, s: str, i=0, j=None) -> bool:

        if j is None:
            j = len(s) - 1

        if i > j:
            return True

        if not s[i].isalnum():
            return self.isPalindrome(s, i + 1, j)

        if not s[j].isalnum():
            return self.isPalindrome(s, i, j - 1)

        if s[i].lower() != s[j].lower():
            return False

        return self.isPalindrome(s, i + 1, j - 1)


obj = Solution()

test_cases = [
    "",
    "a",
    "aa",
    "ab",
    "madam",
    "racecar",
    "A man, a plan, a canal: Panama",
    "race a car",
    "No lemon, no melon",
    "Was it a car or a cat I saw?",
    "12321",
    "123abccba321",
    "0P",
    ".,",
    "Able was I ere I saw Elba"
]

for i, s in enumerate(test_cases, 1):
    result = obj.isPalindrome(s)

    print(f"Test Case {i}")
    print("Input :", s)
    print("Output:", result)
    print()