# LeetCode题解(0249)：移位字符串分组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/group-shifted-strings/)（中等）

标签：哈希表、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (64.21%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        count = collections.defaultdict(list)
        for string in strings:
            key = []
            first = string[0]
            for ch in string:
                key.append((ord(ch) - ord(first) + 26) % 26)
            count[tuple(key)].append(string)
        return list(count.values())
```