# LeetCode题解(0942)：增减字符串匹配(Python)

题目：[原题链接](https://leetcode-cn.com/problems/di-string-match/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制  |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 72ms (87.27%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 76ms (71.61%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def diStringMatch(self, S: str) -> List[int]:
    ans = [0]
    for i in range(len(S)):
        if S[i] == "I":
            ans.append(i + 1)
        else:
            for j in range(len(ans)):
                ans[j] += 1
            ans.append(0)
    return ans
```

解法二：

```python
def diStringMatch(self, S: str) -> List[int]:
    ans = [0]
    a_max = 0
    a_min = 0
    for i in range(len(S)):
        if S[i] == "I":
            a_max += 1
            ans.append(a_max)
        else:
            a_min -= 1
            ans.append(a_min)

    return [a - a_min for a in ans]
```

解法三（减少一次遍历）：

```python
def diStringMatch(self, S: str) -> List[int]:
    ans = []
    a_min, a_max = 0, len(S)
    for s in S:
        if s == "I":
            ans.append(a_min)
            a_min += 1
        else:
            ans.append(a_max)
            a_max -= 1
    return ans + [a_min]
```