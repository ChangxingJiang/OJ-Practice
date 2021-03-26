# LeetCode题解(0179)：最大数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-number/)（中等）

标签：排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 44ms (69.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = "".join(sorted([str(num) for num in nums], key=lambda x: (10 * x)[:10], reverse=True)).lstrip("0")
        return ans if ans else "0"
```