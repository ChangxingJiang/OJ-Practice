import collections
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = build_graph(dislikes)

        table = [0] * (N + 1)
        for m1, m2 in dislikes:
            if table[m1] * table[m2] > 0:
                return False
            if table[m1] != 0 or table[m2] != 0:
                continue

            table[m1] = 1

            now = -1
            queue = collections.deque([m1])
            while queue:
                for _ in range(len(queue)):
                    n1 = queue.popleft()
                    for n2 in graph[n1]:
                        if table[n2] == -now:
                            return False
                        elif table[n2] == 0:
                            table[n2] = now
                            queue.append(n2)
                now *= -1

        return True


if __name__ == "__main__":
    # True
    print(Solution().possibleBipartition(N=4, dislikes=[[1, 2], [1, 3], [2, 4]]))

    # False
    print(Solution().possibleBipartition(N=3, dislikes=[[1, 2], [1, 3], [2, 3]]))

    # False
    print(Solution().possibleBipartition(N=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
