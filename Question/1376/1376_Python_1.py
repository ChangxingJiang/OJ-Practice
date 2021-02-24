import collections
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(set)
        for i, m in enumerate(manager):
            graph[m].add(i)

        queue = collections.deque([(headID, 0)])
        ans = 0
        while queue:
            n1, t1 = queue.popleft()
            if graph[n1]:
                t2 = t1 + informTime[n1]
                ans = max(ans, t2)
                for n2 in graph[n1]:
                    queue.append((n2, t2))
        return ans


if __name__ == "__main__":
    print(Solution().numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]))  # 0
    print(Solution().numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))  # 1
    print(
        Solution().numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]))  # 21
    print(Solution().numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                                  informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))  # 3
    print(Solution().numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]))  # 1076
