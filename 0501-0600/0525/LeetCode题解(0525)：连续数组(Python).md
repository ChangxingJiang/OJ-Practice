# LeetCode题解(0525)：连续数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/contiguous-array/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 924ms (97.76%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        ans = 0
        differ = 0  # 1比0多的数量
        for i, n in enumerate(nums):
            if n == 0:
                differ -= 1
            else:
                differ += 1
            if differ in hashmap:
                ans = max(ans, i - hashmap[differ])
            else:
                hashmap[differ] = i
        return ans
```