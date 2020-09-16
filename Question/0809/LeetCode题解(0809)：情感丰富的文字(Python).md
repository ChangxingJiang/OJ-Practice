# LeetCode题解(0809)：判断字符串是否由单词扩张形成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/expressive-words/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (84.40%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def change(s):
            exp = []
            for ch in s:
                if not exp or ch != exp[-1][0]:
                    exp.append([ch, 1])
                else:
                    exp[-1][1] += 1
            return exp

        S = change(S)
        N = len(S)

        ans = 0
        for word in words:
            word = change(word)
            if len(word) == N:
                for i in range(N):
                    if word[i][0] != S[i][0] or word[i][1] > S[i][1] or (word[i][1] == 1 and S[i][1] == 2):
                        break
                else:
                    ans += 1

        return ans
```

