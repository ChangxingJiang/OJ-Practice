# LeetCode题解(LCP01)：猜数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/guess-numbers/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 28ms (98.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        ans = 0
        for i in range(len(guess)):
            ans += 1 if guess[i] == answer[i] else 0
        return ans
```