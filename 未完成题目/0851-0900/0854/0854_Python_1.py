class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().kSimilarity(A="ab", B="ba"))  # 1
    print(Solution().kSimilarity(A="abc", B="bca"))  # 2
    print(Solution().kSimilarity(A="abac", B="baca"))  # 2
    print(Solution().kSimilarity(A="aabc", B="abca"))  # 2
