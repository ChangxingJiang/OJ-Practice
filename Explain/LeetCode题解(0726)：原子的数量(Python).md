# LeetCode题解(0726)：原子的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-atoms/)（困难）

标签：递归、哈希表、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 40ms (79.62%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 36ms (93.36%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
from collections import Counter


class Solution:
    def __init__(self):
        self.idx = 0
        self.formula = ""
        self.N = 0

    def resolver(self):
        count = Counter()
        while self.idx < self.N and self.formula[self.idx] != ")":
            # 当前字符为大写字母的情况
            if self.formula[self.idx].isupper():
                # 获取原子名称
                idx_start = self.idx
                self.idx += 1
                while self.idx < self.N and self.formula[self.idx].islower():  # 找到所有连续的小写字母（即完整原子名）
                    self.idx += 1
                name = self.formula[idx_start:self.idx]

                # 获取并累加原子数量
                i_start = self.idx
                while self.idx < self.N and self.formula[self.idx].isdigit():
                    self.idx += 1
                count[name] += int(self.formula[i_start:self.idx] or 1)

            # 当前字符为左括号的情况
            elif self.formula[self.idx] == "(":
                self.idx += 1
                inner_count = self.resolver()
                for name, value in inner_count.items():
                    count[name] += value

        self.idx += 1

        # 处理括号结束后的洗漱
        i_start = self.idx
        while self.idx < self.N and self.formula[self.idx].isdigit():
            self.idx += 1
        rate = int(self.formula[i_start:self.idx] or 1)
        if rate > 1:
            for name in count:
                count[name] *= rate

        return count

    def countOfAtoms(self, formula: str) -> str:
        self.formula = formula
        self.N = len(formula)

        # 解析化学式
        count = self.resolver()

        # 排序并输出
        ans = []
        for name in sorted(count):
            ans.append(name)
            rate = count[name]
            if rate > 1:
                ans.append(str(rate))
        return "".join(ans)
```

解法二（栈）：

```python
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [Counter()]
        i = 0
        while i < N:
            # 当前字符为大写字母的情况
            if formula[i].isupper():
                # 获取原子名称
                idx_start = i
                i += 1
                while i < N and formula[i].islower():  # 找到所有连续的小写字母（即完整原子名）
                    i += 1
                name = formula[idx_start:i]

                # 获取并累加原子数量
                idx_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                stack[-1][name] += int(formula[idx_start:i] or 1)

            # 当前字符为左括号的情况
            elif formula[i] == "(":
                stack.append(Counter())
                i += 1

            elif formula[i] == ")":
                inner = stack.pop()
                i += 1
                idx_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                rate = int(formula[idx_start:i] or 1)
                for name, value in inner.items():
                    stack[-1][name] += value * rate

        # 排序并输出
        count = stack[0]
        ans = []
        for name in sorted(count):
            ans.append(name)
            rate = count[name]
            if rate > 1:
                ans.append(str(rate))
        return "".join(ans)
```







