# LeetCode题解(1209)：删除字符串中的所有相邻定长重复项(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/)（中等）

标签：栈、字符串、正则表达式

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | $O(N)$     | 4348ms (5.25%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 88ms (71.61%)  |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（正则表达式）：

```python
def removeDuplicates(self, s: str, k: int) -> str:
    s, num = re.subn(r"(.)\1{" + str(k - 1) + "}", "", s)
    while num:
        s, num = re.subn(r"(.)\1{" + str(k - 1) + "}", "", s)
    return s
```

解法二（栈）：

```python
def removeDuplicates(self, s: str, k: int) -> str:
    stack = []
    for ch in s:
        if not stack:
            stack.append([ch, 1])
        elif stack[-1][0] == ch:
            if stack[-1][1] == k - 1:
                stack.pop()
            else:
                stack[-1][1] += 1
        else:
            stack.append([ch, 1])

    ans = ""
    for elem in stack:
        ans += elem[0] * elem[1]
    return ans
```