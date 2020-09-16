# LeetCode题解(0392)：判断是否为子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/is-subsequence/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 36ms (96.15%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（完全遍历）：

```python
def isSubsequence(self, s: str, t: str) -> bool:
    for c in s:
        if c in t:
            t = t[t.index(c) + 1:]
        else:
            return False
    else:
        return True
```