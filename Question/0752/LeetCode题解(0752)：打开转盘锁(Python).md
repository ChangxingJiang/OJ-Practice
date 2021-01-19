# LeetCode题解(0752)：打开转盘锁(Python)

题目：[原题链接](https://leetcode-cn.com/problems/open-the-lock/)（中等）

标签：广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(10000)$ | $O(10000)$ | 568ms (76.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def openLock(self, dead_ends: List[str], target: str) -> int:
        def neighbors(ss):
            res = []
            for ii in range(4):
                res.append(ss[:ii] + str((int(ss[ii]) - 1) % 10) + ss[ii + 1:])
                res.append(ss[:ii] + str((int(ss[ii]) + 1) % 10) + ss[ii + 1:])
            return res

        dead_ends = set(dead_ends)
        if "0000" in dead_ends or target in dead_ends:
            return -1
        if target == "0000":
            return 0

        visited = dead_ends | {target}
        queue = collections.deque([target])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                s1 = queue.popleft()
                for s2 in neighbors(s1):
                    if s2 == "0000":
                        return step
                    if s2 not in visited:
                        visited.add(s2)
                        queue.append(s2)

        return -1
```

