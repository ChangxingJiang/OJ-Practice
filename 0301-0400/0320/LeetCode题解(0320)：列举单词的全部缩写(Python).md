# LeetCode题解(0320)：列举单词的全部缩写(Python)

题目：[原题链接](https://leetcode-cn.com/problems/generalized-abbreviation/)（中等）

标签：字符串、位运算、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(N)$     | 244ms (33.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []

        size = len(word)
        for i in range(2 ** size):
            pattern = bin(i)[2:].zfill(size)
            res = []
            for j in range(size):
                if pattern[j] == "0":
                    res.append(word[j])
                else:
                    if res and res[-1].isnumeric():
                        res[-1] = str(int(res[-1]) + 1)
                    else:
                        res.append("1")
            ans.append("".join(res))

        return ans
```