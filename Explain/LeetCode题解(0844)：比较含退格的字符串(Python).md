# LeetCode题解(0844)：比较含退格的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/backspace-string-compare/)（简单）

标签：栈、字符串、字符串-双指针

| 解法           | 时间复杂度                      | 空间复杂度                      | 执行用时      |
| -------------- | ------------------------------- | ------------------------------- | ------------- |
| Ans 1 (Python) | $O(S+T)$ : S和T为两字符串的长度 | $O(S+T)$ : S和T为两字符串的长度 | 32ms (96.65%) |
| Ans 2 (Python) | $O(S+T)$ : S和T为两字符串的长度 | $O(S+T)$ : S和T为两字符串的长度 | 40ms (77.12%) |
| Ans 3 (Python) |                                 |                                 |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def backspaceCompare(self, S: str, T: str) -> bool:
    stack1 = []
    for s in S:
        if s != "#":
            stack1.append(s)
        else:
            if len(stack1) > 0:
                stack1.pop(-1)
    stack2 = []
    for t in T:
        if t != "#":
            stack2.append(t)
        else:
            if len(stack2) > 0:
                stack2.pop(-1)
    return stack1 == stack2
```

解法二（双指针）：

```python
def backspaceCompare(self, S: str, T: str) -> bool:
    def helper(s):
        ans = ""
        skip = 0
        for c in reversed(s):
            if c == "#":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                ans += c
        return ans

    return helper(S) == helper(T)
```