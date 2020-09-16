# LeetCode题解(0414)：数组中第三大的数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/third-maximum-number/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 64ms (83.71%) |
| Ans 2 (Python) | ---        | O(1)       | 52ms (99.70%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（直接寻找第三大的值）：

```python
def thirdMax(self, nums: List[int]) -> int:
    nums = set(nums)
    if len(nums) < 3:
        return max(nums)
    max1 = min(nums)
    max2 = max1
    max3 = max2
    for n in nums:
        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n > max2:
            max3 = max2
            max2 = n
        elif n > max3:
            max3 = n
    return max3
```

解法二（逐个删除最大值）：

```python
def thirdMax(self, nums: List[int]) -> int:
    nums = set(nums)
    if len(nums) < 3:
        return max(nums)
    nums.remove(max(nums))
    nums.remove(max(nums))
    return max(nums)
```