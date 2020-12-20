class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))  # 3
    print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))  # 3
    print(Solution().longestCommonSubsequence(text1="abc", text2="def"))  # 0
