# LeetCode题解(1375)：灯泡开关III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bulb-switcher-iii/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 140ms (25.78%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        ans = 0

        stat = [0] * len(light)  # 当前亮灯状态
        now = 0  # 当前全亮的最右侧位置

        for i in range(len(light)):
            stat[light[i] - 1] = 1

            while now < len(light) and stat[now]:
                now += 1

            if now == i + 1:
                ans += 1

        return ans
```

