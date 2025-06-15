from collections import defaultdict
from typing import List, Optional, Set


class TreeNode:
    def __init__(self, idx: int, pid: int, depth: int, weight: int):
        """

        Parameters
        ----------
        idx : int
            节点 ID
        pid : int
            父节点 ID
        depth : int
            深度
        weight : int
            从根节点到当前节点的总权重
        """
        self.idx = idx
        self.pid = pid
        self.depth = depth
        self.weight = weight
        self.parent_list = []


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.n = n
        self.queries = queries
        self.node_list: List[Optional[TreeNode]] = [None] * n

        # 构造边的关系图
        self.edges2 = defaultdict(dict)
        for u, v, w in edges:
            self.edges2[u][v] = w
            self.edges2[v][u] = w

        # 构造倍增树结构
        path = [0]
        path_weight = [0, 0]
        visited = set()
        self.dfs(0, -1, path, path_weight, visited)

        # 执行查询
        result = []
        for u, v in queries:
            # 计算共有祖先节点
            source1 = node1 = self.node_list[u]
            source2 = node2 = self.node_list[v]

            if node1.depth < node2.depth:
                node1, node2 = node2, node1

            # 将 node1 上升到相同深度
            while node1.depth > node2.depth:
                # print("循环 -1")
                for i in range(len(node1.parent_list) - 1, -1, -1):
                    parent = node1.parent_list[i]
                    if parent.depth >= node2.depth:
                        node1 = parent
                        break

            # 从相同高度向上跳
            while node1 != node2:
                for i in range(len(node1.parent_list) - 1, -1, -1):
                    parent1 = node1.parent_list[i]
                    parent2 = node2.parent_list[i]
                    if parent1 != parent2:
                        node1 = parent1
                        node2 = parent2
                        break
                else:
                    # 所有祖先节点都相同
                    node1 = node1.parent_list[0]
                    node2 = node2.parent_list[0]

            # 得到共有祖先节点
            same = node1

            # 计算两侧路径长度
            weight1 = source1.weight - same.weight
            weight2 = source2.weight - same.weight
            # print(f"source1.idx={source1.idx}, source1.weight={source1.weight}, "
            #       f"source2.idx={source2.idx}, source2.weight={source2.weight}, same.weight={same.weight}")
            total_weight = weight1 + weight2
            aim_weight = total_weight / 2  # 目标权重
            if weight1 >= aim_weight:
                # 在 source1 到 same 的路径上
                node1 = source1
                while source1.weight - node1.weight < aim_weight:
                    # print(f"循环1: {node1.idx} {node1.weight} "
                    #       f"{[(parent.idx, parent.weight) for parent in node1.parent_list]}")
                    for i in range(len(node1.parent_list) - 1, -1, -1):
                        parent1 = node1.parent_list[i]
                        if source1.weight - parent1.weight < aim_weight:
                            node1 = self.node_list[parent1.pid]
                            break
                    else:
                        node1 = self.node_list[node1.pid]
                result.append(node1.idx)
            else:
                # 在 same 到 source2 的路径上
                node2 = source2
                last_node2 = node2
                while weight1 + (node2.weight - same.weight) >= aim_weight:
                    # print(f"循环2: {node2.idx} {node2.weight}"
                    #       f"{[(parent.idx, parent.weight) for parent in node2.parent_list]}")
                    for i in range(len(node2.parent_list) - 1, -1, -1):
                        parent2 = node2.parent_list[i]
                        # if parent2.idx == 0:
                        #     last_node2 = node2
                        #     node2 = parent2
                        #     break  # 如果已经是根节点，则直接跳出
                        if weight1 + (parent2.weight - same.weight) >= aim_weight:
                            last_node2 = node2 = parent2
                            # last_node2 = self.node_list[parent2.pid]
                            # node2 = self.node_list[last_node2.pid]
                            # print(f"触发更新: parent2={parent2.idx}, last_node2={last_node2.idx}, node2={node2.idx}")
                            break
                    else:
                        # 如果没有父节点大于目标长度，则说明 node2 就是超过目标长度的第一个点
                        last_node2 = node2
                        break
                result.append(last_node2.idx)

        return result

    def dfs(self, idx: int, pid: int, path: List[int], path_weight: List[int], visited: Set[int]):
        """
        idx = 当前节点 ID
        pid = 父节点 ID
        path = 从根节点到当前节点的路径（左侧是根节点）
        path_weight = 从根节点到当前节点的路径的权重（左侧是根节点，前缀和）
        """
        node = TreeNode(idx, pid, len(path), weight=path_weight[-1])
        # print(f"[DFS] {idx} {path_weight}")
        self.node_list[idx] = node
        visited.add(idx)

        # 构造倍增列表
        i = 1
        while i <= len(path):
            node.parent_list.append(self.node_list[path[-i]])
            i *= 2

        # 将当前节点添加到路径
        path.append(idx)
        for child, child_weight in self.edges2[idx].items():
            path_weight.append(path_weight[-1] + child_weight)
            if child not in visited:
                visited.add(child)
                self.dfs(child, idx, path, path_weight, visited)
                visited.remove(child)
            path_weight.pop()
        path.pop()


if __name__ == "__main__":
    print(Solution().findMedian(n=2, edges=[[0, 1, 7]], queries=[[1, 0], [0, 1]]))  # [0,1]
    print(Solution().findMedian(n=3, edges=[[0, 1, 2], [2, 0, 4]], queries=[[0, 1], [2, 0], [1, 2]]))  # [0,1]
    print(Solution().findMedian(n=5, edges=[[0, 1, 2], [0, 2, 5], [1, 3, 1], [2, 4, 3]],
                                queries=[[3, 4], [1, 2]]))  # [0,1]
