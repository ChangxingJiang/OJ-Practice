import collections
from typing import List


class DSU:
    def __init__(self, n: int):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i: int):
        """查询i所属的连通分支"""
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i: int, j: int):
        """合并i和j的连通分支"""
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]

    def __repr__(self):
        return str(len(self.array)) + ":" + str(self.array)


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 并查集计算连通分支
        # O(N+D)
        dsu = DSU(n)
        for c1, c2 in dependencies:
            dsu.union(c1 - 1, c2 - 1)
        branches = collections.defaultdict(set)
        for i in range(n):
            branches[dsu.find(i)].add(i)

        # 构造图+计算每个节点的父节点数量
        # O(N+D)
        graph = collections.defaultdict(set)
        count = collections.Counter()
        for c1, c2 in dependencies:
            graph[c1 - 1].add(c2 - 1)
            count[c2 - 1] += 1

        # 计算每个连通分支的课程关系情况（拓扑排序）
        # O(N+D)
        actual_needs = []
        for branch in branches.values():
            need = collections.deque()
            queue = collections.deque([i for i in branch if count[i] == 0])
            while queue:
                need.append(len(queue))
                for _ in range(len(queue)):
                    c1 = queue.popleft()
                    for c2 in graph[c1]:
                        count[c2] -= 1
                        if count[c2] == 0:
                            queue.append(c2)

            actual_needs.append(need)

        print(actual_needs)

        # 计算实际最小学期数
        # O(N^2logN)
        actual_list = [0] * n
        now = 0
        while actual_needs:
            # 按每个连通分支的课程数排序连通分支，优先学习课程数多的连通分支
            actual_needs.sort(key=lambda x: (len(x), sum(x)), reverse=True)

            # 尽可能多地向当前学期安排课程
            finish = []
            for i in range(len(actual_needs)):
                # 当前连通分支第1学习的课程可以都被安排在本学期
                if actual_needs[i][0] <= (k - actual_list[now]):
                    actual_list[now] += actual_needs[i].popleft()
                    if not actual_needs[i]:
                        finish.append(i)

                # 当前连通分支第1阶段的课程无法都被安排在本学期
                else:
                    actual_needs[i][0] -= (k - actual_list[now])
                    actual_list[now] = k
                    break

            # 无论当前学期是否已经安排满，都开始安排下一个学期
            now += 1

            # 移除已经学完的连通分支
            while finish:
                actual_needs.pop(finish.pop())

            print(actual_list, actual_needs)

        return now


if __name__ == "__main__":
    print(Solution().minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))  # 3

    print(Solution().minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))  # 4

    print(Solution().minNumberOfSemesters(n=11, dependencies=[], k=2))  # 6

    print(Solution().minNumberOfSemesters(n=6, dependencies=[[1, 6], [2, 6], [3, 5], [4, 5]], k=3))  # 3

    print(Solution().minNumberOfSemesters(n=11, dependencies=[[1, 2], [2, 3], [3, 4], [5, 8], [5, 9], [5, 10], [5, 11],
                                                              [6, 8], [6, 9], [6, 10], [6, 11], [7, 8], [7, 9], [7, 10],
                                                              [7, 11]], k=3))  # 4

    print(Solution().minNumberOfSemesters(n=12, dependencies=[[11, 10], [6, 3], [2, 5], [9, 2], [4, 12], [8, 7], [9, 5],
                                                              [6, 2], [7, 2], [7, 4], [9, 3], [11, 1], [4, 3]],
                                          k=3))  # 4
