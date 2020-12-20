import collections
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 构造邻接列表图
        graph_in = collections.defaultdict(set)
        graph_out = collections.defaultdict(set)
        for n1 in range(len(beforeItems)):
            for n2 in beforeItems[n1]:
                graph_in[n1].add(n2)
                graph_out[n2].add(n1)

        # 统计每组包含的节点列表
        group_dic = collections.defaultdict(set)
        for i in range(n):
            group_dic[group[i]].add(i)

        # 等待访问的组
        waiting_group = {i for i in range(m) if len(group_dic[i]) > 0}

        # 统计所有节点的入射边
        count_edge = {}  # 节点入射边统计（项目依赖其他项目记录的拓扑排序）
        queue = []  # 当前入射边为0的节点列表
        for node in range(n):
            count_edge[node] = 0
        for node in graph_in:
            count_edge[node] = len(graph_in[node])

        # 统计所有小组的组外入射边
        count_group = {i: 0 for i in range(m)}
        for n1 in graph_in:
            g1 = group[n1]
            if g1 != -1:
                for n2 in graph_in[n1]:
                    g2 = group[n2]
                    if g2 != g1:
                        count_group[g1] += 1

        # 选择组外入射边为0的组
        now_group = -2  # 当前的组
        for g in waiting_group:
            if len(group_dic[g]) > 0 and count_group[g] == 0:
                now_group = g

        if now_group != -2:
            # 添加选中组的元素到队列
            for node in group_dic[now_group]:
                if count_edge[node] == 0:
                    queue.append(node)
            waiting_group.remove(now_group)

        # 添加的没有前置的未分组的项目
        for node in range(n):
            g = group[node]
            if g == -1 and count_edge[node] == 0:
                queue.append(node)

        # print("[BEFORE]", queue, count_edge, count_group, waiting_group)

        # 拓扑排序
        order = []
        while queue:
            n1 = queue.pop()
            g1 = group[n1]
            order.append(n1)

            for n2 in graph_out[n1]:
                g2 = group[n2]

                count_edge[n2] -= 1
                if g2 != -1 and g1 != g2:
                    count_group[g2] -= 1

                if (g2 == -1 or g2 == g1) and count_edge[n2] == 0:
                    queue.append(n2)

            if not queue:
                # 选择组外入射边为0的组
                now_group = -2  # 当前的组
                for g in waiting_group:
                    if len(group_dic[g]) > 0 and count_group[g] == 0:
                        now_group = g

                if now_group != -2:
                    # 添加选中组的元素到队列
                    for node in group_dic[now_group]:
                        if count_edge[node] == 0:
                            queue.append(node)
                    waiting_group.remove(now_group)

            # print("[ORDER]", order, ":", queue, count_edge, count_group, waiting_group)

        # print("拓扑排序:", order)

        return order if len(order) == n else []


if __name__ == "__main__":
    import time

    # [6,3,4,1,5,2,0,7]
    print(Solution().sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
                               beforeItems=[[], [6], [5], [6], [3, 6], [], [], []]))

    # []
    print(Solution().sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
                               beforeItems=[[], [6], [5], [6], [3], [], [4], []]))

    # [3,2,4,1,0]
    print(Solution().sortItems(n=5, m=5, group=[2, 0, -1, 3, 0],
                               beforeItems=[[2, 1, 3], [2, 4], [], [], []]))

    # [3,5,9,6,1,2,7,0,4,8]
    start_time = time.time()
    for ii in range(10000):
        print(Solution().sortItems(n=10, m=4, group=[2, 2, 2, 1, 0, 1, 3, 2, 0, 1],
                                   beforeItems=[[7, 6, 2, 5, 3], [], [], [], [7], [], [], [], [], []]))
    print("运行时长:", time.time() - start_time)
