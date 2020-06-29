# LeetCode题解(0521)：寻找字符串独有的最长子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 32ms (94.62%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 36ms (85.13%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findLUSlength(self, a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    for size in range(len(a) - 1, -1, -1):
        for i in range(len(a) - size):
            s = a[i:]
            if s not in b:
                return size + 1
    return -1
```

（这个方法的思路其实是不正确的，但是刚好不会出问题）

解法二：

```python
def findLUSlength(self, a: str, b: str) -> int:
    return max(len(a), len(b)) if a != b else -1
```