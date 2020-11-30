# LeetCode题解(0535)：TinyURL的加密与解密(Python)

题目：[原题链接](https://leetcode-cn.com/problems/encode-and-decode-tinyurl/)（中等）

标签：哈希表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 48ms (40.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Codec:

    def __init__(self):
        self.hashmap = {}

    def encode(self, longUrl: str) -> str:
        token = str(hash(longUrl))
        self.hashmap[token] = longUrl
        return str(token)

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.hashmap:
            val = self.hashmap[shortUrl]
            del self.hashmap[shortUrl]
            return val
```