import collections
from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # ---------- 构造图 ----------
        graph_in = collections.defaultdict(set)
        graph_out = collections.defaultdict(set)
        for edge in prerequisites:
            graph_out[edge[0]].add(edge[1])
            graph_in[edge[1]].add(edge[0])

        # ---------- 拓扑排序 ----------
        count = [0] * n
        # 统计所有节点的入射边
        for idx in graph_in:
            count[idx] = len(graph_in[idx])

        # 初始节点
        queue = collections.deque()
        for idx in range(len(count)):
            if count[idx] == 0:
                queue.append(idx)

        table = [set() for _ in range(n)]

        # 拓扑排序
        while queue:
            idx1 = queue.pop()
            for idx2 in graph_out[idx1]:
                table[idx2] |= {idx1}
                table[idx2] |= table[idx1]
                count[idx2] -= 1
                if count[idx2] == 0:
                    queue.append(idx2)

        ans = []
        for idx1, idx2 in queries:
            ans.append(idx1 in table[idx2])
        return ans


if __name__ == "__main__":
    # [False,True]
    print(Solution().checkIfPrerequisite(n=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))

    # [False,False]
    print(Solution().checkIfPrerequisite(n=2, prerequisites=[], queries=[[1, 0], [0, 1]]))

    # [True,True]
    print(Solution().checkIfPrerequisite(n=3, prerequisites=[[1, 2], [1, 0], [2, 0]],
                                         queries=[[1, 0], [1, 2]]))

    # [False,True]
    print(Solution().checkIfPrerequisite(n=3, prerequisites=[[1, 0], [2, 0]], queries=[[0, 1], [2, 0]]))

    # [True,False,True,False]
    print(Solution().checkIfPrerequisite(n=5,
                                         prerequisites=[[0, 1], [1, 2], [2, 3], [3, 4]],
                                         queries=[[0, 4], [4, 0], [1, 3], [3, 0]]))

    # [true, false, true, true, true, true, true, true, false, false, true, true, false, false, true, true, true, true, false, false, true, false, true, false, true, false, true, true, false, true, true, false, false, true, false, false, true, true, true, false]
print(Solution().checkIfPrerequisite(n=7,
                                     prerequisites=[[2, 3], [2, 1], [2, 0], [3, 4], [3, 6], [5, 1], [5, 0], [1, 4],
                                                    [1, 0], [4, 0], [0, 6]],
                                     queries=[[3, 0], [6, 4], [5, 6], [2, 6], [2, 3], [5, 6], [4, 0], [2, 6],
                                              [3, 5], [5, 3], [1, 6], [1, 0], [3, 5], [6, 5], [2, 3], [3, 0],
                                              [3, 4], [3, 4], [2, 5], [0, 3], [4, 0], [6, 4], [5, 0], [6, 5],
                                              [5, 6], [6, 5], [1, 0], [3, 4], [1, 5], [1, 4], [3, 6], [0, 1],
                                              [1, 2], [5, 1], [5, 3], [5, 3], [3, 4], [5, 4], [5, 4], [5, 3]]))
