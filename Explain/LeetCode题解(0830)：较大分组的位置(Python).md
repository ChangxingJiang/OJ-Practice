# LeetCode题解(0830)：较大分组的位置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/positions-of-large-groups/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (97.22%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def largeGroupPositions(self, S: str) -> List[List[int]]:
    s = 0
    c = S[0]
    ans = []
    for i in range(1, len(S)):
        if S[i] != c:
            if i - s >= 3:
                ans.append([s, i - 1])
            s = i
            c = S[i]
    else:
        if len(S) - s >= 3:
            ans.append([s, len(S) - 1])
    return ans
```