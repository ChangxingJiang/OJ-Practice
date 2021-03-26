# LeetCode题解(面试10.02)：变位词组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/group-anagrams-lcci/)（中等）

标签：排序、哈希表、字符串

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×ClogC)$ : 其中C为字符串长度 | $O(N×C)$   | 64ms (49.14%) |
| Ans 2 (Python) |                                  |            |               |
| Ans 3 (Python) |                                  |            |               |

解法一：

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = list({tuple(sorted(s)) for s in strs})
        dicts = {elem: i for i, elem in enumerate(sets)}

        ans = [[] for _ in range(len(sets))]
        for s in strs:
            ans[dicts[tuple(sorted(s))]].append(s)

        return ans
```

