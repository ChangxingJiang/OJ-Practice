# LeetCode题解(0433)：最小基因变化(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-genetic-mutation/)（中等）

标签：广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×8^4)$ | $O(N)$     | 36ms (79.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _CHANGE_LIST = {
        "A": ["C", "G", "T"],
        "C": ["A", "G", "T"],
        "G": ["A", "C", "T"],
        "T": ["A", "C", "G"]
    }

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0

        bank = set(bank)

        def get_change(s1):
            for i, ch1 in enumerate(s1):
                for ch2 in self._CHANGE_LIST[ch1]:
                    s2 = s1[:i] + ch2 + s1[i + 1:]
                    if s2 in bank:
                        yield s2

        visited = set()
        queue = collections.deque([start])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                now = queue.popleft()
                for change in get_change(now):
                    if change == end:
                        return ans
                    if change not in visited:
                        visited.add(change)
                        queue.append(change)

        return -1
```

