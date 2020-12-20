import collections
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        ans = 0

        # 每个债务关系数
        count = collections.Counter()

        # 构造借贷关系图
        # 直接简化重复边
        graph = collections.defaultdict(collections.Counter)
        for a, b, money in transactions:
            if b not in graph[a]:
                ans += 1  # 记录新边的数量
            graph[a][b] += money
            graph[b][a] -= money
            count[a] += money
            count[b] -= money

        print(ans, graph, count)

        # 首先优化完全销账的关系
        for node in graph:
            friends = list(graph[node].keys())
            for i in range(len(friends)):
                for j in range(i + 1, len(friends)):
                    a, b = friends[i], friends[j]
                    # 向一个人纯入账，向一个人纯出账，出入账价值相同，且那两个人之间有财务关系
                    if graph[node][a] + graph[node][b] == 0 and graph[a][b] != 0:
                        graph[a][b] += graph[node][b]
                        graph[b][a] -= graph[node][b]
                        del graph[node][a]
                        del graph[node][b]
                        del graph[a][node]
                        del graph[b][node]
                        ans -= 2

        print(ans, graph)

        # 其次优化不能完全销账的关系
        for node in graph:
            friends = list(graph[node].keys())
            for i in range(len(friends)):
                for j in range(i + 1, len(friends)):
                    a, b = friends[i], friends[j]
                    # 向一个人纯入账，向一个人纯出账，出入账价值相同，且那两个人之间有财务关系
                    if graph[node][a] * graph[node][b] < 0 and graph[a][b] != 0:
                        # 到b之间可以销账的情况
                        if abs(graph[node][a]) > abs(graph[node][b]):
                            graph[a][b] += graph[node][b]
                            graph[b][a] -= graph[node][b]
                            del graph[node][b]
                            del graph[b][node]
                        else:
                            graph[a][b] -= graph[node][a]
                            graph[b][a] += graph[node][a]
                            del graph[node][a]
                            del graph[a][node]
                        ans -= 1

        print(ans, graph)

        # 检查实际已被销账的关系
        for a in graph:
            friends = list(graph[a].keys())
            for b in friends:
                if graph[a][b] == 0:
                    del graph[a][b]
                    del graph[b][a]
                    ans -= 1

        print(ans, graph)

        return ans


if __name__ == "__main__":
    print(Solution().minTransfers([[0, 1, 10], [2, 0, 5]]))  # 2
    print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))  # 1
    print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 4], [2, 0, 5]]))  # 2
    print(Solution().minTransfers([[2, 0, 5], [3, 4, 4]]))  # 2
    print(Solution().minTransfers([[0, 1, 1], [1, 2, 1], [2, 0, 1]]))  # 0
    print(Solution().minTransfers([[0, 1, 2], [1, 2, 1], [1, 3, 1]]))  # 2
