# LeetCode题解(1431)：拥有最多糖果的孩子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/)（简单）

题目标签：简单数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (54.21%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```python
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    limit = max(candies) - extraCandies
    return [candy >= limit for candy in candies]
```