# LeetCode题解(1086)：前五科的均分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/high-five/)（简单）

标签：哈希表、堆、排序、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # 统计学生得分
        count = collections.defaultdict(list)
        for student, mark in items:
            heapq.heappush(count[student], mark)
            if len(count[student]) > 5:
                heapq.heappop(count[student])

        # 计算学生平均分
        ans = [[student, sum(lst) // 5] for student, lst in count.items()]
        ans.sort(key=lambda x: x[0])

        return ans
```