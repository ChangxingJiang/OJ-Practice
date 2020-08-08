class Solution:
    def isValid(self, S: str) -> bool:
        last = None
        while last != len(S):
            last = len(S)
            S = S.replace("abc", "")
        return not S


if __name__ == "__main__":
    print(Solution().isValid("aabcbc"))  # True
    print(Solution().isValid("abcabcababcc"))  # True
    print(Solution().isValid("abccba"))  # False
    print(Solution().isValid("cababc"))  # False
