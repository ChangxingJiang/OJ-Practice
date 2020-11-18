# LeetCode题解(面试08.14)：布尔计算(Python)

题目：[原题链接](https://leetcode-cn.com/problems/boolean-evaluation-lcci/)（中等）

标签：动态规划、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^2)$   | 64ms (94.22%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（动态规划）：

```python
class Solution:
    def countEval(self, s: str, result: int) -> int:
        size = len(s) // 2 + 1

        # 从各数字位到数字位的True或False的可能方法数
        dp = [[[-1] * size for _ in range(size)] for _ in range(2)]

        # 处理没有符号的情况
        for i in range(size):
            if s[i * 2] == "1":
                dp[1][i][i] = 1
                dp[0][i][i] = 0
            else:
                dp[0][i][i] = 1
                dp[1][i][i] = 0

        # print("当前状态表格：")
        # for i in range(size):
        #     print(dp[0][i], "|", dp[1][i])

        # 处理有符号的情况
        for length in range(1, size):
            for i in range(size - length):
                num1 = 0  # 结果为True的可能方法数
                num0 = 0  # 结果为False的可能方法数
                for j in range(length):
                    sign = s[(i + j) * 2 + 1]
                    # print(length, i, j, "-", (i, i + j), (i + j + 1, i + length), sign)
                    # 处理AND符号
                    if sign == "&":
                        num1 += dp[1][i][i + j] * dp[1][i + j + 1][i + length]
                        num0 += dp[0][i][i + j] * dp[1][i + j + 1][i + length]
                        num0 += dp[1][i][i + j] * dp[0][i + j + 1][i + length]
                        num0 += dp[0][i][i + j] * dp[0][i + j + 1][i + length]

                    # 处理OR符号
                    elif sign == "|":
                        num1 += dp[1][i][i + j] * dp[1][i + j + 1][i + length]
                        num1 += dp[0][i][i + j] * dp[1][i + j + 1][i + length]
                        num1 += dp[1][i][i + j] * dp[0][i + j + 1][i + length]
                        num0 += dp[0][i][i + j] * dp[0][i + j + 1][i + length]

                    # 处理XOR符号
                    else:  # sign == "^"
                        num0 += dp[1][i][i + j] * dp[1][i + j + 1][i + length]
                        num1 += dp[0][i][i + j] * dp[1][i + j + 1][i + length]
                        num1 += dp[1][i][i + j] * dp[0][i + j + 1][i + length]
                        num0 += dp[0][i][i + j] * dp[0][i + j + 1][i + length]

                dp[0][i][i + length] = num0
                dp[1][i][i + length] = num1

        # print("当前状态表格：")
        # for i in range(size):
        #     print(dp[0][i], "|", dp[1][i])

        return dp[result][0][-1]
```