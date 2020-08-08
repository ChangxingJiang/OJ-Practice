# LeetCode题解(1003)：检查字符串是否由指定字符串拼接产生(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions/)（中等）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | $O(N)$     | 36ms (99.03%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 56ms (59.42%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（字符串替换）：

![image-20200806125942237](LeetCode题解(1003)：截图1.png)

```python
def isValid(self, S: str) -> bool:
    last = None
    while last != len(S):
        last = len(S)
        S = S.replace("abc", "")
    return not S
```

解法二（栈）：

```python
def isValid(self, S: str) -> bool:
    stack = []
    for ch in S:
        if ch == "c":
            if len(stack) < 2 or stack.pop() != "b" or stack.pop() != "a":
                return False
        else:
            stack.append(ch)
    return not stack
```