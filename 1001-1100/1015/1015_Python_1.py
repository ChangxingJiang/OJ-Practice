class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1

        v = 1
        ans = 1
        while v % K != 0:
            v %= K
            v = v * 10 + 1
            ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().smallestRepunitDivByK(1))  # 1
    print(Solution().smallestRepunitDivByK(2))  # -1
    print(Solution().smallestRepunitDivByK(3))  # 3
