import bisect
import heapq
from typing import List


# 情景模拟
# O(NK)
# O(K)
# 二分查找 堆


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 每个服务器的处理请求数（用于生成答案）
        # O(K)
        finish_num = [0] * k

        # 记录当前空闲的服务器
        waiting_server_name = [i for i in range(k)]

        # 记录当前正在运行的服务器
        heap = []

        # 情景模拟
        for i in range(len(arrival)):
            # 获取当前时间
            time = arrival[i]

            # 计算当前请求优先的服务器
            idx = i % k

            # 释放当前已经完成任务的服务器资源
            while heap and heap[0][0] <= time:
                temp, finish_server_name = heapq.heappop(heap)
                bisect.insort(waiting_server_name, finish_server_name)

            # 如果当前没有空闲服务器，则跳过当前请求
            if not waiting_server_name:
                continue

            # 寻找分配的服务器
            use_server_idx = bisect.bisect_left(waiting_server_name, idx)

            # 当找到末尾的服务器时，则使用第一个服务器
            if use_server_idx == len(waiting_server_name):
                use_server_idx = 0

            # 从空闲列表中移除使用的服务器
            use_server_name = waiting_server_name.pop(use_server_idx)

            # 累加使用服务器的ID
            finish_num[use_server_name] += 1

            # 将使用的服务器加入到正在使用的服务器中
            heapq.heappush(heap, (time + load[i], use_server_name))

        # 计算最终结果
        # O(K)
        max_num = max(finish_num)
        return [idx for idx, num in enumerate(finish_num) if num == max_num]


if __name__ == "__main__":
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))  # [1]
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]))  # [0]
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11]))  # [0,1,2]
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4, 8, 9, 10], load=[5, 2, 10, 3, 1, 2, 2]))  # [1]
    print(Solution().busiestServers(k=1, arrival=[1], load=[1]))  # [0]
