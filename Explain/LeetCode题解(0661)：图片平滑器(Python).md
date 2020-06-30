# LeetCode题解(0661)：图片平滑器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/image-smoother/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 972ms (31.75%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    x = len(M)
    y = len(M[0])
    N = [[-1 for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            ans = [M[i][j]]
            if i > 0:
                ans.append(M[i - 1][j])
                if j > 0:
                    ans.append(M[i - 1][j - 1])
                if j < y - 1:
                    ans.append(M[i - 1][j + 1])
            if i < x - 1:
                ans.append(M[i + 1][j])
                if j > 0:
                    ans.append(M[i + 1][j - 1])
                if j < y - 1:
                    ans.append(M[i + 1][j + 1])
            if j > 0:
                ans.append(M[i][j - 1])
            if j < y - 1:
                ans.append(M[i][j + 1])
            print(i, j, ans, int(sum(ans) / len(ans)))
            N[i][j] = int(sum(ans) / len(ans))
    return N
```