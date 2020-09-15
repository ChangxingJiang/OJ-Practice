# LeetCode题解(0091)：字符串的解码方法数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decode-ways/)（中等）

标签：字符串、递归、动态规划

| 解法           | 时间复杂度 | 空间复杂度    | 执行用时      |
| -------------- | ---------- | ------------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(log(2^N))$ | 48ms (37.92%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$        | 40ms (82.95%) |
| Ans 3 (Python) |            |               |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
class Solution:
    @functools.lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if int(s) > 26:
                return self.numDecodings(s[1:])
            else:
                return 1 + self.numDecodings(s[1:])
        elif int(s[:2]) > 26:
            return self.numDecodings(s[1:])
        else:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
```

解法二（动态规划）：

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        stats = []
        last = None
        for ch in s[::-1]:
            if ch == "0":
                stats.append(0)
                last = int(ch)
            elif not stats:  # 处理第一个元素的情况
                stats.append(1)
                last = int(ch)
            elif len(stats) == 1:  # 处理第二个元素的情况
                n = int(ch)
                if 10 * n + last <= 26:
                    stats.append(1 + stats[-1])
                else:
                    stats.append(stats[-1])
                last = n
            else:
                n = int(ch)
                if 10 * n + last <= 26:
                    stats.append(stats[-2] + stats[-1])
                else:
                    stats.append(stats[-1])
                last = n
        return stats[-1]
```