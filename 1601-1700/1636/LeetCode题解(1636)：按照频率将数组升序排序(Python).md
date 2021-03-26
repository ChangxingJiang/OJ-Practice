# LeetCode题解(1636)：按照频率将数组升序排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-array-by-increasing-frequency/)（简单）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (80%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        nums.sort(key=lambda x: (count[x], -x))
        return nums
```