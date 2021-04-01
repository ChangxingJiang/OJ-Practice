# LeetCode题解(1736)：替换隐藏数字得到的最晚时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/)（简单）

标签：字符串、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (29.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(":")

        if time[0] == "?" and time[1] == "?":
            hour = "23"
        elif hour[0] == "?":
            if int(hour[1]) <= 3:
                hour = "2" + hour[1]
            else:  # int(hour[1]) > 3
                hour = "1" + hour[1]
        elif hour[1] == "?":
            if int(hour[0]) < 2:
                hour = hour[0] + "9"
            else:
                hour = hour[0] + "3"

        if minute[0] == "?" and minute[1] == "?":
            minute = "59"
        elif minute[0] == "?":
            minute = "5" + minute[1]
        elif minute[1] == "?":
            minute = minute[0] + "9"

        return hour + ":" + minute
```



