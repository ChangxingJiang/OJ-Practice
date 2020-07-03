# LeetCode题解(1047)：删除字符串中的所有相邻重复项(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (35.00%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 56ms  (99.29%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def removeDuplicates(self, S: str) -> str:
    stack = []
    for s in S:
        if len(stack) == 0 or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop(-1)
    return "".join(stack)
```

解法二（替换函数）：

```python
def removeDuplicates(self, S: str) -> str:
    duplicates = {2 * ch for ch in string.ascii_lowercase}

    last_length = -1
    while len(S) != last_length:
        last_length = len(S)
        for d in duplicates:
            S = S.replace(d, "")

    return S
```