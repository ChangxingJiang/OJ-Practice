# LeetCode题解(0682)：棒球比赛(Python)

题目：[原题链接](https://leetcode-cn.com/problems/baseball-game/)（简单）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (97.16%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def calPoints(self, ops: List[str]) -> int:
    marks = []
    for p in ops:
        if p == "+":
            marks.append(marks[-1] + marks[-2])
        elif p == "D":
            marks.append(2 * marks[-1])
        elif p == "C":
            marks.pop(-1)
        else:
            marks.append(int(p))
    return sum(marks)
```