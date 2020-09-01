# LeetCode题解(1529)：翻转列表中的一部分灯泡开关直至达到指定状态的步骤(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bulb-switcher-iv/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (95.83%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（统计变换的数量）：

```python
class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        now = "0"
        for ch in target:
            if ch != now:
                now = ch
                ans += 1
        return ans
```