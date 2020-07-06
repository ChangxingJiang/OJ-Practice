# LeetCode题解(1252)：增量操作后奇数值单元格的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix/)（简单）

| 解法           | 时间复杂度         | 空间复杂度        | 执行用时      |
| -------------- | ------------------ | ----------------- | ------------- |
| Ans 1 (Python) | $O(N)$ : N为操作数 | $O(N)$: N为操作数 | 52ms (83.61%) |
| Ans 2 (Python) |                    |                   |               |
| Ans 3 (Python) |                    |                   |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    r = {}
    c = {}
    for index in indices:
        if index[0] not in r:
            r[index[0]] = 1
        else:
            r[index[0]] += 1

        if index[1] not in c:
            c[index[1]] = 1
        else:
            c[index[1]] += 1

    r_odd = 0
    for k in r.values():
        if k % 2 == 1:
            r_odd += 1
    r_even = n - r_odd

    c_odd = 0
    for k in c.values():
        if k % 2 == 1:
            c_odd += 1
    c_even = m - c_odd

    return r_odd * c_even + c_odd * r_even
```