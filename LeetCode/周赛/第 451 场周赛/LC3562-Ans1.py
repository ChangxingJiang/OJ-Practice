from typing import List


class TreeNode:
    def __init__(self):
        self.children = []


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # 初始化树结构
        self.node_list = [TreeNode() for i in range(n)]
        for u, v in hierarchy:
            self.node_list[u - 1].children.append(v - 1)

        # 初始化变量
        self.budget = budget
        self.present = present
        self.future = future

        _, stat2 = self.dfs(0)

        return max(stat2)

    def dfs(self, idx):
        """返回两个状态列表 stat1 和 stat2，长度均为 budget

        stat1[i] 表示，当直属上级购买了股票时，花费 i 预算时的最大收益
        stat2[i] 表示，当直属上级没有购买了股票时，花费 i 预算时的最大收益
        """
        node = self.node_list[idx]

        p2 = self.present[idx]  # 上级不买
        p1 = p2 // 2  # 上级购买
        f = self.future[idx]

        # 叶子节点的情况
        if not node.children:
            stat1 = [0] * (self.budget + 1)  # 上级购买
            stat2 = [0] * (self.budget + 1)  # 上级不买
            if f > p1 and p1 <= self.budget:
                stat1[p1] = f - p1
            if f > p2 and p2 <= self.budget:
                stat2[p2] = f - p2
            return stat1, stat2

        stat1 = [0] * (self.budget + 1)  # 当前节点买
        stat2 = [0] * (self.budget + 1)  # 当前节点不买

        for child in node.children:
            child_stat1, child_stat2 = self.dfs(child)

            new_stat1 = list(stat1)
            new_stat2 = list(stat2)
            for i in range(self.budget + 1):  # 当前子节点的购买金额
                for j in range(self.budget + 1 - i):  # 当前父节点的购买金额
                    new_stat1[i + j] = max(new_stat1[i + j], stat1[j] + child_stat1[i])  # 其他子节点购买 j，子节点购买 i
                    new_stat2[i + j] = max(new_stat2[i + j], stat2[j] + child_stat2[i])  # 其他子节点购买 j，子节点购买 i
            stat1 = new_stat1
            stat2 = new_stat2

        # print(idx, "中间:", stat1, stat2)

        final_stat1 = [0] * (self.budget + 1)  # 上级买
        final_stat2 = [0] * (self.budget + 1)  # 上级不买
        for i in range(self.budget + 1):
            # 当前节点买
            if i + p1 <= self.budget:
                final_stat1[i + p1] = max(final_stat1[i + p1], stat1[i] + f - p1)
            if i + p2 <= self.budget:
                final_stat2[i + p2] = max(final_stat2[i + p2], stat1[i] + f - p2)

            # 当前节点不买
            final_stat1[i] = max(final_stat1[i], stat2[i])
            final_stat2[i] = max(final_stat2[i], stat2[i])

        # print(idx, "最终:", final_stat1, final_stat2)

        return final_stat1, final_stat2


if __name__ == "__main__":
    print(Solution().maxProfit(n=2, present=[1, 2], future=[4, 3], hierarchy=[[1, 2]], budget=3))  # 5
    print(Solution().maxProfit(n=2, present=[3, 4], future=[5, 8], hierarchy=[[1, 2]], budget=4))  # 4
    print(Solution().maxProfit(n=3, present=[4, 6, 8], future=[7, 9, 11], hierarchy=[[1, 2], [1, 3]], budget=10))  # 10
    print(Solution().maxProfit(n=3, present=[5, 2, 3], future=[8, 5, 6], hierarchy=[[1, 2], [2, 3]], budget=7))  # 12

    # 测试用例
    print(Solution().maxProfit(n=2, present=[6, 11], future=[5, 48], hierarchy=[[1, 2]], budget=142))  # 42
    print(Solution().maxProfit(
        n=3,
        present=[6, 4, 23],
        future=[50, 48, 17],
        hierarchy=[[1, 3], [1, 2]],
        budget=28
    ))  # 96
