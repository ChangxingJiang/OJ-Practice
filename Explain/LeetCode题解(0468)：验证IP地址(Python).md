# LeetCode题解(0468)：验证IP地址是否为IPv4或IPv6的地址(Python)

题目：[原题链接](https://leetcode-cn.com/problems/validate-ip-address/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 20ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

![LeetCode题解(0468)：截图1](LeetCode题解(0468)：截图1.png)

```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # 尝试识别IPv4的IP地址
        lst4 = IP.split(".")
        if len(lst4) == 4:
            for item in lst4:
                if not item.isdigit() or int(item) > 255 or (int(item) != 0 and item[0] == "0") or (int(item) == 0 and len(item) > 1):
                    break
            else:
                return "IPv4"

        # 尝试识别IPv6的IP地址
        chars = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
        lst6 = IP.upper().split(":")
        if len(lst6) == 8:
            for item in lst6:
                if len(item) == 0 or len(item) > 4 or not all([ch in chars for ch in item]):
                    break
            else:
                return "IPv6"

        return "Neither"
```