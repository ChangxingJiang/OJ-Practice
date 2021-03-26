# LeetCode题解(0370)：区间加法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-addition/)（中等）

标签：数组、差分数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(U+N)$   | $O(N)$     | 248ms (6.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        lst = [0] * (length + 1)
        for update in updates:
            lst[update[0]] += update[2]
            lst[update[1] + 1] -= update[2]

        ans = []

        now = 0
        for i in range(length + 1):
            now += lst[i]
            ans.append(now)

        return ans[:-1]
```