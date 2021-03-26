# LeetCode题解(Offer67)：把字符串转换成整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)（中等）

标签：字符串、正则表达式、自动机、自动机-有限状态自动机

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (90.24%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def strToInt(self, str: str) -> int:
        if ans := re.search("^[-+]?[0-9]+", str.lstrip()):
            ans = int(ans.group())
            if ans > 2147483647:
                return 2147483647
            elif ans < -2147483648:
                return -2147483648
            else:
                return ans
        else:
            return 0
```