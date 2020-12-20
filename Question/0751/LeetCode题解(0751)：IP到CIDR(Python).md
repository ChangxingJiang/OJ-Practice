# LeetCode题解(0751)：IP到CIDR(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ip-to-cidr/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (65.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # 将IP转换为数值
        start = 0
        for x in ip.split("."):
            start = start * 256 + int(x)

        ans = []

        while n > 0:
            mask = min((start & -start), n).bit_length()
            if mask == 0:
                mask += 1
            ans.append(".".join(str((start >> i) % 256) for i in (24, 16, 8, 0)) + "/" + str(33 - mask))
            start += 1 << (mask - 1)
            n -= 1 << (mask - 1)

        return ans
```