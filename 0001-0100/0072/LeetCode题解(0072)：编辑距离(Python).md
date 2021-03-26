# LeetCode题解(0072)：计算两字符串之间的编辑距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/edit-distance/)（困难）

标签：字符串、动态规划

| 解法           | 时间复杂度                                | 空间复杂度                                | 执行用时       |
| -------------- | ----------------------------------------- | ----------------------------------------- | -------------- |
| Ans 1 (Python) | $O(M×N)$ : M为word1的长度，N为word2的长度 | $O(M×N)$ : M为word1的长度，N为word2的长度 | 184ms (87.65%) |
| Ans 2 (Python) | $O(M×N)$ : M为word1的长度，N为word2的长度 | $O(M×N)$ : M为word1的长度，N为word2的长度 | 56ms (100.00%) |
| Ans 3 (Python) |                                           |                                           |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（动态规划）：

```python
def minDistance(self, word1: str, word2: str) -> int:
    N1, N2 = len(word1), len(word2)

    # 处理某一个字符串为空的情况
    if N1 == 0 or N2 == 0:
        return N1 + N2

    # 定义状态记录数组
    matrix = [[0] * (N2 + 1) for _ in range(N1 + 1)]
    matrix[0][0] = 0

    # 计算空串与另一个字符串的比较（首行、首列）
    for i in range(N1):
        matrix[i + 1][0] = matrix[i][0] + 1
    for j in range(N2):
        matrix[0][j + 1] = matrix[0][j] + 1

    # 计算两个字符串
    for i in range(N1):
        for j in range(N2):
            if word1[i] == word2[j]:
                matrix[i + 1][j + 1] = matrix[i][j]
            else:
                matrix[i + 1][j + 1] = min(matrix[i + 1][j], matrix[i][j + 1], matrix[i][j]) + 1

    return matrix[N1][N2]
```

解法二（用列表存储状态，并用集合实现当前状态去重，减少无用的状态转移）：

![image-20200813090612538](LeetCode题解(0072)：截图1.png)

```python
def minDistance(self, word1: str, word2: str) -> int:
    visited = set()
    queue = collections.deque([(word1, word2, 0)])

    while True:
        w1, w2, d = queue.popleft()
        if (w1, w2) not in visited:
            if w1 == w2:
                return d
            visited.add((w1, w2))
            while w1 and w2 and w1[0] == w2[0]:
                w1 = w1[1:]
                w2 = w2[1:]
            d += 1
            queue.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])
```

