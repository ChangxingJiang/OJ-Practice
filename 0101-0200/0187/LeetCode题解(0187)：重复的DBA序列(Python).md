# LeetCode题解(0187)：重复的DBA序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/repeated-dna-sequences/)（中等）

标签：哈希表、位运算

| 解法           | 时间复杂度 | 空间复杂度       | 执行用时      |
| -------------- | ---------- | ---------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(min(N,4^10))$ | 68ms (91.23%) |
| Ans 2 (Python) |            |                  |               |
| Ans 3 (Python) |            |                  |               |

解法一：

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        count = set()
        for i in range(len(s) - 9):
            ch = s[i:i + 10]
            if ch not in count:
                count.add(ch)
            else:
                ans.add(ch)
        return list(ans)
```