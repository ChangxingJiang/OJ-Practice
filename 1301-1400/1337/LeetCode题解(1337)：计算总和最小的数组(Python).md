# LeetCode题解(1337)：计算总和最小的数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/)（简单）

| 解法           | 时间复杂度                           | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(NMlogN)$ : N为行数，M为每行军人数 | $O(N)$     | 40ms (84.13%) |
| Ans 2 (Python) |                                      |            |               |
| Ans 3 (Python) |                                      |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（自定义排序）：

```python
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    def helper(n):
        return mat[n].count1(1), n

    m = [i for i in range(len(mat))]
    m.sort(key=helper)

    return m[:k]
```