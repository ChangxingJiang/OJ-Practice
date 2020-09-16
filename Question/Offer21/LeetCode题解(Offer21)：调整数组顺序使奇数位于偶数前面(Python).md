# LeetCode题解(Offer21)：调整数组顺序使奇数位于偶数前面(Python)

题目：[原题链接](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)（简单）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (82.18%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（双指针）：

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        idx = 0
        for i in range(len(nums)):
            n = nums[i]
            if n % 2 == 1:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return nums
```