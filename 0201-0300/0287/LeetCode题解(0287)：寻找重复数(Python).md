# LeetCode题解(0287)：寻找重复数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-duplicate-number/)（中等）

标签：数组、双指针、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (76.83%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
```

