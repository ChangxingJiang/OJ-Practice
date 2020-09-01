# LeetCode题解(0115)：字符串中指定子序列的出现次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distinct-subsequences/)（困难）

标签：字符串、动态规划、动态规划-状态表格

| 解法           | 时间复杂度                              | 空间复杂度                               | 执行用时       |
| -------------- | --------------------------------------- | ---------------------------------------- | -------------- |
| Ans 1 (Python) | $O(M×N×C)$ : 其中C为状态最高出现频数    | $O(Max(M,N)×C)$: 其中C为状态最高出现频数 | 超出时间限制   |
| Ans 2 (Python) | $O(M×N)$                                | $O(M×N)$                                 | 180ms (30.61%) |
| Ans 3 (Python) | $O(M+N×C)$ : 其中C为字符在t中的出现频数 | $O(M×C)$: 其中C为字符在t中的出现频数     | 36ms (99.63%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（动态规划：用双端队列存储状态）：

> 使用双端队列存储状态适合于重复出现的状态没有意义的情形，并搭配集合来筛选状态；对于当前这种题目不适用。

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N1 = len(s)
        N2 = len(t)
        D = N1 - N2

        # 处理t比s场的特殊情况
        if D < 0:
            return 0

        ans = 0

        # 动态规划：使用双端队列存储当前状态
        queue = collections.deque([(0, 0)])
        while queue:
            i1, i2 = queue.popleft()
            if i2 == N2:
                ans += 1
                continue
            if i1 < N1 and s[i1] == t[i2]:
                queue.append((i1 + 1, i2 + 1))
            if i1 < N1 and i1 - i2 < D:
                queue.append((i1 + 1, i2))

        return ans
```

解法二（动态规划：使用状态表格存储状态）：

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N1 = len(s)
        N2 = len(t)

        # 定义动态规划状态矩阵
        matrix = [[0] * (N1 + 1) for _ in range(N2 + 1)]
        matrix[0][0] = 1

        # 计算首行的状态
        for j in range(N1):
            matrix[0][j + 1] = matrix[0][j]

        # 计算状态转移数量
        for i in range(1, N2 + 1):
            for j in range(1, N1 + 1):
                if t[i - 1] == s[j - 1]:
                    matrix[i][j] += matrix[i - 1][j - 1]
                matrix[i][j] += matrix[i][j - 1]

        return matrix[-1][-1]
```

解法三（动态规划：使用单个数组存储当前行状态）：

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N1 = len(s)
        N2 = len(t)

        # 处理字符串s比字符串t短的情况
        if N1 < N2:
            return 0

        # 生成字符串中各个字符的坐标位置字典
        count = collections.defaultdict(list)
        for i, c in enumerate(t):
            count[c].append(i)

        stats = [1] + [0] * N2  # 当前行状态

        for ch in s:  # 遍历字符串s
            for j in count[ch][::-1]:  # 如果当前字符存在于j中，则遍历当前字符在j中的所有坐标
                stats[j + 1] += stats[j]  # 则累加当前位置的状态数

        return stats[-1]
```