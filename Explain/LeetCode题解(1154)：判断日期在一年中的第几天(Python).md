# LeetCode题解(1154)：判断日期在一年中的第几天(Python)

题目：[原题链接](https://leetcode-cn.com/problems/day-of-the-year/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (96.43%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 40ms (72.62%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def dayOfYear(self, date: str) -> int:
    year, month, date = date.split("-")
    year, month, date = int(year), int(month), int(date)

    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if leap:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return sum(month_days[:month - 1]) + date
```

解法二（优雅化）：

```python
def dayOfYear(self, date: str) -> int:
    year, month, date = map(int, date.split("-"))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return sum(month_days[:month - 1]) + date
```