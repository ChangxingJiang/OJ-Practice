class Solution:
    _TABLE = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }
    _JUMP = {
        "2": "6",
        "3": "6",
        "4": "6",
        "5": "6",
        "7": "8"
    }

    def confusingNumberII(self, N: int) -> int:
        ans = 0

        i = 1
        while i <= N:
            s = str(i)
            l, r = 0, len(s) - 1
            differ = False
            while l <= r:
                if s[l] not in self._TABLE:
                    i = int(s[:l] + self._JUMP[s[l]] + "".join(["0"] * (len(s) - l - 1)))
                    break
                if s[r] not in self._TABLE:
                    i = int(s[:r] + self._JUMP[s[r]] + "".join(["0"] * (len(s) - r - 1)))
                    break
                elif s[l] != self._TABLE[s[r]]:
                    differ = True
                l += 1
                r -= 1
            else:
                if differ:
                    ans += 1
                i += 1

        return ans


if __name__ == "__main__":
    print(Solution().confusingNumberII(10))  # 3
    print(Solution().confusingNumberII(20))  # 6
    print(Solution().confusingNumberII(100))  # 19

    print(Solution().confusingNumberII(174))  # 31
