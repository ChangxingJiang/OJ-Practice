from typing import List


# 贪心算法
# O(NlogN) O(N)


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        if len(stoneValue) == 1:
            return 0
        if len(stoneValue) == 2:
            return min(stoneValue)

        total = sum(stoneValue)
        half = total / 2

        last = 0
        for i, stone in enumerate(stoneValue):
            if last + stone == half:
                return (last + stone) + max(self.stoneGameV(stoneValue[:i + 1]), self.stoneGameV(stoneValue[i + 1:]))
            elif last + stone > half:
                if half - last < (last + stone) - half:
                    return last + self.stoneGameV(stoneValue[:i])
                elif half - last > (last + stone) - half:
                    return (total - (last + stone)) + self.stoneGameV(stoneValue[i + 1:])
                else:
                    return max(
                        last + self.stoneGameV(stoneValue[:i]),
                        (total - (last + stone)) + self.stoneGameV(stoneValue[i + 1:])
                    )

            last += stone


if __name__ == "__main__":
    print(Solution().stoneGameV(stoneValue=[6, 2, 3, 4, 5, 5]))  # 18
    print(Solution().stoneGameV(stoneValue=[7, 7, 7, 7, 7, 7, 7]))  # 28
    print(Solution().stoneGameV(stoneValue=[4]))  # 0
    print(Solution().stoneGameV(stoneValue=[2, 1, 1]))  # 0
    print(Solution().stoneGameV(stoneValue=[68, 75, 25, 50, 34, 29, 77, 1, 2, 69]))  # 304
