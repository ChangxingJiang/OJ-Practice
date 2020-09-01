# LeetCode题解(0344)：反转字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-string/)（简单）

标签：字符串、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 48ms (76.38%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 52ms (59.61%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic方法）：

```python
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```

解法二（双指针实现）：

```python
def reverseString(self, s: List[str]) -> None:
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
```