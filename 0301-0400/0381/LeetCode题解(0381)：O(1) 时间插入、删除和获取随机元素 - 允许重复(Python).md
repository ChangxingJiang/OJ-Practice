# LeetCode题解(0381)：设计常数时间插入、删除和获取随机元素（允许重复）的类(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)（困难）

标签：设计、数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 156ms (36%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.dict = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        self.dict[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if self.dict[val]:
            idx = self.dict[val].pop()
            if len(self.nums) > 1 and idx != len(self.nums) - 1:
                self.dict[self.nums[-1]]._remove(len(self.nums) - 1)
                self.dict[self.nums[-1]].add(idx)
                self.nums[idx] = self.nums[-1]
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)
```