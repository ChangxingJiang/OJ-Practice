import collections
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 记录每一个值的下标
        count = collections.defaultdict(list)
        for i in range(len(tasks)):
            e, p = tasks[i]
            count[(e, p)].append(i)

        # 排序
        tasks.sort()
        print(tasks)

        # 记录堆
        waiting = []

        ans = []

        now = 0  # 当前时间

        for e2, p2 in tasks:
            print(waiting, now, ":", e2, p2, "->", ans)

            while now <= e2 and waiting:
                p1, e1 = heapq.heappop(waiting)
                now += p1
                ans.append(count[(e1, p1)].pop())

            if now <= e2:  # 当前空闲
                ans.append(count[(e2, p2)].pop())
                now = e2 + p2
            else:  # 当前不空闲
                heapq.heappush(waiting, (p2, e2))

        # 处理积压的任务
        while waiting:
            p1, e1 = heapq.heappop(waiting)
            ans.append(count[(e1, p1)].pop())

        return ans


if __name__ == "__main__":
    print(Solution().getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))  # [0,2,3,1]
    print(Solution().getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))  # [4,3,2,0,1]

    # 测试用例:9/34
    # [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
    print(Solution().getOrder(
        tasks=[[19, 13], [16, 9], [21, 10], [32, 25], [37, 4],
               [49, 24], [2, 15], [38, 41], [37, 34], [33, 6],
               [45, 4], [18, 18], [46, 39], [12, 24]]))
