from typing import List


def sub(a, b):
    """求点a到点b的向量"""
    return [b[0] - a[0], b[1] - a[1]]


def cross(a, b):
    """求向量a到向量b的向量叉积"""
    return a[0] * b[1] - a[1] * b[0]


class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        size = len(points)
        visited = [False] * size

        ans = []

        # 将最左侧的点作为出发点
        start = 0
        for i in range(size):
            if points[i][0] < points[start][0]:
                start = i
        ans.append(start)
        visited[start] = True

        for direct in direction:
            next = -1
            # 下一个转向方向为L，则当前这一步选择最右侧的点
            if direct == "L":
                for j in range(size):
                    if not visited[j]:
                        if next == -1 or cross(sub(points[start], points[j]), sub(points[start], points[next])) > 0:
                            next = j

            # 下一个转向方向为R，则当前这一步选择最左侧的点
            if direct == "R":
                for j in range(size):
                    if not visited[j]:
                        if next == -1 or cross(sub(points[start], points[j]), sub(points[start], points[next])) < 0:
                            next = j

            ans.append(next)
            visited[next] = True
            start = next

        # 将最后一个点添加到结果中
        for i in range(size):
            if not visited[i]:
                ans.append(i)

        return ans


if __name__ == "__main__":
    print(Solution().visitOrder(points=[[1, 1], [1, 4], [3, 2], [2, 1]], direction="LL"))  # [0,2,1,3]
    print(Solution().visitOrder(points=[[1, 3], [2, 4], [3, 3], [2, 1]], direction="LR"))  # [0,3,1,2]
