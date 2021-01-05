# LeetCode题解(1711)：大餐计数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-good-meals/)（中等）

标签：数学、哈希表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 4088ms (5.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        count = collections.Counter()

        ans = 0

        for d1 in deliciousness:
            # 统计当前美味程度可以带来的结果数
            if d1 in count:
                ans += count[d1]

            # 记录当前美味程度需要的另一个美味程度
            for i in range(22):  # 0+1=1:2的0次幂;两个2的20次方的和是2的21次方(第68个测试用例)
                d2 = 2 ** i - d1
                if d2 >= 0:
                    count[d2] += 1

        return ans % self._MOD
```

