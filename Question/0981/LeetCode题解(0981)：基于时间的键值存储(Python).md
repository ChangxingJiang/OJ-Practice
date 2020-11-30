# LeetCode题解(0981)：基于时间的键值存储(Python)

题目：[原题链接](https://leetcode-cn.com/problems/time-based-key-value-store/)（中等）

标签：哈希表、二分查找

| 解法           | 时间复杂度                   | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------- | ---------- | -------------- |
| Ans 1 (Python) | set = $O(1)$ get = $O(logN)$ | $O(N)$     | 768ms (84.81%) |
| Ans 2 (Python) |                              |            |                |
| Ans 3 (Python) |                              |            |                |

解法一：

```python
class TimeMap:

    def __init__(self):
        self.hashmap_t = collections.defaultdict(list)
        self.hashmap_val = collections.defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.hashmap_t[key]:
            bisect.insort_left(self.hashmap_t[key], timestamp)
        self.hashmap_val[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if len(self.hashmap_t[key]) > 0:
            i = bisect.bisect_left(self.hashmap_t[key], timestamp)
            if i >= len(self.hashmap_t[key]):
                i -= 1
            if self.hashmap_t[key][i] > timestamp:
                i -= 1
            # print(i, self.hashmap_t[key], timestamp)
            if i >= 0:
                return self.hashmap_val[key][self.hashmap_t[key][i]]
            else:
                return ""
        else:
            return ""
```