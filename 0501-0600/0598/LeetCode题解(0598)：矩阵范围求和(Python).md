# LeetCode题解(0598)：矩阵范围求和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-addition-ii/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 84ms (87.54%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 92ms (52.72%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（维护每次都加1的最大区域）：

```python
def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    for op in ops:
        m = min(m, op[0])
        n = min(n, op[1])
    return m * n
```

解法二（使用zip方法）：

```python
def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    if len(ops) == 0:
        return m * n
    zipped = list(zip(*ops))
    return min(min(zipped[0]), m) * min(min(zipped[1]), n)
```