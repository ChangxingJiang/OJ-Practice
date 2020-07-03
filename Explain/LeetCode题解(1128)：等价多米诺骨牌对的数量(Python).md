# LeetCode题解(1128)：等价多米诺骨牌对的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 276ms (95.19%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    count = collections.Counter((d[0], d[1]) if d[0] < d[1] else (d[1], d[0]) for d in dominoes)
    ans = 0
    for val in count.values():
        ans += val * (val - 1) / 2
    return ans
```