from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        visited = {0}

        while len(visited) < n:
            for city1, city2 in connections:
                if city2 in visited:
                    visited.add(city1)
                elif city1 in visited:
                    ans += 1
                    visited.add(city2)

        return ans


if __name__ == "__main__":
    # 3
    print(Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))

    # 2
    print(Solution().minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))

    # 0
    print(Solution().minReorder(n=3, connections=[[1, 0], [2, 0]]))
