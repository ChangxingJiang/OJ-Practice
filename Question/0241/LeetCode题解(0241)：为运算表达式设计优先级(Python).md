# LeetCode题解(0241)：为运算表达式设计优先级(Python)

题目：[原题链接](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/)（中等）

标签：分治算法、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 44ms (59.21%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 处理只剩下数字的情况
        if input.isdigit():
            return [int(input)]

        # 处理还剩下数字和运算符的情况
        ans = []
        for i, ch in enumerate(input):
            if ch in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for n1 in left:
                    for n2 in right:
                        if ch == "+":
                            ans.append(n1 + n2)
                        elif ch == "-":
                            ans.append(n1 - n2)
                        else:
                            ans.append(n1 * n2)
        return ans
```

