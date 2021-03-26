class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for c in s:
            if c == "L":
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
                if c == "A":
                    absent += 1
                    if absent >= 2:
                        return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().checkRecord("PPALLP"))  # True
    print(Solution().checkRecord("PPALLL"))  # False
