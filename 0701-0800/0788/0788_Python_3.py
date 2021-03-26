class Solution:
    def rotatedDigits(self, N: int) -> int:
        d7 = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "2",
            "4": "2",
            "5": "3",
            "6": "4",
            "7": "4",
            "8": "5",
            "9": "6"
        }
        o7 = {"3", "4", "7"}
        d3 = {
            "0": "0",
            "1": "1",
            "2": "1",
            "3": "1",
            "4": "1",
            "5": "1",
            "6": "1",
            "7": "1",
            "8": "2",
            "9": "2"
        }
        o3 = {"2", "3", "4", "5", "6", "7", "9"}

        S = str(N)
        S7 = S3 = ""
        off = False
        for s in S:
            if off:
                S3 += "2"
            else:
                off = s in o3
                S3 += d3[s]

        off = False
        for s in S:
            if off:
                S7 += "6"
            else:
                off = s in o7
                S7 += d7[s]

        return int(S7, base=7) - int(S3, base=3)


if __name__ == "__main__":
    print(Solution().rotatedDigits(10))  # 4
    print(Solution().rotatedDigits(11))  # 4
    print(Solution().rotatedDigits(12))  # 5
    print(Solution().rotatedDigits(13))  # 5
    print(Solution().rotatedDigits(100))  # 40
    print(Solution().rotatedDigits(112))  # 45
    print(Solution().rotatedDigits(113))  # 45
    print(Solution().rotatedDigits(114))  # 45
    print(Solution().rotatedDigits(115))  # 46
    print(Solution().rotatedDigits(116))  # 47
    print(Solution().rotatedDigits(117))  # 47
    print(Solution().rotatedDigits(118))  # 47
    print(Solution().rotatedDigits(119))  # 48
    print(Solution().rotatedDigits(120))  # 49
    print(Solution().rotatedDigits(125))  # 52
    print(Solution().rotatedDigits(150))  # 56
    print(Solution().rotatedDigits(200))  # 81
    print(Solution().rotatedDigits(857))  # 247
