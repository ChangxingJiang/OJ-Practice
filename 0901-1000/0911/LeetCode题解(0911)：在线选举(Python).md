# LeetCode题解(0911)：在线选举(Python)

题目：[原题链接](https://leetcode-cn.com/problems/online-election/)（中等）

标签：二分查找

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(N)$ ; 查询 = $O(logN)$ | $O(N)$     | 740ms (64.29%) |
| Ans 2 (Python) |                                  |            |                |
| Ans 3 (Python) |                                  |            |                |

解法一：

```python
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.lst = []
        count = collections.Counter()
        max_val, max_num = 0, 0
        for i in range(len(times)):
            count[persons[i]] += 1
            if count[persons[i]] >= max_num:
                max_val, max_num = persons[i], count[persons[i]]
            self.lst.append(max_val)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.lst[idx]
```

