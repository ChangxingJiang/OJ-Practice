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

        return max(stat2.values())

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
            stat1 = {0: 0}
            stat2 = {0: 0}
            if f > p1 and p1 <= self.budget:
                stat1[p1] = f - p1
            if f > p2 and p2 <= self.budget:
                stat2[p2] = f - p2
            # print(idx, stat1, stat2)
            return stat1, stat2

        stat1 = {0: 0}  # 当前节点买
        stat2 = {0: 0}  # 当前节点不买

        for child in node.children:
            child_stat1, child_stat2 = self.dfs(child)

            new_stat1 = stat1.copy()
            new_stat2 = stat2.copy()

            for k1, v1 in stat1.items():  # 当前子节点的购买金额
                for k2, v2 in child_stat1.items():  # 当前父节点的购买金额
                    if k1 + k2 <= self.budget:
                        new_stat1[k1 + k2] = max(new_stat1.get(k1 + k2, 0), v2 + v1)  # 其他子节点购买 j，子节点购买 i

            for k1, v1 in stat2.items():  # 当前子节点的购买金额
                for k2, v2 in child_stat2.items():  # 当前父节点的购买金额
                    if k1 + k2 <= self.budget:
                        new_stat2[k1 + k2] = max(new_stat2.get(k1 + k2, 0), v1 + v2)  # 其他子节点购买 j，子节点购买 i

            stat1 = new_stat1
            stat2 = new_stat2

        # print(idx, "中间:", stat1, stat2)

        final_stat1 = {0: 0}  # 上级买
        final_stat2 = {0: 0}  # 上级不买

        # 当前节点买
        for k1, v1 in stat1.items():
            if k1 + p1 <= self.budget:
                final_stat1[k1 + p1] = max(final_stat1.get(k1 + p1, 0), v1 + f - p1)
            if k1 + p2 <= self.budget:
                final_stat2[k1 + p2] = max(final_stat2.get(k1 + p2, 0), v1 + f - p2)

        # 当前节点不买
        for k1, v1 in stat2.items():
            if k1 <= self.budget:
                final_stat1[k1] = max(final_stat1.get(k1, 0), v1)
                final_stat2[k1] = max(final_stat2.get(k1, 0), v1)

        # print(idx, "最终:", final_stat1, final_stat2)

        return final_stat1, final_stat2


if __name__ == "__main__":
    print(Solution().maxProfit(n=2, present=[1, 2], future=[4, 3], hierarchy=[[1, 2]], budget=3))  # 5
    print(Solution().maxProfit(n=2, present=[3, 4], future=[5, 8], hierarchy=[[1, 2]], budget=4))  # 4
    print(Solution().maxProfit(n=3, present=[4, 6, 8], future=[7, 9, 11], hierarchy=[[1, 2], [1, 3]], budget=10))  # 10
    print(Solution().maxProfit(n=3, present=[5, 2, 3], future=[8, 5, 6], hierarchy=[[1, 2], [2, 3]], budget=7))  # 12

    # 测试用例
    print(Solution().maxProfit(n=2, present=[6, 11], future=[5, 48], hierarchy=[[1, 2]], budget=142))  # 42
    print(Solution().maxProfit(n=3, present=[6, 4, 23], future=[50, 48, 17], hierarchy=[[1, 3], [1, 2]],
                               budget=28))  # 96
    print(Solution().maxProfit(n=1, present=[45], future=[38], hierarchy=[], budget=115))  # 0
    print(Solution().maxProfit(n=5, present=[40, 8, 31, 16, 11], future=[42, 49, 12, 46, 37],
                               hierarchy=[[1, 4], [1, 5], [4, 3], [1, 2]], budget=19))  # 67
