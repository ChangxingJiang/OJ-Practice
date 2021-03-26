# LeetCode题解(0754)：到达终点数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reach-a-number/)（中等）

标签：数学

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(\sqrt{N})$ | $O(1)$     | 132ms (29.20%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def reachNumber(self, target: int) -> int:
        # 1 : [1]
        # 2 : [1,3]
        # 3 : [2,4,6]
        # 4 : [4,6,8,10]
        # 5 : [1,3,5,7,9,11,13,15]
        target = abs(target)
        now = 1
        ans = 0
        while target > 0:
            target -= now
            now += 1
            ans += 1
        if target % 2 == 0:  # 存在于比最大值小的同一步中
            return ans
        else:
            return ans + 1 + ans % 2  # 如果在奇数步，需要走两步；如果在偶数步，需要走一步
```

