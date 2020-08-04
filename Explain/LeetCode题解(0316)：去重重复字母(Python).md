# LeetCode题解(0316)：去重重复字母(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-duplicate-letters/)（困难）

标签：贪心算法、栈

相关题目：题目与1081题相同。

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 108ms (6.50%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (95.53%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（贪心算法）：

```python
def removeDuplicateLetters(self, s: str) -> str:
    if not s:
        return ""
    count = Counter(s)
    pos = 0
    for i in range(len(s)):
        if s[i] < s[pos]:
            pos = i
        count[s[i]] -= 1
        if count[s[i]] == 0:
            break
    return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], ""))
```

解法二（用栈维护最小字典序结果）：

```python
def removeDuplicateLetters(self, s: str) -> str:
    count = Counter(s)
    stack = []
    for ch in s:
        count[ch] -= 1
        if ch not in stack:
            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)
    return "".join(stack)
```