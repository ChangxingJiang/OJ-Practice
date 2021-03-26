# LeetCode题解(1558)：得到目标数组的最少函数调用次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-numbers-of-function-calls-to-make-target-array/)（中等）

标签：数学、贪心算法

| 解法           | 时间复杂度                         | 空间复杂度 | 执行用时    |
| -------------- | ---------------------------------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogV)$ : 其中V为每个数的最大值 | $O(1)$     | 712ms (69%) |
| Ans 2 (Python) |                                    |            |             |
| Ans 3 (Python) |                                    |            |             |

解法一：

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op_2_min = 0  # 第2种操作的最小次数
        op_1 = 0  # 第1种操作的次数总数
        for num in nums:
            op_2 = 0
            while num:
                if num % 2 == 1:
                    num -= 1
                    op_1 += 1
                else:
                    num //= 2
                    op_2 += 1
            op_2_min = max(op_2_min, op_2)

        return op_1 + op_2_min
```