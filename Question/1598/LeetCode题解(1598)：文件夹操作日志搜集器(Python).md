# LeetCode题解(1598)：依据文件夹操作日志计算当前路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/crawler-log-folder/)（简单）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (76%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        now = 0
        for log in logs:
            if log == "../":
                now = max(0, now - 1)
            elif log == "./":
                continue
            else:
                now += 1
        return now
```