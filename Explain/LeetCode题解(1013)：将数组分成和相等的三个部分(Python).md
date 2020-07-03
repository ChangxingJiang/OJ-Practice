# LeetCode题解(1013)：将数组分成和相等的三个部分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (85.22%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def canThreePartsEqualSum(self, A: List[int]) -> bool:
    aim = sum(A) / 3
    if aim % 1 != 0:
        return False

    cut = 0
    total = 0
    for a in A:
        total += a
        if total == aim:
            cut += 1
            total = 0
            if cut >= 3:
                return True
    else:
        return False
```

