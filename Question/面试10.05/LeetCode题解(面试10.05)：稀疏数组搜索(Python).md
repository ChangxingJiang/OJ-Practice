# LeetCode题解(面试10.05)：稀疏数组搜索(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sparse-array-search-lcci/)（简单）

标签：二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (69.64%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（二分查找）：

```python
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            mid = (left + right) // 2

            while mid <= right and words[mid] == "":
                mid += 1

            if mid > right:
                right = (left + right) // 2 - 1

            elif words[mid] < s:
                left = mid + 1
            elif words[mid] > s:
                right = mid - 1
            else:
                return mid
        return -1
```