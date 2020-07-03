# LeetCode题解(1018)：可被5整除的二进制前缀(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 384ms (59.25%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 132ms (90.16%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（朴素算法）：

```python
def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    val = 0
    ans = []
    for a in A:
        val = (val << 1) ^ a
        ans.append(val % 5 == 0)
    return ans
```

解法二（避免大数求余）：

```python
def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    val = 0
    ans = []
    for a in A:
        val = (val << 1 ^ a) % 5
        ans.append(val== 0)
    return ans
```