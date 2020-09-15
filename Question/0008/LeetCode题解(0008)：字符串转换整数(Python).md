# LeetCode题解(0008)：提取字符串中的整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/string-to-integer-atoi/)（中等）

标签：字符串、正则表达式、自动机、自动机-有限状态自动机

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 36ms (97.40%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 48ms (58.90%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（正则表达式）：

```python
def myAtoi(self, str: str) -> int:
    # 字符串格式预处理
    match = re.search(r"^[+-]?[0-9]+", str.lstrip())

    # 处理没有匹配结果的情况
    if not match:
        return 0

    # 处理包含匹配结果的情况
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    group = int(match.group())
    if group < INT_MIN:
        return INT_MIN
    elif group > INT_MAX:
        return INT_MAX
    else:
        return group
```

解法二（有限状态自动机）：

```python
INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1


class Automaton:
    def __init__(self):
        self.stat = "start"
        self.sign = 1
        self.ans = 0
        self.table = {
            "start": ["start", "signed", "number", "end"],
            "signed": ["end", "end", "number", "end"],
            "number": ["end", "end", "number", "end"],
            "end": ["end", "end", "end", "end"],
        }

    def get(self, ch: str):
        # 计算当前状态
        if ch.isspace():
            self.stat = self.table[self.stat][0]
        elif ch == "+" or ch == "-":
            self.stat = self.table[self.stat][1]
        elif ch.isdigit():
            self.stat = self.table[self.stat][2]
        else:
            self.stat = self.table[self.stat][3]
        # 计算当前变化
        if self.stat == "number":
            self.ans = 10 * self.ans + int(ch)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.stat == "signed":
            self.sign = 1 if ch == "+" else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for ch in str:
            automaton.get(ch)
        return automaton.sign * automaton.ans
```