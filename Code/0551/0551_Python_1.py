class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2:
            return False
        if "LLL" in s:
            return False
        return True


if __name__ == "__main__":
    print(Solution().checkRecord("PPALLP"))  # True
    print(Solution().checkRecord("PPALLL"))  # False
