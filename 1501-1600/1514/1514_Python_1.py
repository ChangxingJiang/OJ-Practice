import collections
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        for i, edge in enumerate(edges):
            graph[edge[0]][edge[1]] = succProb[i]
            graph[edge[1]][edge[0]] = succProb[i]

        visited = {start: 1}
        queue = collections.deque([start])
        while queue:
            n1 = queue.popleft()
            for n2 in graph[n1]:
                p2 = visited[n1] * graph[n1][n2]
                if n2 not in visited or p2 > visited[n2]:
                    visited[n2] = p2
                    queue.append(n2)

        return visited[end] if end in visited else 0


if __name__ == "__main__":
    # 0.25000
    print(Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))

    # 0.30000
    print(Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2))

    # 0.00000
    print(Solution().maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2))
