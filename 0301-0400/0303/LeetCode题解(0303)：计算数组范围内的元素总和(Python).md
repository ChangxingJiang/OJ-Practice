# LeetCode题解(0303)：计算数组范围内的元素总和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-sum-query-immutable/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(j-i)     | O(n)       | 7296ms (5.37%) |
| Ans 2 (Python) | O(1)       | O(n)       | 100ms (75.87%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（基本实现方法）：

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        for k in range(i, j + 1):
            ans += self.nums[k]
        return ans
```

解法二（缓存求和结果）：

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.adds = [0]
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            self.adds.append(add)
        print(self.adds)

    def sumRange(self, i: int, j: int) -> int:
        return self.adds[j + 1] - self.adds[i]
```