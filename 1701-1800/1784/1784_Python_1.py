class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        b1, b2 = False, False
        for ch in s:
            if not b1:
                if ch == "1":
                    b1 = True
            elif not b2:
                if ch == "0":
                    b2 = True
            else:
                if ch == "1":
                    return False
        return True


if __name__ == "__main__":
    print(Solution().checkOnesSegment("1001"))  # False
    print(Solution().checkOnesSegment("110"))  # True
