# LeetCode题解(0268)：判断序列中缺失的整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/missing-number/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 48ms (81.34%) |
| Ans 2 (Python) | O(n)       | O(1)       | 36ms (98.90%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def missingNumber(self, nums: List[int]) -> int:
    have_zero = False
    nums_sum = 0
    nums_max = 0
    for n in nums:
        nums_sum += n
        if n == 0:
            have_zero = True
        if nums_max < n:
            nums_max = n
    expect_sum = int((1 + nums_max) * nums_max / 2)
    answer = expect_sum - nums_sum
    if answer == 0:
        if have_zero:
            return nums_max + 1
        else:
            return 0
    else:
        return answer
```

解法二（使用列表长度优化最大值算法）：

```python
def missingNumber(self, nums: List[int]) -> int:
    nums_max = len(nums)
    nums_sum = 0
    for n in nums:
        nums_sum += n
    expect_sum = int((1 + nums_max) * nums_max / 2)
    return expect_sum - nums_sum
```