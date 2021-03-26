# LeetCode题解(1606)：找到处理最多请求的服务器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/)（困难）

标签：堆、有序映射、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N×K)$   | $O(K)$     | 908ms (92%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（情景模拟）：

```python
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
```