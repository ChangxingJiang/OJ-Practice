# LeetCode题解(0564)：寻找与当前数差值最小的回文数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-closest-palindrome/)（困难）

标签：字符串、数学

| 解法           | 时间复杂度                 | 空间复杂度                 | 执行用时      |
| -------------- | -------------------------- | -------------------------- | ------------- |
| Ans 1 (Python) | $O(L)$ : 其中L为字符串长度 | $O(L)$ : 其中L为字符串长度 | 32ms (96.69%) |
| Ans 2 (Python) |                            |                            |               |
| Ans 3 (Python) |                            |                            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # 处理特殊情况
        if n == "1":
            return "0"

        # 计算字符串中分隔位置的坐标
        idx_1 = (len(n) + 1) // 2  # 包含中间位置的坐标
        idx_2 = len(n) // 2  # 不包含中间位置的坐标

        ans = []

        # 计算第一种可能的答案（直接翻转后半部分）
        if n != n[::-1]:
            ans.append(int(n[:idx_1] + n[:idx_2][::-1]))

        # 计算第二种可能的答案（前半部分加1后翻转后半部分）
        temp = str(int(n[:idx_1]) + 1)
        ans.append(int(temp + temp[:idx_2][::-1]))

        # 计算第三种可能的答案（前半部分减1后翻转后半部分）
        if n == "1" + "0" * (len(n) - 1) or n == "1" + "0" * (len(n) - 2) + "1":  # 处理10、100等特殊情况
            ans.append(int("9" * (len(n) - 1)))
        else:
            temp = str(int(n[:idx_1]) - 1)
            ans.append(int(temp + temp[:idx_2][::-1]))

        # 选择其中差值最小的答案
        n = int(n)
        return str(sorted(ans, key=lambda i: (abs(i - n), i))[0])
```