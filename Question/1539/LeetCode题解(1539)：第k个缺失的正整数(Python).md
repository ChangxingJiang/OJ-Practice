# LeetCode题解(1539)：第k个缺失的正整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-missing-positive-number/)（简单）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (70.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        for n in arr:
            last += 1
            if n - last >= k:
                return last + k - 1
            else:
                k -= n - last
                last = n
        return last + k
```