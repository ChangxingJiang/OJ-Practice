# LeetCode题解(0522)：字符串独有的最长子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-uncommon-subsequence-ii/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度                         | 空间复杂度                      | 执行用时      |
| -------------- | ---------------------------------- | ------------------------------- | ------------- |
| Ans 1 (Python) | $O(N^2×C)$ : 其中C为字符串平均长度 | $O(N×C)$: 其中C为字符串平均长度 | 40ms (89.42%) |
| Ans 2 (Python) | $O(N^2×C)$ : 其中C为字符串平均长度 | $O(N×C)$: 其中C为字符串平均长度 | 60ms (11.54%) |
| Ans 3 (Python) |                                    |                                 |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用排序和哈希表减少遍历项）：

```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s: len(s), reverse=True)
        count = collections.Counter(strs)
        visited = []
        for str in strs:
            if count[str] == 1:
                for visit in visited:
                    i1 = 0
                    i2 = 0
                    while i1 < len(str) and i2 < len(visit):
                        if str[i1] == visit[i2]:
                            i1 += 1
                        i2 += 1
                    if i1 == len(str):
                        break
                else:
                    return len(str)
            visited.append(str)
        return -1
```

解法二（直接遍历）：

```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        N = len(strs)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                i1, i2 = 0, 0
                while i1 < len(strs[i]) and i2 < len(strs[j]):
                    if strs[i][i1] == strs[j][i2]:
                        i1 += 1
                    i2 += 1
                if i1 == len(strs[i]):
                    break
            else:
                ans = max(ans, len(strs[i]))
        return ans
```