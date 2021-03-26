import collections
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(dict)
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]

        ans_idx, ans_val = -1, n
        for city in range(n):
            visited = collections.Counter({city: 0})
            queue = collections.deque([(city, 0)])
            while queue:
                for _ in range(len(queue)):
                    city1, d1 = queue.popleft()
                    for city2 in graph[city1]:
                        d2 = d1 + graph[city1][city2]
                        if d2 <= distanceThreshold and (city2 not in visited or d2 < visited[city2]):
                            queue.append((city2, d2))
                            visited[city2] = d2
            if len(visited) <= ans_val:
                ans_idx, ans_val = city, len(visited)

        return ans_idx


if __name__ == "__main__":
    print(Solution().findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))  # 3
    print(Solution().findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
                                 distanceThreshold=2))  # 0
