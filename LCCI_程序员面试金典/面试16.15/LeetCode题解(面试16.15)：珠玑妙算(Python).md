# LeetCode题解(面试16.15)：珠玑妙算游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/master-mind-lcci/submissions/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (94.97%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        ans1, ans2 = 0, 0


        colors = ["R", "Y", "G", "B"]
        lst1 = [0, 0, 0, 0]
        lst2 = [0, 0, 0, 0]
        for i in range(4):
            if solution[i] == guess[i]:
                ans1 += 1
            else:
                lst1[colors.index(solution[i])] += 1
                lst2[colors.index(guess[i])] += 1

        for i in range(4):
            ans2 += min(lst1[i], lst2[i])

        return [ans1, ans2]
```