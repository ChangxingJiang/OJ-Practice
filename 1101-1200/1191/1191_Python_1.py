from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        v1 = -10001
        t = -10001
        for n in arr:
            t = max(t + n, n)
            v1 = max(v1, t)

        if k == 1:
            return v1 % self._MOD if v1 > 0 else 0

        v2 = v1
        for n in arr:
            t = max(t + n, n)
            v2 = max(v2, t)

        if k == 2:
            return v2 % self._MOD if v2 > 0 else 0

        v3 = v2
        for n in arr:
            t = max(t + n, n)
            v3 = max(v3, t)

        if v2 == v3:
            return v3 % self._MOD if v3 > 0 else 0
        else:
            d = v3 - v2
            return (v2 + (k - 2) * d) % self._MOD


if __name__ == "__main__":
    print(Solution().kConcatenationMaxSum(arr=[1, 2], k=3))  # 9
    print(Solution().kConcatenationMaxSum(arr=[1, -2, 1], k=5))  # 2
    print(Solution().kConcatenationMaxSum(arr=[-1, -2], k=7))  # 0
