class Solution:
    def minInsertions(self, s: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minInsertions(s="(()))"))  # 1
    print(Solution().minInsertions(s="())"))  # 0
    print(Solution().minInsertions(s="))())("))  # 3
    print(Solution().minInsertions(s="(((((("))  # 12
    print(Solution().minInsertions(s=")))))))"))  # 5
