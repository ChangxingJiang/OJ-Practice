class Solution:
    def reverseBits(self, num: int) -> int:
        last, now = 0, 0
        ans = 0
        for i in range(32):
            if num & (1 << i):
                now += 1
            else:
                ans = max(ans, last + now + 1)
                last, now = now, 0
        ans = max(ans, last + now + 1)
        return min(ans, 32)


if __name__ == "__main__":
    # print(["1" if (-2) & (1 << i) else "0" for i in range(32)])
    # print(["1" if (-1) & (1 << i) else "0" for i in range(32)])
    print(Solution().reverseBits(1775))  # 8
    print(Solution().reverseBits(7))  # 4
    print(Solution().reverseBits(0))  # 1
    print(Solution().reverseBits(-1))  # 32
    print(Solution().reverseBits(-2))  # 32
