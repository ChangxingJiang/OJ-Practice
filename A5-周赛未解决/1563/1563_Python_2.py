import functools
from typing import List


# 贪心算法
# O(NlogN) O(N)


class Solution:

    def stoneGameV(self, stoneValue: List[int]) -> int:

        @functools.lru_cache(None)
        def count(values):
            size = len(values)

            # 处理很小的情况
            if size == 0:
                return 0
            if size == 1:
                return 0
            if size == 2:
                return min(values)

            # 找到最有可能的情况
            total = sum(values)
            half = total // 2
            last = 0
            maybe = 0
            for i, stone in enumerate(values):
                last += stone
                if last >= half:
                    maybe = i
                    break

            # 扩展到最有可能的6种情况
            ans = []
            for test in range(max(0, maybe - 4), min(size, maybe + 4)):
                sum1 = sum(values[:test])
                sum2 = total - sum1
                if sum1 < sum2:
                    ans.append(sum1 + count(tuple(values[:test])))
                elif sum1 > sum2:
                    ans.append(sum2 + count(tuple(values[test:])))
                else:
                    ans.append(sum1 + count(tuple(values[:test])))
                    ans.append(sum2 + count(tuple(values[test:])))
            # print(values, "->", maybe, "->", max(ans))

            return max(ans)

        return count(tuple(stoneValue))


if __name__ == "__main__":
    print(Solution().stoneGameV(stoneValue=[6, 2, 3, 4, 5, 5]))  # 18
    print(Solution().stoneGameV(stoneValue=[7, 7, 7, 7, 7, 7, 7]))  # 28
    print(Solution().stoneGameV(stoneValue=[4]))  # 0
    print(Solution().stoneGameV(stoneValue=[2, 1, 1]))  # 3
    print(Solution().stoneGameV(stoneValue=[68, 75, 25, 50, 34, 29, 77, 1, 2, 69]))  # 304
    print(Solution().stoneGameV(stoneValue=[98, 77, 24, 49, 6, 12, 2, 44, 51, 96]))  # 330
