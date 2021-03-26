# LeetCode题解(0710)：黑名单中的随机数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/random-pick-with-blacklist/)（困难）

标签：哈希表、随机、排序、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(BlogB)$ | $O(B)$     | 364ms (83.01%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（黑名单映射）：

```python
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.black = {}

        black_set = set(blacklist)
        last = N - 1

        # 保证黑名单连续数字不相同（如果黑名单超过白名单长度则为-1,-2，仍然会在白名单中向前遍历）
        blacklist.sort()
        for black in blacklist:
            while last in black_set:
                last -= 1
            self.black[black] = last
            last -= 1

        self.n = N - len(black_set)

        print(self.n, self.black)

    def pick(self) -> int:
        r = random.randint(0, self.n - 1)
        return self.black[r] if r in self.black else r
```