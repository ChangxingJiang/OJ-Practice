# LeetCode题解(1497)：检查数组对是否可以被k整除(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k/)（中等）

标签：贪心算法、数组、哈希表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 264ms (13%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = collections.Counter()

        # 统计余数
        for num in arr:
            surplus = num % k
            count[surplus] += 1

        for surplus, num in count.items():
            # 处理余数为0的情况
            if surplus == 0:
                if num % 2 != 0:
                    return False

            # 处理余数不为0的情况
            else:
                if num != count[k - surplus]:
                    return False

        return True
```