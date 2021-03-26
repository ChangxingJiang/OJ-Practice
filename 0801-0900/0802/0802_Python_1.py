import collections
from typing import List


class Solution:
    def eventualSafeNodes(self, graph1: List[List[int]]) -> List[int]:
        size = len(graph1)

        ans = []

        count = collections.Counter()
        queue = collections.deque()
        graph2 = [[] for _ in range(size)]  # 入度图
        for i in range(size):
            count[i] = len(graph1[i])
            for j in graph1[i]:
                graph2[j].append(i)
            if count[i] == 0:
                queue.append(i)
                ans.append(i)

        while queue:
            i1 = queue.popleft()
            for i2 in graph2[i1]:
                count[i2] -= 1
                if count[i2] == 0:
                    queue.append(i2)
                    ans.append(i2)

        ans.sort()
        return ans


if __name__ == "__main__":
    # [2,4,5,6]
    print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
