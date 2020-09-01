# LeetCode题解(0678)：判断包含通配符*的字符串中的括号是否有效(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-parenthesis-string/)（中等）

标签：字符串、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 24ms (100.00%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (87.80%)  |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

![LeetCode题解(0678)：截图1](LeetCode题解(0678)：截图1.png)

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == ")":
                idx = len(stack) - 1
                while idx > -1:
                    if stack[idx] == "(":
                        break
                    idx -= 1
                if idx >= 0:
                    stack.pop(idx)
                elif len(stack) > 0:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        left_num = 0
        for ch in stack:
            if ch == "(":
                left_num += 1
            elif left_num > 0:
                left_num -= 1
        return left_num == 0
```

解法二（贪心算法）：

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left_num = 0
        max_left_num = 0
        for ch in s:
            if ch == "(":
                min_left_num += 1
                max_left_num += 1
            elif ch == "*":
                if min_left_num > 0:
                    min_left_num -= 1
                max_left_num += 1
            else:
                if min_left_num > 0:
                    min_left_num -= 1
                max_left_num -= 1
            if max_left_num < 0:
                return False
        return min_left_num == 0
```