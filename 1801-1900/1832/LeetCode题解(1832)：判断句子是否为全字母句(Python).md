# LeetCode题解(1832)：判断句子是否为全字母句(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(26)$    | 40ms (68.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(collections.Counter(sentence)) == 26
```

