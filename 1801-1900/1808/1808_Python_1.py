class Solution:
    _MOD = 10 ** 9 + 7

    # 相当于找n个数，它们的和为primeFactors，求乘积的最大值
    def maxNiceDivisors(self, f: int) -> int:
        if f == 1:
            return 1

        a, b = divmod(f, 3)
        if b == 0:
            return pow(3, a, mod=self._MOD)
        elif b == 1:
            return pow(3, a - 1, mod=self._MOD) * 4 % self._MOD
        else:  # b==2
            return pow(3, a, mod=self._MOD) * 2 % self._MOD


if __name__ == "__main__":
    print(Solution().maxNiceDivisors(1))  # 1
    print(Solution().maxNiceDivisors(5))  # 6
    print(Solution().maxNiceDivisors(8))  # 18
    print(Solution().maxNiceDivisors(9))  # 27
    print(Solution().maxNiceDivisors(10))  # 36
