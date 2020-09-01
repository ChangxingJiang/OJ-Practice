# LeetCode题解(1023)：判断字符串是否能通过模式串添加小写字母生成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/camelcase-matching/)（中等）

标签：字符串、正则表达式

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | --                               | --         | 48ms (34.43%) |
| Ans 2 (Python) | $O(N×C)$ : 其中C为字符串平均长度 | $O(1)$     | 32ms (93.44%) |
| Ans 3 (Python) |                                  |            |               |

解法一（正则表达式）：

```python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        regex = "^[a-z]*" + "[a-z]*".join(pattern) + "[a-z]*$"  # 整理正则表达式
        return [bool(re.match(regex, query)) for query in queries]
```

解法二：

```python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(q):
            i = 0
            for ch in q:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                else:
                    if ch.isupper():
                        return False
            return i == len(pattern)

        return [check(query) for query in queries]
```