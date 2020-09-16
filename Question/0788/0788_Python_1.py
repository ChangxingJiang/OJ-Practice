class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        for i in range(1, N + 1):
            s = str(i)
            n = ""
            for c in s:
                if c in ["0", "1", "8"]:
                    n += c
                elif c == "5":
                    n += "2"
                elif c == "2":
                    n += "5"
                elif c == "6":
                    n += "9"
                elif c == "9":
                    n += "6"
                else:
                    break
            else:
                if int(n) != i:
                    ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().rotatedDigits(10))  # 4
