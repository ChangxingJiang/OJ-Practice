# LeetCode题解(0334)：递增的三元子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)（中等）

标签：栈、贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (98.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = n2 = float("inf")
        for num in nums:
            if num < n1:
                n1 = num
            elif n1 < num < n2:
                n2 = num
            elif n2 < num:
                return True
        return False
```

