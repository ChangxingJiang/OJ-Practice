# LeetCode题解(0438)：找到字符串中所有字母异位词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(S+P)$   | $O(P)$     | 160ms (35.34%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size1, size2 = len(s), len(p)
        if size1 < size2:
            return []

        ans = []
        aim = collections.Counter(p)
        count = collections.Counter()
        for i in range(size2):
            count[s[i]] += 1
        if count == aim:
            ans.append(0)
        for i in range(size1 - size2):
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            count[s[i + size2]] += 1
            if count == aim:
                ans.append(i + 1)

        return ans
```