# LeetCode题解(0093)：依据未分隔的IP地址复原所有可能的IP地址(Python)

题目：[原题链接](https://leetcode-cn.com/problems/restore-ip-addresses/)（中等）

标签：字符串、递归

| 解法           | 时间复杂度          | 空间复杂度      | 执行用时      |
| -------------- | ------------------- | --------------- | ------------- |
| Ans 1 (Python) | $O(3^4×N)=O(N)$ | $O(4)=O(1)$ | 36ms (96.82%) |
| Ans 2 (Python) |                     |                 |               |
| Ans 3 (Python) |                     |                 |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归）：

```python
class Solution:
    def restoreIpAddresses(self, s: str, num: int = 4) -> List[str]:
        N = len(s)

        # 处理长度异常的情况
        if N < num or N > num * 3:
            return []

        # 处理最后一段的情况
        if num == 1:
            n = int(s)
            if 1 <= n <= 255 and s[0] != "0":
                return [s]
            elif n == 0 and len(s) == 1:
                return [s]
            else:
                return []

        # 处理第一个数字为0的情况
        if s[0] == "0":
            return [s[:1] + "." + ss for ss in self.restoreIpAddresses(s[1:], num - 1)] if N <= num * 3 - 2 else []

        # 处理其他情况
        lst1 = [s[:1] + "." + ss for ss in self.restoreIpAddresses(s[1:], num - 1)] if N <= num * 3 - 2 else []
        lst2 = [s[:2] + "." + ss for ss in self.restoreIpAddresses(s[2:], num - 1)] if num + 1 <= N <= num * 3 - 1 else []
        lst3 = [s[:3] + "." + ss for ss in self.restoreIpAddresses(s[3:], num - 1)] if num + 2 <= N and int(s[0:3]) <= 255 else []
        return lst1 + lst2 + lst3
```