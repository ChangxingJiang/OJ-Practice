# LeetCode题解(1224)：最大相等频率(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-equal-frequency/)（困难）

标签：哈希表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 超出时间限制   |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 160ms (81.02%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        size = len(set(nums))
        count1 = collections.Counter()
        count2 = collections.Counter({0: size})

        ans = 1
        for i, n in enumerate(nums):
            count2[count1[n]] -= 1
            count1[n] += 1
            count2[count1[n]] += 1

            lst1 = [v for k, v in count2.items() if k != 0 and v != 0]
            lst2 = [k for k, v in count2.items() if k != 0 and v != 0]

            # print(i, ":", count1, count2, "->", lst1, lst2)

            # 如果当前所有的数出现次数都是相同的
            if len(lst1) == 1:
                # 如果它们每个数的出现次数不是1
                if lst1[0] != 1:
                    # 那么如果它们不只1个数，则无法实现
                    if lst2[0] != 1:
                        continue

            # 如果当前所有的数有两种不同的出现次数
            if len(lst1) == 2:
                # 如果出现少的一个次数不是一次，则无法实现
                if min(lst1) != 1:
                    continue

            # 如果当前所有的数有三种不同的出现次数，则注定无法实现
            if len(lst1) > 2:
                continue

            ans = max(ans, i + 1)

        return ans
```

解法二：

```python
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        nums += [inf]
        count = collections.Counter(nums)

        # 从后往前遍历
        for i in reversed(range(len(nums))):
            count[nums[i]] -= 1
            lst = sorted(filter(lambda x: x > 0, count.values()))  # 剔除掉是0的出现频率
            if len(lst) == 1 or (lst[0] == 1 and lst[1] == lst[-1]) or (lst[0] == lst[-2] == lst[-1] - 1):
                return i
```