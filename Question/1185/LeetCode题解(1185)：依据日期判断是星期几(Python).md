# LeetCode题解(1185)：依据日期判断是星期几(Python)

题目：[原题链接](https://leetcode-cn.com/problems/day-of-the-week/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 28ms (99.68%)  |
| Ans 2 (Python) |            |            | 436ms (87.70%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（模拟情景）：

![LeetCode题解(1185)：截图1](LeetCode题解(1185)：截图1.png)

```
def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    ans = 4

    # 累加年份
    for y in range(1971, year):
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            ans += 2
        else:
            ans += 1
    ans = ans % 7

    print(year, ans)

    # 累加月份
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[1] = 29
    ans += sum(months[:month - 1])
    ans = ans % 7

    print(year, ans)

    # 累加日期
    ans += day - 1

    print(year, ans)

    # 计算星期
    ans = ans % 7
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][ans]
```

解法二（解法一的优化）：

> **【思路】**
>
> 年份计算：
>
> ```python
> # 将循环改为计算
> ans += year + year // 4 - year // 100 + year // 400 - 1971 // 4 + 1971 // 100 + 1971 // 400
> # 直接计算出常数部分
> ans += year + year // 4 - year // 100 + year // 400 - 478
> # 因为478为7的倍数，因此可忽略
> ans += year + year // 4 - year // 100 + year // 400
> ```
>
> 月份计算，参考基姆拉尔森公式，将月份视作在30天（month*2）基础上的小幅变化：
>
> ```python
> # 累加月份
> ans += 2 * month + 3 * (month + 1) / 5  # 其中需将1月和2月视作前一年的13月和14月
> ```

```python
def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    if month == 1 or month == 2:
        month += 12
        year -= 1
    ans = int((year + year // 4 - year // 100 + year // 400 + 2 * month + 3 * (month + 1) / 5 + day) % 7)
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][ans]
```