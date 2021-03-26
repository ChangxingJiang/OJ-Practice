# LeetCode题解(0248)：中心对称数III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/strobogrammatic-number-iii/)（困难）

标签：数学、递归、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    # 已知开始范围，计算两个数之间的数量
    @staticmethod
    def num1(low, high, middle=False):
        if middle:
            return len([str(i) for i in [0, 1, 8] if int(low) <= i <= int(high)])
        else:
            return len([str(i) for i in [0, 1, 6, 8, 9] if int(low) < i < int(high)])

    # 计算各个位的数量
    @staticmethod
    def count(n, first):
        if n == 0:
            return 1
        if n == 1:
            return 3
        if n == 2:
            return 4 if first else 5

        if first:
            return 4 * Solution.count(n - 2, first=False)
        else:
            return 5 * Solution.count(n - 2, first=False)

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # 字符串交换列表
        reverse_lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        # print("当前计算:", low, high)

        # 如果顺序相反则返回0
        if int(low) > int(high):
            return 0

        # 处理两个数完全相同的情况
        if low == high:
            return 1 if low == low[::-1] else 0

        a, b = len(low), len(high)

        # 处理两数位数不同的情况
        # 例：(150-525) -> (150-199) + (200-499) + (500-525)
        if a == b:
            # 寻找两个数第一个不同的位数
            i = 0
            while i < a and low[i] == high[i]:
                i += 1

            s = a // 2

            # 处理只有一位的情况
            # 处理奇数长度的中间位的情况
            if a == 1 or (a % 2 == 1 and i == s):
                return self.num1(low[i], high[i], middle=True)

            # 处理在中间位之前的情况
            if (a % 2 == 0 and i < s) or (a % 2 == 1 and i < s):
                ans = self.num1(low[i], high[i]) * self.count(a - (i + 1) * 2, first=False)
                # print(low, high, "(", i, ")", "=",
                #       self.num1(low[i], high[i]), "*", self.count(a - (i + 1) * 2, first=False), "=", ans,
                #       "->",
                #       (low, low[:i + 1] + "9" * (a - i - 1)) if low[i] in reverse_lst else (),
                #       (high[:i + 1] + "0" * (a - i - 1), high) if high[i] in reverse_lst else ())
                if low[i] in reverse_lst:
                    high2 = low[:i + 1] + "9" * (a - i - 1)
                    ans += self.strobogrammaticInRange(low, high2)
                if high[i] in reverse_lst:
                    low2 = high[:i + 1] + "0" * (a - i - 1)
                    ans += self.strobogrammaticInRange(low2, high)
                return ans

            # 处理中心位之后的情况
            ch = reverse_lst[low[s - (i - s + 1)] if a % 2 == 0 else low[s - (i - s)]]  # 计算当前字符的目标值
            # 计算是否超出情况
            if int(low[i]) < int(ch) < int(high[i]):
                return 1
            elif int(low[i]) == int(ch):
                while i < a:
                    ch = reverse_lst[low[s - (i - s + 1)] if a % 2 == 0 else low[s - (i - s)]]  # 计算当前字符的目标值
                    if int(ch) > int(low[i]):
                        return 1
                    elif int(ch) == int(low[i]):
                        i += 1
                    else:
                        return 0
                return 1
            elif int(ch) == int(high[i]):
                while i < a:
                    ch = reverse_lst[low[s - (i - s + 1)] if a % 2 == 0 else low[s - (i - s)]]  # 计算当前字符的目标值
                    if int(ch) < int(high[i]):
                        return 1
                    elif int(ch) == int(high[i]):
                        i += 1
                    else:
                        return 0
                return 1
            else:
                return 0

        # 处理两个数位数不同的情况
        # 例：(50-4050) -> (50-99) + 3位数的情况数 + (1000-4050)
        else:
            ans = 0
            for i in range(a + 1, b):
                ans += self.count(i, first=True)
            # print(low, high, "=", ans, "->", (low, "9" * a), ("1" + "0" * (b - 1), high))
            return (ans +
                    self.strobogrammaticInRange(low, "9" * a) +
                    self.strobogrammaticInRange("1" + "0" * (b - 1), high))
```