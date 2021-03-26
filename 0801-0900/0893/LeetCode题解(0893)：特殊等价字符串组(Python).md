# LeetCode题解(0893)：计算特殊等价字符串组数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/groups-of-special-equivalent-strings/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (73.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（转换为等价字符串）：

```python
def numSpecialEquivGroups(self, A: List[str]) -> int:
    def helper(s):
        odd = "".join(sorted(list([s[i] for i in range(len(s)) if i % 2 == 0])))
        even = "".join(sorted(list([s[i] for i in range(len(s)) if i % 2 == 1])))
        return odd + even
    return len(set([helper(a) for a in A]))
```