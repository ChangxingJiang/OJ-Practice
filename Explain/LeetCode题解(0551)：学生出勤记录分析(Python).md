# LeetCode题解(0551)：学生出勤记录分析(Python)

题目：[原题链接](https://leetcode-cn.com/problems/student-attendance-record-i/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | O(1)       | 40ms (70.22%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (89.33%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def checkRecord(self, s: str) -> bool:
    if s.count("A") >= 2:
        return False
    if "LLL" in s:
        return False
    return True
```

解法二（遍历)：

```python
def checkRecord(self, s: str) -> bool:
    absent = 0
    late = 0
    for c in s:
        if c == "L":
            late += 1
            if late >= 3:
                return False
        else:
            late = 0
            if c == "A":
                absent += 1
                if absent >= 2:
                    return False
    else:
        return True
```