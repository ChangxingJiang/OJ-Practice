import collections
from typing import List


# 移动窗口、双端队列
# O(N)

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = None

        # 每个元素最多被遍历两次，添加一次，删除一次
        # 队列内单调递减

        queue = collections.deque([])
        for x2, y2 in points:
            # 移除队列中已经超出窗口的点
            while queue:
                x1, y1 = queue[0]
                if x1 < x2 - k:
                    queue.popleft()
                else:
                    break

            # print(x2, "DEL", "->", queue)

            # 如果队列中存在元素，计算当前的结果
            if queue:
                x1, y1 = queue[0]
                if queue[0] != 0:
                    value = y1 + y2 + (x2 - x1)
                    if ans is None or ans < value:
                        ans = value

            # 将当前结果加入等待区，并移除等待区开头所有小于当前结果的值
            while queue:
                x1, y1 = queue[-1]
                if (x2 - x1) + y1 <= y2:
                    queue.pop()
                else:
                    break
            queue.append((x2, y2))

            # print(x2, "ADD", "->", queue)

        return ans


if __name__ == "__main__":
    # 4
    print(Solution().findMaxValueOfEquation(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1))

    # 3
    print(Solution().findMaxValueOfEquation(points=[[0, 0], [3, 0], [9, 2]], k=3))

    # 38
    print(Solution().findMaxValueOfEquation(
        points=[[-16, 15], [-7, -18], [-4, 2], [1, 0], [7, 10], [9, -6], [14, 5], [15, 13], [16, -12], [20, 20]],
        k=8))
