from typing import List

MOD = 10 ** 9 + 7


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.children = []


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        # 构造树结构
        n = len(vals)
        nodes = [TreeNode(val) for val in vals]
        for i in range(n):
            p = par[i]
            if p != -1:
                nodes[p].children.append(nodes[i])

        # 计算每个数的状态压缩值
        self.stat_hash = {}
        for val in vals:
            stat = 0
            for ch in str(val):
                v = 1 << int(ch)
                if stat & v:
                    stat = -1
                    break
                stat |= v
            self.stat_hash[val] = stat

        self.result = 0

        # 开始遍历树结构
        self.dfs(nodes[0])

        return self.result

    def dfs(self, node):
        value = node.value  # 当前节点值
        stat = self.stat_hash[value]  # 当前节点状态

        # 叶子节点
        if not node.children:
            if stat >= 0:
                self.result = (self.result + value) % MOD
                return {stat: value}
            return {}

        # 合并所有叶子节点
        stat_value_hash = self.dfs(node.children[0])
        for i in range(1, len(node.children)):
            new_stat_value_hash = stat_value_hash.copy()
            stat_value_hash_2 = self.dfs(node.children[i])
            for k2, v2 in stat_value_hash_2.items():
                new_stat_value_hash[k2] = max(new_stat_value_hash.get(k2, 0), v2)
                for k1, v1 in stat_value_hash.items():
                    if not k1 & k2:
                        new_stat_value_hash[k1 | k2] = max(new_stat_value_hash.get(k1 | k2, 0), v1 + v2)
            stat_value_hash = new_stat_value_hash

        # 将叶子节点与当前节点合并
        if stat >= 0:
            new_stat_value_hash = stat_value_hash.copy()
            new_stat_value_hash[stat] = max(new_stat_value_hash.get(stat, 0), value)
            for k1, v1 in stat_value_hash.items():
                if not k1 & stat:
                    new_stat_value_hash[k1 | stat] = max(new_stat_value_hash.get(k1 | stat, 0), v1 + value)
            stat_value_hash = new_stat_value_hash

        if stat_value_hash:
            max_value = max(stat_value_hash.values())
        else:
            max_value = 0

        self.result = (self.result + max_value) % MOD

        return stat_value_hash


if __name__ == "__main__":
    print(Solution().goodSubtreeSum(vals=[2, 3], par=[-1, 0]))  # 8
    print(Solution().goodSubtreeSum(vals=[1, 5, 2], par=[-1, 0, 0]))  # 15
    print(Solution().goodSubtreeSum(vals=[34, 1, 2], par=[-1, 0, 1]))  # 42
    print(Solution().goodSubtreeSum(vals=[3, 22, 5], par=[-1, 0, 1]))  # 18

    # 测试用例 10 / 537
    print(Solution().goodSubtreeSum(vals=[9787, 1916], par=[-1, 0]))  # 0
