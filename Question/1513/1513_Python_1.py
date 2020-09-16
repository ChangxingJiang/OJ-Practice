class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        now = 0
        ans = 0
        for ch in s:
            if ch == "1":
                now += 1
                ans += now
            else:
                now = 0
        return ans % MOD


if __name__ == "__main__":
    print(Solution().numSub(s="0110111"))  # 9
    print(Solution().numSub(s="101"))  # 2
    print(Solution().numSub(s="111111"))  # 21
    print(Solution().numSub(s="000"))  # 0
