from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []

        height, width = len(obstacleGrid), len(obstacleGrid[0])

        visited = {(0, 0)}
        path = [(0, 0)]

        def dfs():
            x, y = path[-1]

            # 检查是否已走到终点
            if x == height - 1 and y == width - 1:
                self.ans = list(path)

            else:
                # 尝试向下走
                if x < height - 1 and obstacleGrid[x + 1][y] != 1 and (x + 1, y) not in visited:
                    path.append((x + 1, y))
                    visited.add((x + 1, y))
                    dfs()
                    path.pop()

                # 尝试向右走
                if y < width - 1 and obstacleGrid[x][y + 1] != 1 and (x, y + 1) not in visited:
                    path.append((x, y + 1))
                    visited.add((x, y + 1))
                    dfs()
                    path.pop()

                # # 尝试向上走
                # if x > 0 and obstacleGrid[x - 1][y] != 1 and (x - 1, y) not in visited:
                #     path.append((x - 1, y))
                #     visited.add((x - 1, y))
                #     dfs()
                #     path.pop()
                #
                # # 尝试向左走
                # if y > 0 and obstacleGrid[x][y - 1] != 1 and (x, y - 1) not in visited:
                #     path.append((x, y - 1))
                #     visited.add((x, y - 1))
                #     dfs()
                #     path.pop()

        dfs()

        return self.ans


if __name__ == "__main__":
    # [[0,0],[0,1],[0,2],[1,2],[2,2]]
    print(Solution().pathWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))

    # []
    print(Solution().pathWithObstacles([[1]]))
