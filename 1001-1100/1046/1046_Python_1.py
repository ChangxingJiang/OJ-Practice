from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone1 = stones.pop(-1)
            stone2 = stones.pop(-1)
            new_stone = stone1 - stone2

            idx1 = 0
            idx2 = len(stones)
            while idx1 < idx2:
                mid = (idx1 + idx2) // 2
                if new_stone > stones[mid]:
                    idx1 = mid + 1
                elif new_stone < stones[mid]:
                    idx2 = mid
                else:
                    idx1 = mid
                    break
            stones.insert(idx1, new_stone)

        return stones[0]


if __name__ == "__main__":
    print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))  # 1
    print(Solution().lastStoneWeight([2, 2]))  # 1
    print(Solution().lastStoneWeight([15, 14]))  # 1
    print(Solution().lastStoneWeight(
        [434, 667, 378, 919, 212, 902, 240, 257, 208, 996, 411, 222, 557, 634, 425, 949, 755, 833, 785, 886, 40, 159,
         932, 157, 764, 916, 85, 300, 130, 278]))  # 1
