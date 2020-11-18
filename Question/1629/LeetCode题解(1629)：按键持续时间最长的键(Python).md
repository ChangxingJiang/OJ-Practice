# LeetCode题解(1629)：按键持续时间最长的键(Python)

题目：[原题链接](https://leetcode-cn.com/problems/slowest-key/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (84%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = None
        ans_val = 0
        last = 0
        for i in range(len(releaseTimes)):
            if releaseTimes[i] - last > ans_val:
                ans = keysPressed[i]
                ans_val = releaseTimes[i] - last
            elif releaseTimes[i] - last == ans_val and keysPressed[i] > ans:
                ans = keysPressed[i]

            last = releaseTimes[i]

        return ans
```