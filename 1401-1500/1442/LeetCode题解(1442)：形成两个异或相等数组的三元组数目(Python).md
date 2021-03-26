# LeetCode题解(1442)：形成两个异或相等数组的三元组数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)（中等）

标签：数组、位运算、数学、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (89.42%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        now = 0
        count = {now: [1, -1, 0]}
        for i, n in enumerate(arr):
            now ^= n
            if now in count:
                a, b, c = count[now]  # 出现次数总计，上一次出现的坐标、、总计出现次数
                res = (i - b) * a + c - 1
                ans += res
                count[now] = [a + 1, i, res]
            else:
                count[now] = [1, i, 0]

        return ans
```

