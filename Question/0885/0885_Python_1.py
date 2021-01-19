from typing import List


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 定义边缘位置
        top, bottom, left, right = r0, r0, c0, c0 + 1
        stat = 0
        x, y = r0, c0

        ans = []

        while len(ans) < R * C:
            if 0 <= x < R and 0 <= y < C:
                ans.append([x, y])
            if stat == 0:  # 向右移动的状态
                if y < right:
                    y += 1
                else:
                    bottom += 1
                    stat = 1
                    x += 1
            elif stat == 1:  # 向下移动的状态
                if x < bottom:
                    x += 1
                else:
                    left -= 1
                    stat = 2
                    y -= 1
            elif stat == 2:  # 向左移动的状态
                if y > left:
                    y -= 1
                else:
                    top -= 1
                    stat = 3
                    x -= 1
            else:  # 向上移动的状态
                if x > top:
                    x -= 1
                else:
                    right += 1
                    stat = 0
                    y += 1

        return ans


if __name__ == "__main__":
    # [[0,0],[0,1],[0,2],[0,3]]
    print(Solution().spiralMatrixIII(R=1, C=4, r0=0, c0=0))

    # [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    print(Solution().spiralMatrixIII(R=5, C=6, r0=1, c0=4))
