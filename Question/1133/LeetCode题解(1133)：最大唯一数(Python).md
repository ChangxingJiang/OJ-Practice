# LeetCode题解(1133)：最大唯一数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-unique-number/)（简单）

标签：哈希表、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (86.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        remove = set()
        number = set()
        for n in A:
            if n not in remove:
                if n not in number:
                    number.add(n)
                else:
                    number.remove(n)
                    remove.add(n)

        return max(number) if number else -1
```