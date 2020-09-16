class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lst = set()
        for i in range(len(s) - k + 1):
            lst.add(s[i:i + k])
        return len(lst) == 2 ** k


if __name__ == "__main__":
    print(Solution().hasAllCodes(s="00110110", k=2))  # True
    print(Solution().hasAllCodes(s="00110", k=2))  # True
    print(Solution().hasAllCodes(s="0110", k=1))  # True
    print(Solution().hasAllCodes(s="0110", k=2))  # False
    print(Solution().hasAllCodes(s="0000000001011100", k=4))  # False
