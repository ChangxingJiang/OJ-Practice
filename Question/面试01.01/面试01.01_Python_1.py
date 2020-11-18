class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))


if __name__ == "__main__":
    print(Solution().isUnique("leetcode"))  # False
    print(Solution().isUnique("abc"))  # True
