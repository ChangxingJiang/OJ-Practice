from typing import List


class Solution:
    def __init__(self):
        self.dp = []  # 状态矩阵：dp[state]表示状态为完成状态state的课至少需要几个学期

    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 初始化状态矩阵
        self.dp = [-1] * (1 << (n + 1))
        self.dp[0] = 0

        # 计算每门课程的前置课程的状态
        pre_state = [0] * (n + 1)
        for c1, c2 in dependencies:
            pre_state[c2] |= (1 << c1)

        for state in range(1 << (n + 1)):
            # 如果当前课程状态不存在，则跳过当前课程状态
            if self.dp[state] == -1:
                continue

            # 寻找下一门可以学习的课程
            course = []
            for i in range(1, n + 1):
                # 如果这门课程已经被学过了
                if (state >> i) & 1 == 1:
                    continue

                # 如果这门课程的前置条件还没有被完成
                if (state & pre_state[i]) != pre_state[i]:
                    continue

                course.append(i)

            self.dfs(x=0, m=len(course), k=min(len(course), k), step=self.dp[state] + 1, state=state, course=course)
        return self.dp[-2]

    def dfs(self, x, m, k, step, state, course):
        """深度优先搜索

        :param x: 当前已经遍历到的下一门可以学习的课程坐标
        :param m: 下一个学期可以学习的课程数量
        :param k: 下一个学期可以学习的课程数量上限
        :param step: 当前的学期数量
        :param state: 当前课程学习情况
        :param course: 下一门可以学习的课程
        """
        # 剪枝条件:本学期已无法达到理论最高效的情况
        if m - x < k:
            return

        # 如果当前学期已经安排完成
        if x >= m or k == 0:
            if self.dp[state] == -1 or self.dp[state] > step:
                self.dp[state] = step
        else:
            self.dfs(x + 1, m, k - 1, step, state | (1 << course[x]), course)  # 深度优先搜索:选择当前课程
            self.dfs(x + 1, m, k, step, state, course)  # 深度优先搜索:不选择当前课程


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

    # 自制用例
    print(Solution().minNumberOfSemesters(n=6, dependencies=[[6, 1], [6, 2], [5, 3], [5, 4]], k=3))  # 3
