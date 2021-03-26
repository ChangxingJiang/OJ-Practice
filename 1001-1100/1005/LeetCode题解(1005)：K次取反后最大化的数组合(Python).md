# LeetCode题解(1005)：K次取反后最大化的数组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/)（简单）

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时      |
| -------------- | ------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN+K)$ | $O(N)$     | 60ms (86.21%) |
| Ans 2 (Python) |              |            |               |
| Ans 3 (Python) |              |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    number = []
    minus = []
    for a in A:
        if a >= 0:
            number.append(a)
        else:
            minus.append(a)
    minimum = min(number)
    minus.sort(reverse=True)

    out = 1
    for _ in range(K):
        if len(minus) > 0:
            n = -minus.pop(-1)
            if n < minimum:
                minimum = n
            number.append(n)
        else:
            out *= -1
    return sum(number) + sum(minus) - minimum + out * minimum
```

