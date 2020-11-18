import collections
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = build_graph(flights)

        visited = collections.Counter({src: 0})

        ans = float("inf")
        now_city = collections.deque([(src, 0)])
        while K >= 0:
            for _ in range(len(now_city)):
                city, cost1 = now_city.popleft()
                for near, cost2 in graph[city].items():
                    cost = cost1 + cost2
                    if near == dst and cost < ans:
                        ans = cost
                    elif (near not in visited or visited[near] > cost) and cost < ans:
                        now_city.append((near, cost))
                        visited[near] = cost

            K -= 1

        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    # 200
    print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=1))

    # 500
    print(Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=0))
