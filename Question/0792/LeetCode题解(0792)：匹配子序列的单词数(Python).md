# LeetCode题解(0792)：匹配子序列的单词数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-matching-subsequences/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(S+W×L)$ | $O(26×S)$  | 1020ms (22.45%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # 计算下一个字母的位置
        now = [-1] * 26
        table = [list(now)]
        for i in range(len(S) - 1, -1, -1):
            now[ord(S[i]) - 97] = i
            table.append(list(now))
        table.reverse()

        # 检查每个单词是否为子序列
        ans = 0
        for word in words:
            idx = 0
            for ch in word:
                if table[idx][ord(ch) - 97] == -1:
                    break
                else:
                    idx = table[idx][ord(ch) - 97] + 1
            else:
                ans += 1

        return ans
```

