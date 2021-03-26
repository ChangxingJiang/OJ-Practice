from typing import List


class Solution:
    _MOD = 1337

    def single_pow(self, a, k):
        if k == 0:
            return 1

        a %= self._MOD
        if k % 2 == 1:
            return a * self.single_pow(a, k - 1) % self._MOD
        else:
            res = self.single_pow(a, k // 2)
            return (res * res) % self._MOD

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        return self.single_pow(a, last) * self.single_pow(self.superPow(a, b), 10) % self._MOD


if __name__ == "__main__":
    print(Solution().superPow(a=2, b=[3]))  # 8
    print(Solution().superPow(a=2, b=[1, 0]))  # 1024
    print(Solution().superPow(a=1, b=[4, 3, 3, 8, 5, 2]))  # 1
    print(Solution().superPow(a=2147483647, b=[2, 0, 0]))  # 1198
