# LeetCode题解(1052)：爱生气的书店老板(Python)

题目：[原题链接](https://leetcode-cn.com/problems/grumpy-bookstore-owner/)（中等）

标签：数组、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 328ms (67.39%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        size = len(customers)

        lst1 = []
        lst2 = []
        for i in range(size):
            if grumpy[i] == 0:
                lst1.append(customers[i])
                lst2.append(0)
            else:
                lst1.append(0)
                lst2.append(customers[i])

        left = right = now = ans = 0
        while right < size:
            now += lst2[right]
            if right - left + 1 > X:
                now -= lst2[left]
                left += 1
            right += 1
            ans = max(ans, now)

        return sum(lst1) + ans
```

