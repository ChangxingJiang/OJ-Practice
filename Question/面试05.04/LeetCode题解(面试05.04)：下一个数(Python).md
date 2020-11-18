# LeetCode题解(面试05.04)：下一个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/closed-number-lcci/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 32ms (92.83%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        # 计算更小的那个数
        i, n = 0, num
        a, b = -1, -1  # 准备移到的位，准备移走的位
        array = []  # 移走的位之后的位
        while n:
            if not n & 1:
                a = i
            if n & 1:
                if a == -1:
                    array.append(i)
                else:
                    b = i
                    break
            i += 1
            n >>= 1

        if a >= 0 and b >= 0:
            ans1 = num - (1 << b) + (1 << a)
            m = a - 1
            for n in array:
                ans1 -= (1 << n)
                ans1 += (1 << m)
                m -= 1
        else:
            ans1 = -1

        # print(a, b, array, "->", ans1)

        # 计算更大的那个数
        i, n = 0, num
        a, b = -1, -1  # 准备移走的位，准备移到的位
        array = []  # 移走的位之后的位
        while n:
            if n & 1:
                a = i
            if not n & 1:
                if a != -1:
                    b = i
                    break
                else:
                    array.append(i)
            i += 1
            n >>= 1
        if b == -1:
            b = i

        if a >= 0 and b >= 0:
            ans2 = num + (1 << b) - (1 << a)
            m = a - 1
            for n in array:
                ans2 += (1 << n)
                ans2 -= (1 << m)
                m -= 1
        else:
            ans2 = -1

        return [ans2, ans1]
```