import heapq
from typing import List


class Solution:
    def getOrder(self, original_tasks: List[List[int]]) -> List[int]:
        size = len(original_tasks)

        # 将下标值添加到任务中
        tasks = []
        for i in range(size):
            e, p = original_tasks[i]
            tasks.append((e, p, i))

        # 排序任务列表
        tasks.sort()

        waiting = []  # 等待执行的任务堆
        now = 0  # 当前时间：第1个任务出现的时间
        j = 0  # 下一个需要加入任务堆的任务下标

        ans = []

        while j < size:
            # 将之前已出现的任务添加到任务堆中
            while j < size and tasks[j][0] <= now:
                heapq.heappush(waiting, (tasks[j][1], tasks[j][2]))
                j += 1

            # 处理当前时间结点已没有任务的情况
            if not waiting:
                now = tasks[j][0]
                heapq.heappush(waiting, (tasks[j][1], tasks[j][2]))
                j += 1

            # 将相同时间点的任务添加到任务堆中
            while j < size and tasks[j][0] <= now:
                heapq.heappush(waiting, (tasks[j][1], tasks[j][2]))
                j += 1

            # 处理需要优先处理的任务
            p, i = heapq.heappop(waiting)
            now += p
            ans.append(i)

        # 处理积压的任务
        while waiting:
            p, i = heapq.heappop(waiting)
            ans.append(i)

        return ans


if __name__ == "__main__":
    print(Solution().getOrder(original_tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))  # [0,2,3,1]
    print(Solution().getOrder(original_tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))  # [4,3,2,0,1]

    # 测试用例:9/34
    # [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
    print(Solution().getOrder(
        original_tasks=[[19, 13], [16, 9], [21, 10], [32, 25], [37, 4],
                        [49, 24], [2, 15], [38, 41], [37, 34], [33, 6],
                        [45, 4], [18, 18], [46, 39], [12, 24]]))
