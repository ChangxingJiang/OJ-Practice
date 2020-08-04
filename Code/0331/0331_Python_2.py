class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        idx = 0
        while slot > -1 and idx < len(preorder):
            if preorder[idx] == ",":
                slot += 1
            elif preorder[idx] == "#":
                slot -= 2
            idx += 1
        return slot == -1 and idx == len(preorder)


if __name__ == "__main__":
    print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))  # True
    print(Solution().isValidSerialization("1,#"))  # False
    print(Solution().isValidSerialization("9,#,#,1"))  # False
    print(Solution().isValidSerialization("1,#,#,#,#"))  # False
    print(Solution().isValidSerialization("#,#"))  # False
    print(Solution().isValidSerialization("#"))  # True
    print(Solution().isValidSerialization("1"))  # False
    print(Solution().isValidSerialization("#,#,3,5,#"))  # False
