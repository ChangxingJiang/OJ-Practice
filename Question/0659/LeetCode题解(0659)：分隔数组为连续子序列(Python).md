# LeetCode题解(0659)：分隔数组为连续子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/)（中等）

标签：堆、数组、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 96ms (96.39%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（维护序列起点堆）：

```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 格式化数组
        lst = []
        now = nums[0] - 1
        for n in nums:
            if n == now:
                lst[-1] += 1
            elif n == now + 1:
                lst.append(1)
                now = n
            else:
                lst.append(0)
                lst.append(1)
                now = n
        lst.append(0)

        # 维护起点堆
        heap = []
        for i2 in range(len(lst)):
            while lst[i2] > len(heap):
                heapq.heappush(heap, i2)
            while lst[i2] < len(heap):
                i1 = heapq.heappop(heap)
                if i2 - i1 < 3:
                    return False

        return True
```