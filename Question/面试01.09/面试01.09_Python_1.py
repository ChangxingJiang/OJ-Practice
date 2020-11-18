class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        elif not s2:
            return False
        return s2 in s1 * 3


if __name__ == "__main__":
    print(Solution().isFlipedString(s1="waterbottle", s2="erbottlewat"))  # True
    print(Solution().isFlipedString(s1="aa", s2="aba"))  # False
