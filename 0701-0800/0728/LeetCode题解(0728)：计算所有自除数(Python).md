# LeetCode题解(0728)：计算所有自除数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/self-dividing-numbers/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 76ms (32.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```
def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    ans = []
    for i in range(left, right + 1):
        s = str(i)
        if "0" not in s and all([i % int(c) == 0 for c in s]):
            ans.append(i)
    return ans
```

