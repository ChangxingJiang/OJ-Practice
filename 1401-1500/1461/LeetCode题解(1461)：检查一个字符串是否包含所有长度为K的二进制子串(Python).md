# LeetCode题解(1461)：检查一个字符串是否包含所有长度为K的二进制子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)（中等）

标签：字符串、集合、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×K)$   | $O(N×K)$   | 424ms (69.44%) |
| Ans 2 (Python) | $O(N×K)$   | $O(N×K)$   | 260ms (99.44%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lst = set()
        for i in range(len(s) - k + 1):
            lst.add(s[i:i + k])
        return len(lst) == 2 ** k
```

解法二（优化解法一）：

![LeetCode题解(1461)：截图](LeetCode题解(1461)：截图.png)

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 处理字符串长度过短的情况
        if len(s) < 2 ** k + 1:
            return False

        # 处理其他情况
        aim = 2 ** k
        lst = set()
        for i in range(len(s) - k + 1):
            lst.add(s[i:i + k])
            if len(lst) == aim:
                return True
        return False
```