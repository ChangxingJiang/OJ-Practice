# LeetCode题解(0884)：两句话中的不常见单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(A+B)$   | $O(A+B)$   | 32ms (97.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    A = A.split(" ")
    B = B.split(" ")
    ans = []
    for a in A:
        if a not in B and A.count(a) == 1:
            ans.append(a)
    for b in B:
        if b not in A and B.count(b) == 1:
            ans.append(b)
    return ans
```

