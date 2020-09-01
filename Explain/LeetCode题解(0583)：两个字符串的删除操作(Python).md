# LeetCode题解(0583)：删除两个字符串的字符直至两字符串相等的操作次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)（中等）

标签：字符串、动态规划、动态规划-状态表格

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 300ms (77.17%) |
| Ans 2 (Python) | $O(M×N)$   | $O(N)$     | 272ms (97.02%) |
| Ans 3 (Python) | $O(M×N)$   | $O(N)$     | 256ms (99.26%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（动态规划）：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 生成状态表格
        N1, N2 = len(word1), len(word2)
        matrix = [[0] * (N1 + 1) for _ in range(N2 + 1)]

        # 填写首行首列
        for j in range(1, N1 + 1):
            matrix[0][j] = matrix[0][j - 1] + 1
        for i in range(1, N2 + 1):
            matrix[i][0] = matrix[i - 1][0] + 1

        # 状态计算
        for i in range(1, N2 + 1):
            for j in range(1, N1 + 1):
                if word2[i - 1] != word1[j - 1]:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + 1
                else:
                    matrix[i][j] = matrix[i - 1][j - 1]

        return matrix[-1][-1]
```

解法二（单行动态规划）：

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 生成状态表格
        N1, N2 = len(word1), len(word2)
        matrix = [0] * (N1 + 1)

        # 填写首行首列
        for j in range(1, N1 + 1):
            matrix[j] = matrix[j - 1] + 1

        # 状态计算
        for i in range(1, N2 + 1):
            last = matrix[0]
            matrix[0] += 1
            for j in range(1, N1 + 1):
                tmp = matrix[j]
                if word2[i - 1] != word1[j - 1]:
                    matrix[j] = min(matrix[j], matrix[j - 1]) + 1
                else:
                    matrix[j] = last
                last = tmp
        return matrix[-1]
```

解法三（计算相同子序列）：

![LeetCode题解(0583)：截图1](LeetCode题解(0583)：截图1.png)

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 生成状态表格
        N1, N2 = len(word1), len(word2)
        matrix = [0] * (N1 + 1)

        # 状态计算
        for i in range(1, N2 + 1):
            last = 0
            for j in range(1, N1 + 1):
                tmp = matrix[j]
                if word2[i - 1] == word1[j - 1]:
                    matrix[j] = last + 1
                else:
                    matrix[j] = max(matrix[j], matrix[j - 1])
                last = tmp

        # 生成结果
        return N1 + N2 - 2 * matrix[-1]
```