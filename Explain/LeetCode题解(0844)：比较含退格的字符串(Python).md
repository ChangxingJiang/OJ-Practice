# LeetCode题解(0844)：比较含退格的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/backspace-string-compare/)（简单）

| 解法           | 时间复杂度                      | 空间复杂度                      | 执行用时      |
| -------------- | ------------------------------- | ------------------------------- | ------------- |
| Ans 1 (Python) | $O(S+T)$ : S和T为两字符串的长度 | $O(S+T)$ : S和T为两字符串的长度 | 32ms (96.65%) |
| Ans 2 (Python) | $O(S+T)$ : S和T为两字符串的长度 | $O(S+T)$ : S和T为两字符串的长度 | 44ms (52.10%) |
| Ans 3 (Python) |                                 |                                 |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def backspaceCompare(self, S: str, T: str) -> bool:
    stack = []
    for s in S:
        if s != "#":
            stack.append(s)
        else:
            if len(stack) > 0:
                stack.pop(-1)
    S = "".join(stack)
    stack = []
    for t in T:
        if t != "#":
            stack.append(t)
        else:
            if len(stack) > 0:
                stack.pop(-1)
    T = "".join(stack)
    return S == T
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

    S = helper(S)
    T = helper(T)

    return S == T
```