# LeetCode题解(0455)：分发饼干(Python)

题目：[原题链接](https://leetcode-cn.com/problems/assign-cookies/)（简单）

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时       |
| -------------- | -------------- | ---------- | -------------- |
| Ans 1 (Python) | O(mlogm+nlogn) | O(m+n)     | 212ms (53.19%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

> **【思路】**
>
> 如果满足的尽量多的话，那应该优先满足胃口小的孩子。

```python
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    idx1 = 0
    idx2 = 0
    while idx1 < len(g) and idx2 < len(s):
        if g[idx1] <= s[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            idx2 += 1
    return idx1
```