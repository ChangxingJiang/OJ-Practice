import collections
from typing import List


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
