from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n0, n1, total = 1, 0, 0
        for n in arr:
            total += n
            if total % 2 == 1:
                ans += n0
            else:
                ans += n1  # 前面有n1-1个，自己是1个
            ans %= self._MOD
            if total % 2 == 0:
                n0 += 1
            else:
                n1 += 1
        return ans


if __name__ == "__main__":
    print(Solution().numOfSubarrays([1, 3, 5]))  # 4
    print(Solution().numOfSubarrays([2, 4, 6]))  # 0
    print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))  # 16
    print(Solution().numOfSubarrays([100, 100, 99, 99]))  # 4
    print(Solution().numOfSubarrays([7]))  # 1
