# LeetCode题解(0022)：依据括号数生成所有有效的括号组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/generate-parentheses/)（中等）

标签：字符串、回溯法

| 解法           | 时间复杂度                | 空间复杂度                 | 执行用时      |
| -------------- | ------------------------- | -------------------------- | ------------- |
| Ans 1 (Python) | $O(\frac{4^N}{\sqrt{n}})$ | $O(\frac{4^N}{n\sqrt{n}})$ | 44ms (64.59%) |
| Ans 2 (Python) | $O(N!)$                   | $O(N!)$                    | 392ms (5.02%) |
| Ans 3 (Python) | $O(\frac{4^N}{\sqrt{n}})$ | $O(\frac{4^N}{n\sqrt{n}})$ | 36ms (94.22%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return []
    elif n == 1:
        return ["()"]
    else:
        ans = {"()"}
        for _ in range(n - 1):
            now = set()
            for p in ans:
                for i in range(len(p)):
                    now.add(p[:i] + "()" + p[i:])
            ans = now
    return list(ans)
```

解法二（无法处理重复值的回溯法）：

```python
def generateParenthesis(self, n: int) -> List[str]:
    def backtrack(now, num):
        if num == n:
            ans.add(now)
            return
        for i in range(len(now)):
            backtrack(now[:i] + "()" + now[i:], num + 1)

    ans = set()
    if n:
        backtrack("()", 1)
    return list(ans)
```

解法三（可以解决重复值的回溯法）：

```python
def generateParenthesis(self, n: int) -> List[str]:
    def backtrack(now, left, right):
        if len(now) == 2 * n:
            ans.append("".join(now))
            return
        if left < n:
            now.append("(")
            backtrack(now, left + 1, right)
            now.pop()
        if left > right:
            now.append(")")
            backtrack(now, left, right + 1)
            now.pop()

    ans = []
    backtrack([], 0, 0)
    return ans
```