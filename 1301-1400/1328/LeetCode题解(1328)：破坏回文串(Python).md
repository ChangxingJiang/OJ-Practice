# LeetCode题解(1328)：替换一个字母得到字典序最小的非回文串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/break-a-palindrome/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 20ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

![LeetCode题解(1328)：截图1](LeetCode题解(1328)：截图1.png)

```python
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # 处理长度为1的特殊情况
        if len(palindrome) == 1:
            return ""

        # 检查是否可通过使字典序变小的替换完成替换
        mid = len(palindrome) // 2
        for i in range(mid):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]

        # 将最后一个a替换为b
        return palindrome[:-1] + "b"
```