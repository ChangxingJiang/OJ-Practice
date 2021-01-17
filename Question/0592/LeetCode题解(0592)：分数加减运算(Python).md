# LeetCode题解(0592)：分数加减运算(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fraction-addition-and-subtraction/)（中等）

标签：数学、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (67.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def analyse(ss):
            if ss[0] == "+":
                flag = 1
            else:
                flag = -1
            s1, s2 = ss[1:].split("/")
            n1, n2 = int(s1), int(s2)
            return (flag, n1, n2)

        if expression[0] != "-":
            expression = "+" + expression

        lst = []
        now = ""
        for ch in expression:
            if ch == "+" or ch == "-":
                if now:
                    lst.append(analyse(now))
                now = ch
            else:
                now += ch
        lst.append(analyse(now))

        res1, res2 = 0, 2520
        for flag, n1, n2 in lst:
            res1 += flag * n1 * res2 // n2  # 1-10的最小公倍数=2520

        if res1 == 0:
            return "0/1"
        else:
            v = math.gcd(res1, res2)
            return str(res1 // v) + "/" + str(res2 // v)
```

