# LeetCode题解(1464)：数组中两元素的最大乘积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (83.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def maxProduct(self, nums: List[int]) -> int:
    max1 = 0
    max2 = 0
    for n in nums:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    return (max1 - 1) * (max2 - 1)
```