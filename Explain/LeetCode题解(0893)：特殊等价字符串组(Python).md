# LeetCode题解(0893)：特殊等价字符串组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/groups-of-special-equivalent-strings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (73.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（转换为等价字符串）：

```python
def numSpecialEquivGroups(self, A: List[str]) -> int:
    def helper(s):
        odd = "".join(sorted(list([s[i] for i in range(len(s)) if i % 2 == 0])))
        even = "".join(sorted(list([s[i] for i in range(len(s)) if i % 2 == 1])))
        return odd + even
    return len(set([helper(a) for a in A]))
```