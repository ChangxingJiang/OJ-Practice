from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        size = len(heights)

        def go(now, brick, ladder):
            # 尽可能地向前走
            while now < size - 1 and heights[now] >= heights[now + 1]:
                now += 1

            # 处理已经走到尽头的情况
            if now == size - 1:
                return now

            # 处理还没有走到尽头的情况
            height = heights[now + 1] - heights[now]

            if brick < height:
                if ladder == 0:
                    # 砖块不够且没有梯子的情况
                    return now
                else:
                    # 砖块不够但有梯子的情况
                    return go(now + 1, brick, ladder - 1)
            else:
                if ladder == 0:
                    # 砖块够但没有梯子的情况
                    return go(now + 1, brick - height, ladder)
                else:
                    # 砖块够且有梯子的情况
                    return max(
                        go(now + 1, brick, ladder - 1),
                        go(now + 1, brick - height, ladder)
                    )

        return go(0, bricks, ladders)


if __name__ == "__main__":
    print(Solution().furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))  # 4
    print(Solution().furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))  # 7
    print(Solution().furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))  # 3
