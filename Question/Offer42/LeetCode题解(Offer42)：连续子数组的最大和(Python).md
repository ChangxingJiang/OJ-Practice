# LeetCode题解(Offer42)：找出整数数组中一个具有最大和的连续子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)（简单）

标签：数组、动态规划、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 144ms (5.67%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 60ms (96.62%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix = 0
        min_prefix = 0
        for n in nums:
            prefix += n
            if n > 0:
                ans = max(ans, prefix - min_prefix)
            else:
                min_prefix = min(min_prefix, prefix)
                ans = max(ans, n)
        return ans
```

解法二：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -100000009
        prefix = 0
        for n in nums:
            prefix += n
            if prefix > ans:
                ans = prefix
            if prefix < 0:
                prefix = 0
        return ans
```