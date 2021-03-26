from typing import List


# 图
# 时间:O(N) 空间:O(N)

class Node:
    def __init__(self, i, val):
        self.i = i
        self.val = val
        self.near = set()


class Solution:
    def __init__(self):
        self.ans = []

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # 生成节点字典
        # O(N)
        node_dict = {i: Node(i, labels[i]) for i in range(n)}

        # 生成图的连通结构
        # O(N)
        for edge in edges:
            node1, node2 = node_dict[edge[0]], node_dict[edge[1]]
            node1.near.add(node2)
            node2.near.add(node1)

        # 遍历树结构计算结果
        # 时间:O(N) 空间:O(N)

        self.ans = [0] * n

        def dfs(last_node, now_node):
            res = [0] * 26
            res[ord(now_node.val) - 97] += 1
            for next_node in now_node.near:
                if next_node != last_node:
                    temp = dfs(now_node, next_node)
                    for i in range(26):
                        res[i] += temp[i]
            self.ans[now_node.i] = res[ord(now_node.val) - 97]
            return res

        dfs(None, node_dict[0])

        return self.ans


if __name__ == "__main__":
    # [2,1,1,1,1,1,1]
    print(Solution().countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd"))

    # [4,2,1,1]
    print(Solution().countSubTrees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb"))

    # [3,2,1,1,1]
    print(Solution().countSubTrees(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab"))

    # [1,2,1,1,2,1]
    print(Solution().countSubTrees(n=6, edges=[[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]], labels="cbabaa"))

    # [6,5,4,1,3,2,1]
    print(Solution().countSubTrees(n=7, edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], labels="aaabaaa"))
