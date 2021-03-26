# LeetCode题解(0271)：字符串的编码与解码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/encode-and-decode-strings/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 84ms (72.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Codec:
    def encode(self, strs: [str]) -> str:
        lst = [str(len(s)) for s in strs]
        return ",".join(lst) + "." + "".join(strs)

    def decode(self, s: str) -> [str]:
        idx = s.index(".")
        code = s[:idx]
        if not code:
            return []

        lst = [int(ss) for ss in code.split(",")]

        idx += 1

        ans = []
        for length in lst:
            ans.append(s[idx:idx + length])
            idx += length
        return ans
```