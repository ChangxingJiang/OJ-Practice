# LeetCode题解(1203)：项目管理(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/)（困难）

标签：图、拓扑排序、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+G)$   | $O(N+G)$   | 超出时间限制   |
| Ans 2 (Python) | $O(N+G)$   | $O(N+G)$   | 548ms (68.18%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
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
```

解法二：

```python
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # 构建组到任务的映射
        group2Items = collections.defaultdict(set)
        index = m
        for i in range(n):
            if group[i] == -1:
                group[i] = index
                group2Items[index] = set([i])
                index += 1
            else:
                group2Items[group[i]].add(i)

        # 构建组的拓扑图
        beforeGroupsDic, preGroupsDic = {}, {}
        for i in range(index):
            beforeGroupsDic[i] = set()
            preGroupsDic[i] = set()
        for i in range(n):
            for j in beforeItems[i]:
                beforeGroupsDic[group[i]].add(group[j])
                preGroupsDic[group[j]].add(group[i])

        # 去除组内部的节点 如果存在环，在任务级别判断
        for i in range(index):
            if i in beforeGroupsDic[i]:
                beforeGroupsDic[i].remove(i)
                preGroupsDic[i].remove(i)
        res = []
        while beforeGroupsDic:
            # 找出所有入度为0的小组
            groups = [key for key, values in beforeGroupsDic.items() if not beforeGroupsDic[key]]
            if not groups:
                return []
            # 处理小组的拓扑关系
            for g in groups:
                beforeGroupsDic.pop(g)
                for g1 in preGroupsDic[g]:
                    beforeGroupsDic[g1].remove(g)
                preGroupsDic.pop(g)
            # 对小组内部建立拓扑图
            for key in groups:
                its = list(group2Items[key])
                # 对这些点建立拓扑图
                beforeItemsDic, preItemsDic = {}, {}
                for i in its:
                    beforeItemsDic[i] = set()
                    preItemsDic[i] = set()
                for i in its:
                    for j in beforeItems[i]:
                        if group[i] == group[j]:
                            beforeItemsDic[i].add(j)
                            preItemsDic[j].add(i)
                while beforeItemsDic:
                    items = [k for k, v in beforeItemsDic.items() if not beforeItemsDic[k]]
                    if not items:
                        return []
                    res += items
                    # 处理项目的拓扑关系
                    for item in items:
                        beforeItemsDic.pop(item)
                        for item1 in preItemsDic[item]:
                            if item1 in beforeItemsDic:
                                beforeItemsDic[item1].remove(item)
                        preItemsDic.pop(item)
        return res
```