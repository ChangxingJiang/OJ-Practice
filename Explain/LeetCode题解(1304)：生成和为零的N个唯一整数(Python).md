# LeetCode题解(1304)：生成和为零的N个唯一整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (99.03%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def sumZero(self, n: int) -> List[int]:
    m = n // 2
    if n % 2 == 0:
        return [i for i in range(-m, 0)] + [i for i in range(1, m + 1)]
    else:
        return [i for i in range(-m, m + 1)]
```