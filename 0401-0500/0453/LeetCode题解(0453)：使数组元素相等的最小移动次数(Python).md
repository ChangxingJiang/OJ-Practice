# LeetCode题解(0453)：使数组元素相等的最小移动次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | O(n)       | 超出时间限制   |
| Ans 2 (Python) | O(n)       | O(1)       | 316ms (78.52%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（实际操作法）：

> **【思路】**
>
> 模拟实际操作，每次操作保留一个最大值，并将数组中其他的值+1，直到数组中所有数相同为止。

```python
def minMoves(self, nums: List[int]) -> int:
    step = 0
    while len(set(nums)) > 1:
        maximum = max(nums)
        nums.remove(maximum)
        nums = [i + 1 for i in nums]
        nums.append(maximum)
        step += 1
    return step
```

解法二（Pythonic）：

> **【思路】**
>
> 每一次的相加，实际上相当于消除了超过最小值的1；因此，只需要统计数组超过数组最小值一共多少即可。

```python
def minMoves(self, nums: List[int]) -> int:
    minimum = min(nums)
    return sum([n - minimum for n in nums])
```