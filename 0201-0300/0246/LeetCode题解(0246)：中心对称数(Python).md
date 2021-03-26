# LeetCode题解(0246)：中心对称数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/strobogrammatic-number/)（简单）

标签：数学、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (97.24%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 翻转180度后的对应表
        reverse_lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in reverse_lst or num[right] not in reverse_lst:
                return False
            if reverse_lst[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
```