# LeetCode题解(1640)：能否连接形成数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-array-formation-through-concatenation/)（简单）

标签：数组、排序、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时 |
| -------------- | ---------- | ---------- | -------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms     |
| Ans 2 (Python) |            |            |          |
| Ans 3 (Python) |            |            |          |

解法一：

```python
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lst = {num: idx for idx, num in enumerate(arr)}
        for piece in pieces:
            last = -1
            for num in piece:
                if num not in lst:
                    return False
                if lst[num] < last:
                    return False
                last = lst[num]
        return True
```