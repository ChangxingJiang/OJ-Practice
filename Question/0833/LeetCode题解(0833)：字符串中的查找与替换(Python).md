# LeetCode题解(0833)：字符串中指定位置替换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-and-replace-in-string/)（中等）

标签：字符串

| 解法           | 时间复杂度             | 空间复杂度        | 执行用时      |
| -------------- | ---------------------- | ----------------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ : N为操作数 | $O(N)$: N为操作数 | 40ms (97.22%) |
| Ans 2 (Python) |                        |                   |               |
| Ans 3 (Python) |                        |                   |               |

解法一：

```python
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        new_indexes = sorted([(indexes[i], i) for i in range(len(indexes))], key=lambda k: k[0])
        idx_change = 0  # 坐标变化
        for i in range(len(new_indexes)):
            index = new_indexes[i]
            idx = index[0] + idx_change
            n1 = len(sources[index[1]])
            n2 = len(targets[index[1]])
            if S[idx:idx + n1] == sources[index[1]]:
                S = S[:idx] + targets[index[1]] + S[idx + n1:]
                idx_change += n2 - n1
        return S
```