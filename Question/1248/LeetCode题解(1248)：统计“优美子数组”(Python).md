# LeetCode题解(1248)：统计“优美子数组”(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-number-of-nice-subarrays/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 172ms (75.60%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)

        ans = 0

        left = 0
        odd_num = 0
        even_left = 0
        for right in range(size):
            if nums[right] % 2 == 1:
                odd_num += 1
                if odd_num == k:
                    ans += even_left + 1
                elif odd_num > k:
                    odd_num -= 1
                    left += 1

                    even_left = 0
                    while nums[left] % 2 == 0:
                        even_left += 1
                        left += 1

                    ans += even_left + 1
            else:
                if odd_num == k:
                    ans += even_left + 1
                elif odd_num == 0:
                    left += 1
                    even_left += 1

        return ans
```

