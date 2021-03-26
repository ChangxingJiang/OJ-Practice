# LeetCode题解(1178)：猜字谜(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/)（困难）

标签：哈希表、位运算

| 解法           | 时间复杂度                                   | 空间复杂度     | 执行用时       |
| -------------- | -------------------------------------------- | -------------- | -------------- |
| Ans 1 (Python) | $O(W×L×logL+P×2^7×7×log7)$ : 其中L为谜底长度 | $O(W×L+2^7×7)$ | 916ms (35.29%) |
| Ans 2 (Python) |                                              |                |                |
| Ans 3 (Python) |                                              |                |                |

解法一：

```python
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def all_chance(chars):
            lst = [chars[0]]
            chars = list(sorted(set(chars[1:])))
            size = len(chars)
            res = []

            def recursion(i):
                if i == size:
                    res.append("".join(sorted(lst)))
                else:
                    lst.append(chars[i])
                    recursion(i + 1)
                    lst.pop()
                    recursion(i + 1)

            recursion(0)

            return res

        count = collections.Counter()
        for word in words:
            count["".join(sorted(set(word)))] += 1

        ans = []
        for puzzle in puzzles:
            now = 0
            for chance in all_chance(puzzle):
                now += count[chance]
            ans.append(now)

        return ans
```