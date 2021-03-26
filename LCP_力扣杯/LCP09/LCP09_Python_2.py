import collections
from typing import List


class Solution:
    def minJump(self, jump: List[int]) -> int:
        size = len(jump)

        queue = collections.deque([0])
        step = 0  # 当前的步数

        visited = 0  # 当前已经访问到的位置
        while queue:
            # 累加当前步数
            step += 1

            # 处理当前广度优先搜索层
            for _ in range(len(queue)):
                n1 = queue.popleft()

                # 添加弹簧的终点
                n2 = n1 + jump[n1]
                if n2 >= size:
                    return step
                if n2 > visited:
                    queue.append(n2)

                # 向后的部分
                if n1 > visited:
                    for n2 in range(visited + 1, n1):
                        queue.append(n2)
                    visited = n1


if __name__ == "__main__":
    print(Solution().minJump(jump=[2, 5, 1, 1, 1, 1]))  # 3
    print(Solution().minJump(jump=[3, 7, 6, 1, 4, 3, 7, 8, 1, 2, 8, 5, 9, 8, 3, 2, 7, 5, 1, 1]))  # 6
