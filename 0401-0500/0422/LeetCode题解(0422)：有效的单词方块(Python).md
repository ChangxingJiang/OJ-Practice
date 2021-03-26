# LeetCode题解(0422)：有效的单词方块(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-word-square/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 100ms (18.99%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if len(words) <= j or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False
        return True
```