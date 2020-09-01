class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2))  # 4
    print(Solution().getLengthOfOptimalCompression(s="aabbaa", k=2))  # 2
    print(Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0))  # 3
