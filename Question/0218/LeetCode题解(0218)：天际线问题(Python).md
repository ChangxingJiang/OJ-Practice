# LeetCode题解(0218)：天际线问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-skyline-problem/)（困难）

标签：堆、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^N)$   | $O(N)$     | 92ms (49.51%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（堆和二分查找）：

```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        right_heap = []  # 当前房屋的结束位置
        height_lst = []  # 当前房屋高度情况

        ans = []

        for building in buildings:
            left, right, height = building
            # 移除更早的房屋
            while right_heap and right_heap[0][0] < left:
                # 记录当前的最高房子
                old_highest = height_lst[-1]
                # 移除最早的房子
                last_right, last_height = heapq.heappop(right_heap)
                height_lst.pop(bisect.bisect_left(height_lst, last_height))
                # 计算当前的最高房子
                new_highest = height_lst[-1] if height_lst else 0
                # 如果高度出现变化则记录变化
                if new_highest != old_highest:
                    if ans and ans[-1][0] == last_right:
                        ans.pop()
                    ans.append([last_right, new_highest])

            # 记录当前的房屋高度
            old_highest = height_lst[-1] if height_lst else 0
            # 添加当前的房屋
            bisect.insort_left(height_lst, height)
            heapq.heappush(right_heap, (right, height))
            # 计算当前的最高房子
            new_highest = height_lst[-1]
            # 如果高度出现变化则记录变化
            if new_highest != old_highest:
                if ans and ans[-1][0] == left:
                    ans.pop()
                ans.append([left, new_highest])

        # 移除所有的房屋
        while right_heap:
            # 记录当前的最高房子
            old_highest = height_lst[-1]
            # 移除最早的房子
            last_right, last_height = heapq.heappop(right_heap)
            height_lst.pop(bisect.bisect_left(height_lst, last_height))
            # 计算当前的最高房子
            new_highest = height_lst[-1] if height_lst else 0
            # 如果高度出现变化则记录变化
            if new_highest != old_highest:
                if ans and ans[-1][0] == last_right:
                    ans.pop()
                ans.append([last_right, new_highest])

        return ans
```