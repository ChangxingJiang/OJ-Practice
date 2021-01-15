# LeetCode题解(1720)：解码异或后的数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decode-xored-array/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (67.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for n in encoded:
            ans.append(ans[-1] ^ n)
        return ans
```

