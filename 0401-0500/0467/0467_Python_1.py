class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        now_val, now_num = float("inf"), 0
        dp = [0] * 26
        for ch in p:
            v = ord(ch) - 97
            if v != (now_val + 1) % 26:
                now_val, now_num = v, 1
            else:
                now_val += 1
                now_num += 1
            dp[v] = max(dp[v], now_num)
        return sum(dp)


if __name__ == "__main__":
    print(Solution().findSubstringInWraproundString("a"))  # 1
    print(Solution().findSubstringInWraproundString("cac"))  # 2
    print(Solution().findSubstringInWraproundString("zab"))  # 6
