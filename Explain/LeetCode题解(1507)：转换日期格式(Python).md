# LeetCode题解(1507)：转换日期格式(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reformat-date/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (68.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        month = str(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(month) + 1).zfill(2)
        return "-".join([year, month, day[:-2].zfill(2)])
```