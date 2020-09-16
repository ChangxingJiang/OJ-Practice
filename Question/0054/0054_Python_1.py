from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 处理空表的情况
        if not matrix or not matrix[0]:
            return []

        # 定义边缘位置
        top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        stat = 0
        x, y = 0, 0
        ans = []

        while top <= bottom and left <= right:
            ans.append(matrix[x][y])
            if stat == 0:  # 向右移动的状态
                if y < right:
                    y += 1
                else:
                    top += 1
                    stat = (stat + 1) % 4
                    x += 1
            elif stat == 1:  # 向下移动的状态
                if x < bottom:
                    x += 1
                else:
                    right -= 1
                    stat = (stat + 1) % 4
                    y -= 1
            elif stat == 2:  # 向左移动的状态
                if y > left:
                    y -= 1
                else:
                    bottom -= 1
                    stat = (stat + 1) % 4
                    x -= 1
            else:  # 向上移动的状态
                if x > top:
                    x -= 1
                else:
                    left += 1
                    stat = (stat + 1) % 4
                    y += 1

        return ans


if __name__ == "__main__":
    # [1,2,3,6,9,8,7,4,5]
    print(Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(Solution().spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
