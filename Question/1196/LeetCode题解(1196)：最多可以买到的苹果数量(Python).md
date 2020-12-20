# LeetCode题解(1196)：最多可以买到的苹果数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/how-many-apples-can-you-put-into-the-basket/)（简单）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(1)$     | 56ms (82.43%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        now = 5000
        ans = 0
        for n in arr:
            now -= n
            if now > 0:
                ans += 1
            else:
                return ans

        return ans
```