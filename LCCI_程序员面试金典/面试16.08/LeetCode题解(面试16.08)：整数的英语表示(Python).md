# LeetCode题解(面试16.08)：整数的英语表示(Python)

题目：[原题链接](https://leetcode-cn.com/problems/english-int-lcci/)（困难）

标签：分治算法、数学、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 44ms (67.12%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（分治算法）：

```python
class Solution:
    # 处理[0,20)的情况
    def count1(self, n):
        return ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"][n]

    # 处理[20,100)的情况
    def count2(self, n):
        a, b = divmod(n, 10)
        ans = [["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][a - 2]]
        if b:
            ans.append(self.count1(b))
        return " ".join(ans)

    # 处理[0,100)的情况
    def count3(self, n):
        if n < 20:
            return self.count1(n)
        else:
            return self.count2(n)

    # 处理[100,1000)的情况
    def count4(self, n):
        a, b = divmod(n, 100)
        ans = [self.count1(a), "Hundred"]
        if b:
            ans.append(self.count3(b))
        return " ".join(ans)

    # 处理[0,1000)的情况
    def count5(self, n):
        if n < 100:
            return self.count3(n)
        else:
            return self.count4(n)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ans = []
        name = ["Billion", "Million", "Thousand", None]
        while num > 0:
            num, now = divmod(num, 1000)
            b = name.pop()
            if b and now:
                ans.append(b)
            if now:
                ans.append(self.count5(now))

        return " ".join(ans[::-1])
```