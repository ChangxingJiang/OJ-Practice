class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))  # True
    print(Solution().isValidSerialization("1,#"))  # False
    print(Solution().isValidSerialization("9,#,#,1"))  # False
