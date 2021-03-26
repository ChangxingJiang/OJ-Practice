# 贪心算法

import bisect
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 计算翻越高度及翻越数量
        marks = [0]  # 翻越数量
        tasks = [0]  # 翻越高度
        last = heights[0]
        for i in range(1, len(heights)):
            height = heights[i]
            if height <= last:
                marks[-1] = i
            else:
                tasks.append(height - last)
                marks.append(i)
            last = height

        # print(marks, tasks)

        # 贪心攀爬
        now = []  # 当前的需要搭梯子的排序的最大值
        # total = 0  # 当前用砖块的总值
        for idx, task in enumerate(tasks):
            bisect.insort_right(now, task)

            if ladders > 0:
                if len(now) > ladders and sum(now[:-ladders]) > bricks:
                    return marks[len(now) - 2]
            else:
                if sum(now) > bricks:
                    return marks[len(now) - 2]

            # print(now)

        return marks[-1]


if __name__ == "__main__":
    print(Solution().furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))  # 4
    print(Solution().furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))  # 7
    print(Solution().furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))  # 3
    print(Solution().furthestBuilding(heights=[1, 2], bricks=0, ladders=0))  # 0
