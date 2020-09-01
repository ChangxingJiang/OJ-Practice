class Solution:
    def checkRecord(self, s: str) -> bool:
        return not s.count("A") >= 2 and not "LLL" in s


if __name__ == "__main__":
    print(Solution().checkRecord("PPALLP"))  # True
    print(Solution().checkRecord("PPALLL"))  # False
