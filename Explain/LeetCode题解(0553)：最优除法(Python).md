# LeetCode题解(0553)：在连续除法中添加括号使结果最大(Python)

题目：[原题链接](https://leetcode-cn.com/problems/optimal-division/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (96.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        N = len(nums)
        if N == 1:
            return str(nums[0])
        elif N == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            nums = [str(n) for n in nums]
            return nums[0] + "/(" + "/".join(nums[1:]) + ")"
```