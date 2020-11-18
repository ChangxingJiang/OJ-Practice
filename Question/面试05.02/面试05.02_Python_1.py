class Solution:
    def printBin(self, num: float) -> str:
        now = 2
        ans = []
        while num and len(ans) < 32:
            val = 1 / now
            if num >= val:
                ans.append("1")
                num -= val
            else:
                ans.append("0")
            now *= 2
        if num:
            return "ERROR"
        else:
            return "0." + "".join(ans)


if __name__ == "__main__":
    print(Solution().printBin(0.625))  # 0.101
    print(Solution().printBin(0.1))  # ERROR
