# LeetCode题解(1807)：替换字符串中的括号内容(Python)

题目：[原题链接](https://leetcode-cn.com/problems/evaluate-the-bracket-pairs-of-a-string/)（中等）

标签：哈希表、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(S+K)$   | $O(K)$     | 192ms (69.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {key: value for key, value in knowledge}

        ans = []
        left, right = -1, -1
        for i, ch in enumerate(s):
            if ch == "(":
                left = i
                ans.append(s[right + 1:left])
            elif ch == ")":
                right = i
                key = s[left + 1:right]
                if key in knowledge:
                    ans.append(knowledge[key])
                else:
                    ans.append("?")
        ans.append(s[right + 1:])

        return "".join(ans)
```

