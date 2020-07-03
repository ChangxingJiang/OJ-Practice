# LeetCode题解(0985)：查询后的偶数和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries/)（简单）

| 解法           | 时间复杂度                              | 空间复杂度                              | 执行用时       |
| -------------- | --------------------------------------- | --------------------------------------- | -------------- |
| Ans 1 (Python) | $O(N+Q)$ : N为A的长度，Q为queries的长度 | $O(N+Q)$ : N为A的长度，Q为queries的长度 | 608ms (94.38%) |
| Ans 2 (Python) |                                         |                                         |                |
| Ans 3 (Python) |                                         |                                         |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    total = sum([a for a in A if a % 2 == 0])
    ans = []
    for query in queries:
        a = A[query[1]]
        b = a + query[0]
        A[query[1]] = b
        if a % 2 == 0:
            total -= a
        if b % 2 == 0:
            total += b
        ans.append(total)

    return ans
```