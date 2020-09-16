# LeetCode题解(1545)：找出依据指定规则翻转的字符串的第K位(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (98.30%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        count = 0
        for i in [2 ** i for i in range(20, 0, -1)]:
            if k > i:
                k = 2 * i - k
                count += 1
            elif k == i:
                return "1" if count % 2 == 0 else "0"
        return "0" if count % 2 == 0 else "1"
```

