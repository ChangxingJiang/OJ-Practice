# LeetCode题解(1702)：修改后的最大二进制字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-binary-string-after-change/)（中等）

标签：数学、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (99.59%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n1 = binary.count("0")
        if n1 <= 1:
            return binary

        n2 = 0
        for c in binary:
            if c != "1":
                break
            n2 += 1

        n3 = len(binary)

        return "1" * (n2 + n1 - 1) + "0" + "1" * (n3 - n2 - n1)
```

