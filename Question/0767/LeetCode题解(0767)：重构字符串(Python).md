# LeetCode题解(0767)：重构字符串至相邻字符不相同(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reorganize-string/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (99.81%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（排序法）：

![LeetCode题解(0767)：截图1](LeetCode题解(0767)：截图1.png)

```python
class Solution:
    def reorganizeString(self, S: str) -> str:
        # 统计每个字母的出现频次
        count = [(S.count(x), x) for x in set(S)]

        # 计算是否可以构成字符串
        if max(count, key=lambda k: k[0])[0] > (len(S) + 1) / 2:
            return ""

        # 构成临时字符串
        count.sort(key=lambda k: k[0])
        nums = []
        for num, x in count:
            nums += [x] * num

        # # 生成结果字符串
        ans = []
        i1 = 0
        i2 = int(len(S) / 2)
        first = True
        for i in range(len(S)):
            if first:
                ans.append(nums[i2])
                i2 += 1
            else:
                ans.append(nums[i1])
                i1 += 1
            first = not first

        return "".join(ans)
```