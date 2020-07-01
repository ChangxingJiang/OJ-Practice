class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isLongPressedName("alex", "aaleex"))  # True
    print(Solution().isLongPressedName("saeed", "ssaaedd"))  # False
    print(Solution().isLongPressedName("leelee", "lleeelee"))  # True
    print(Solution().isLongPressedName("laiden", "laiden"))  # True
