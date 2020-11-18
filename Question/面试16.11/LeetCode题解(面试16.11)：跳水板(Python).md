# LeetCode题解(面试16.11)：跳水板(Python)

题目：[原题链接](https://leetcode-cn.com/problems/diving-board-lcci/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K)$     | $O(K)$     | 80ms (58.14%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        
        if shorter == longer:
            return [shorter * k]

        ans = []
        for i in range(k + 1):
            ans.append(longer * i + shorter * (k - i))
        return ans
```