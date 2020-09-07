import collections
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans = 0

        # 转换边的存储格式
        # 处理所有已有3类型的连接还有1和2的连接的数量
        points = collections.defaultdict(dict)
        for edge in edges:
            t, p1, p2 = edge[0], edge[1], edge[2]
            if t == 3:
                if p2 not in points[p1]:
                    points[p1][p2] = 3
                    points[p2][p1] = 3
                elif points[p1][p2] == 1 or points[p1][p2] == 2:
                    ans += 1
                elif points[p1][p2] == 4:
                    points[p1][p2] = 3
                    points[p2][p1] = 3
                    ans += 2
            elif t == 1:
                if p2 not in points[p1]:
                    points[p1][p2] = 1
                    points[p2][p1] = 1
                elif points[p1][p2] == 3 or points[p1][p2] == 4:
                    ans += 1
                elif points[p1][p2] == 2:
                    points[p1][p2] = 4
                    points[p2][p1] = 4
            elif t == 2:
                if p2 not in points[p1]:
                    points[p1][p2] = 2
                    points[p2][p1] = 2
                elif points[p1][p2] == 3 or points[p1][p2] == 4:
                    ans += 1
                elif points[p1][p2] == 1:
                    points[p1][p2] = 4
                    points[p2][p1] = 4

        print("Step1:", ans, points)

        # 广度优先遍历(Type=3)
        # 处理额外多余的3类型连接
        visited_all = {1}
        now_point = {1}
        paths = set()
        while len(visited_all) < n and now_point:
            next_point = set()
            for p1 in now_point:
                for p2 in points[p1]:
                    if points[p1][p2] == 3:
                        if p2 not in visited_all:
                            next_point.add(p2)
                            visited_all.add(p2)
                            paths.add((p1, p2))
                        elif (p2, p1) not in paths:
                            ans += 1
            now_point = next_point

        print("Step2:", ans, visited_all)

        # 广度优先遍历(Type=4)
        # 处理额外多余的3类型连接
        now_point = visited_all.copy()
        paths = set()
        while now_point:
            next_point = set()
            for p1 in now_point:
                for p2 in points[p1]:
                    if points[p1][p2] == 4:
                        if p1 in visited_all and p2 in visited_all:
                            if (p2, p1) not in paths:
                                ans += 2
                            paths.add((p1, p2))
                        else:
                            next_point.add(p2)
                            visited_all.add(p2)
                            paths.add((p1, p2))
            now_point = next_point

        print("Step3:", ans, visited_all)

        # 广度优先遍历(Type=1)
        visited_1 = set()
        now_point = visited_all.copy()
        paths = set()
        while now_point:
            next_point = set()
            for p1 in now_point:
                for p2 in points[p1]:
                    if points[p1][p2] == 1:
                        if p1 in visited_all and p2 in visited_all:
                            ans += 0.5
                        elif p2 not in visited_all:
                            if p2 not in visited_1:
                                next_point.add(p2)
                                visited_1.add(p2)
                                paths.add((p1, p2))
                            elif (p2, p1) not in paths:
                                ans += 1
            now_point = next_point

        if len(visited_all) + len(visited_1) < n:
            return -1

        print("Step4:", ans, visited_all, visited_1)

        # 广度优先遍历(Type=2)
        visited_2 = set()
        now_point = visited_all.copy()
        paths = set()
        while now_point:
            next_point = set()
            for p1 in now_point:
                for p2 in points[p1]:
                    if points[p1][p2] == 2:
                        if p1 in visited_all and p2 in visited_all:
                            ans += 0.5
                        elif p2 not in visited_all:
                            if p2 not in visited_2:
                                next_point.add(p2)
                                visited_2.add(p2)
                                paths.add((p1, p2))
                            elif (p2, p1) not in paths:
                                ans += 1
            now_point = next_point

        if len(visited_all) + len(visited_2) < n:
            return -1

        print("Step5:", ans, visited_all, visited_1, visited_2)

        return int(ans)


if __name__ == "__main__":
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))  # 2
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))  # 0
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]))  # -1
    print(Solution().maxNumEdgesToRemove(n=2, edges=[[1, 1, 2], [2, 1, 2], [3, 1, 2]]))  # 2
    print(Solution().maxNumEdgesToRemove(n=13,
                                         edges=[[1, 1, 2], [2, 1, 3], [3, 2, 4], [3, 2, 5], [1, 2, 6], [3, 6, 7], [3, 7, 8], [3, 6, 9], [3, 4, 10],
                                                [2, 3, 11], [1, 5, 12], [3, 3, 13],
                                                [2, 1, 10], [2, 6, 11], [3, 5, 13], [1, 9, 12], [1, 6, 8], [3, 6, 13], [2, 1, 4], [1, 1, 13],
                                                [2, 9, 10], [2, 1, 6], [2, 10, 13], [2, 2, 9],
                                                [3, 4, 12], [2, 4, 7], [1, 1, 10], [1, 3, 7], [1, 7, 11], [3, 3, 12], [2, 4, 8], [3, 8, 9],
                                                [1, 9, 13], [2, 4, 10], [1, 6, 9], [3, 10, 13],
                                                [1, 7, 10], [1, 1, 11], [2, 4, 9], [3, 5, 11], [3, 2, 6], [2, 1, 5], [2, 5, 11], [2, 1, 7], [2, 3, 8],
                                                [2, 8, 9], [3, 4, 13], [3, 3, 8],
                                                [3, 3, 11], [2, 9, 11], [3, 1, 8], [2, 1, 8], [3, 8, 13], [2, 10, 11], [3, 1, 5], [1, 10, 11],
                                                [1, 7, 12], [2, 3, 5], [3, 1, 13], [2, 4, 11],
                                                [2, 3, 9], [2, 6, 9], [2, 1, 13], [3, 1, 12], [2, 7, 8], [2, 5, 6], [3, 1, 9], [1, 5, 10], [3, 2, 13],
                                                [2, 3, 6], [2, 2, 10], [3, 4, 11],
                                                [1, 4, 13], [3, 5, 10], [1, 4, 10], [1, 1, 8], [3, 3, 4], [2, 4, 6], [2, 7, 11], [2, 7, 10],
                                                [2, 3, 12], [3, 7, 11], [3, 9, 10], [2, 11, 13],
                                                [1, 1, 12], [2, 10, 12], [1, 7, 13], [1, 4, 11], [2, 4, 5], [1, 3, 10], [2, 12, 13], [3, 3, 10],
                                                [1, 6, 12], [3, 6, 10], [1, 3, 4], [2, 7, 9],
                                                [1, 3, 11], [2, 2, 8], [1, 2, 8], [1, 11, 13], [1, 2, 13], [2, 2, 6], [1, 4, 6], [1, 6, 11],
                                                [3, 1, 2], [1, 1, 3], [2, 11, 12], [3, 2, 11],
                                                [1, 9, 10], [2, 6, 12], [3, 1, 7], [1, 4, 9], [1, 10, 12], [2, 6, 13], [2, 2, 12], [2, 1, 11],
                                                [2, 5, 9], [1, 3, 8], [1, 7, 8], [1, 2, 12],
                                                [1, 5, 11], [2, 7, 12], [3, 1, 11], [3, 9, 12], [3, 2, 9], [3, 10, 11]]))  # 114
