import collections
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans = 0

        # 转换边的存储格式
        points = collections.defaultdict(dict)
        for edge in edges:
            t, p1, p2 = edge[0], edge[1], edge[2]
            if t == 3:
                if p2 not in points[p1]:
                    points[p1][p2] = 3
                    points[p2][p1] = 3
                elif points[p1][p2] == 1 or points[p1][p2] == 2:
                    ans += 1
                elif points[p1][p2] == 3:
                    ans += 2
            elif t == 1:
                if p2 not in points[p1]:
                    points[p1][p2] = 1
                    points[p2][p1] = 1
                elif points[p1][p2] == 3:
                    ans += 1
                elif points[p1][p2] == 2:
                    points[p1][p2] = 3
                    points[p2][p1] = 3
            elif t == 2:
                if p2 not in points[p1]:
                    points[p1][p2] = 2
                    points[p2][p1] = 2
                elif points[p1][p2] == 3:
                    ans += 1
                elif points[p1][p2] == 1:
                    points[p1][p2] = 3
                    points[p2][p1] = 3

        # 广度优先遍历(Alice)
        delete1 = set()
        visited = {1}
        now_point = {1}
        while len(visited) < n and now_point:
            print(now_point, visited)
            next_point = set()
            for p1 in now_point:
                for p2 in points[p1]:
                    print(p1, p2)
                    if points[p1][p2] == 1 or points[p1][p2] == 3:
                        if p2 not in visited:
                            next_point.add(p2)
                            visited.add(p2)
                        else:
                            delete1.add((p1, p2))
            now_point = next_point

        # 广度优先遍历(Bob)
        delete2 = set()
        visited = {1}
        now_point = {1}
        while len(visited) < n and now_point:
            next_point = set()
            for p1 in now_point:
                for p2 in points[p1]:
                    if points[p1][p2] == 2 or points[p1][p2] == 3:
                        if p2 not in visited:
                            next_point.add(p2)
                            visited.add(p2)
                        else:
                            delete2.add((p1, p2))
            now_point = next_point

        print(ans, delete1, delete2)

        return ans + len(delete1 & delete2)


if __name__ == "__main__":
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))  # 2
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))  # 0
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]))  # -1
    print(Solution().maxNumEdgesToRemove(n=2, edges=[[1, 1, 2], [2, 1, 2], [3, 1, 2]]))  # 2
