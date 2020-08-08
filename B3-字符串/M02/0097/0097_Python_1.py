class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))  # True
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))  # False
