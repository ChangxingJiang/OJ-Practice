# LeetCode题解(0784)：字符串的字母大小写全排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/letter-case-permutation/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N*N)$ | $O(2^N*N)$ | 72ms (71.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（不断分裂结果）：

```python
def letterCasePermutation(self, S: str) -> List[str]:
    ans = [S]
    for i in range(len(S)):
        s = S[i]
        if s.isalpha():
            new = []
            for a in ans:
                new.append(a[:i] + s.lower() + a[i + 1:])
                new.append(a[:i] + s.upper() + a[i + 1:])
            ans = new
    return ans
```