# LeetCode题解(0846)：一手顺子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/hand-of-straights/)（中等）

标签：有序映射

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (96.30%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        size = len(hand)

        if size % W != 0:
            return False

        def get_num(nums):
            lst = [0] * (len(nums) + 1)
            now = 0
            for i in range(len(nums)):
                if nums[i] > now:
                    lst[i] += (nums[i] - now)
                    if i + W > len(nums):
                        return False
                    lst[i + W - 1] -= (nums[i] - now)
                now += lst[i]
            return now == 0

        count = collections.Counter(hand)

        now_val = []
        now_num = []
        for v in sorted(count):
            if not now_val or now_val[-1] == v - 1:
                now_val.append(v)
                now_num.append(count[v])
            else:
                if not get_num(now_num):
                    return False
                now_val, now_num = [v], [count[v]]

        if not get_num(now_num):
            return False

        return True
```

