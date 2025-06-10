from typing import List

MOD = 10 ** 9 + 7


class Solution:

    def countPermutations(self, complexity: List[int]) -> int:
        # 无法解锁的情况
        if complexity[0] >= min(complexity[1:]):
            return 0

        # 然后计算 n - 1 的阶乘
        n = len(complexity)

        res = 1
        for i in range(2, n):
            res *= i
            res %= MOD

        return res


if __name__ == "__main__":
    print(Solution().countPermutations([1, 2, 3]))  # 2
    print(Solution().countPermutations([3, 3, 3, 4, 4, 4]))  # 0
