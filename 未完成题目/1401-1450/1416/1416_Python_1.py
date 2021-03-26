class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numberOfArrays(s="1000", k=10000))  # 1
    print(Solution().numberOfArrays(s="1000", k=10))  # 0
    print(Solution().numberOfArrays(s="1317", k=2000))  # 8
    print(Solution().numberOfArrays(s="2020", k=30))  # 1
    print(Solution().numberOfArrays(s="1234567890", k=90))  # 34
