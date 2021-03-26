from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        size = len(stones)

        max_val = stones[-1] - stones[0] + 1 - size - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)

        min_val = max_val
        l = 0
        num = 0
        for r in range(size):
            num += 1
            while stones[r] - stones[l] + 1 > size:
                l += 1
                num -= 1

            # 处理特殊情况：3,4,5,6,10
            if size - num == 1 and stones[r] - stones[l] + 1 == size - 1:
                min_val = min(min_val, 2)
            else:
                min_val = min(min_val, size - num)

        return [min_val, max_val]


if __name__ == "__main__":
    print(Solution().numMovesStonesII([7, 4, 9]))  # [1,2]
    print(Solution().numMovesStonesII([6, 5, 4, 3, 10]))  # [2,3]
    print(Solution().numMovesStonesII([100, 101, 104, 102, 103]))  # [0,0]
