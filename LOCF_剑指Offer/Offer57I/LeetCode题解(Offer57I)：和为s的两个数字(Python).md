# LeetCode题解(Offer57I)：寻找数组中两个和为目标值的数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)（简单）

标签：数组、集合

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 168ms (51.34%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = set()
        for n in nums:
            if target - n in lst:
                return [n, target - n]
            else:
                lst.add(n)
```