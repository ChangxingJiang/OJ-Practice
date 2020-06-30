# LeetCode题解(0628)：计算三个数的最大乘积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-product-of-three-numbers/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 368ms (30.66%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 320ms (88.43%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

> 【思路】
>
> 可能的最大值为三个最大的正数相乘，或两个绝对值最大的负数以及最大的正数相乘。

```python
def maximumProduct(self, nums: List[int]) -> int:
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
```

解法二（遍历）：

```python
def maximumProduct(self, nums: List[int]) -> int:
    min1 = min2 = float("inf")
    max1 = max2 = max3 = float("-inf")
    for n in nums:
        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n
        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n > max2:
            max3 = max2
            max2 = n
        elif n > max3:
            max3 = n
    return max(max1 * max2 * max3, min1 * min2 * max1)
```