class Solution:
    def binaryGap(self, N: int) -> int:
        ans = 0
        now = -1
        while N > 0:
            if N & 1 == 1:
                if now != -1:
                    ans = max(ans, now)
                now = 0
            if now != -1:
                now += 1
            N = N >> 1
        return ans


if __name__ == "__main__":
    print(Solution().binaryGap(22))  # 2
    print(Solution().binaryGap(5))  # 2
    print(Solution().binaryGap(6))  # 1
    print(Solution().binaryGap(8))  # 0
