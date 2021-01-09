# LeetCode题解(1505)：最多K次交换相邻数位后得到的最小整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)（困难）

标签：贪心算法、树状数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 824ms (55.23%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class RangeUpdateBIT:
    def __init__(self, n: int):
        self.n = n
        self._tree = [0] * (n + 1)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, i: int, x: int):
        self.add(i, x - (self.query(i) - self.query(i - 1)))

    def add(self, i: int, x: int):
        while i <= self.n:
            self._tree[i] += x
            i += RangeUpdateBIT._lowbit(i)

    def range_add(self, l: int, r: int, x: int):
        self.add(l, x)
        self.add(r + 1, -x)

    def query(self, i: int) -> int:
        ans = 0
        while i > 0:
            ans += self._tree[i]
            i -= RangeUpdateBIT._lowbit(i)
        return ans


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        size = len(num)
        nums = [int(ch) for ch in num]

        # 构造各个数字的出现位置列表
        count = [collections.deque() for _ in range(10)]
        for i, n in enumerate(nums):
            count[n].append(i)

        # 构造树状数组
        bit = RangeUpdateBIT(size)

        ans = []

        # 贪心算法生成结果
        now = 0  # 当前的最小数字
        while k:
            # 如果当前的最小数字已经用完，或最小的数字已经不能移动到当前的第一位，则向后继续寻找次小的数字
            while now < 10 and len(count[now]) == 0:
                now += 1

            # 如果已经用完所有的数字，则返回结果
            if now == 10:
                break

            # 计算当前值的最优选择
            idx = now
            while idx < 10 and (len(count[idx]) == 0 or count[idx][0] - bit.query(count[idx][0] + 1) > k):
                idx += 1

            # 计算需要消耗的步数
            need = count[idx][0] - bit.query(count[idx][0] + 1)

            # 将当前数字添加到结果中
            ans.append(idx)

            # 从剩余的步数中减去需要的步数
            k -= need

            #  将所有更靠后的数字的距离-1
            bit.range_add(count[idx][0] + 1, size, 1)

            # 从剩余的数字中移除当前使用的数字
            count[idx].popleft()

        # 处理还交换次数用完后剩余的情况
        while len(ans) < size:
            # 寻找当前下标的最小值
            now = min([i for i in range(10)], key=lambda x: count[x][0] if len(count[x]) > 0 else size)

            ans.append(now)
            count[now].popleft()

        # 整理格式并返回结果
        return "".join([str(n) for n in ans])
```

