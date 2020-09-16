# LeetCode题解(0791)：依据字符在另一个字符串中的出现顺序排序字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/custom-sort-string/)（中等）

标签：字符串、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 36ms (92.31%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（自定义排序）：

```python
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = {}
        for ch in set(S):
            count[ch] = S.index(ch)

        return "".join(sorted(T, key=lambda k: count[k] if k in count else -1))
```