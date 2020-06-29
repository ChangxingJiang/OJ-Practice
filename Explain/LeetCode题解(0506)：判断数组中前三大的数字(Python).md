# LeetCode题解(0506)：判断数组中前三大的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/relative-ranks/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 420ms (27.70%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 84ms (91.78%)  |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用排序后字符串的坐标）：

```python
def findRelativeRanks(self, nums: List[int]) -> List[str]:
    order = sorted(nums, reverse=True)
    ans = []
    for n in nums:
        idx = order.index(n)
        if idx == 0:
            ans.append("Gold Medal")
        elif idx == 1:
            ans.append("Silver Medal")
        elif idx == 2:
            ans.append("Bronze Medal")
        else:
            ans.append(str(idx + 1))
    return ans
```

解法二：

```python
def findRelativeRanks(self, nums: List[int]) -> List[str]:
    order = [-1] * (max(nums) + 1)
    for i in range(len(nums)):
        order[nums[i]] = i
    rank = 1
    for i in order[::-1]:
        if i != -1:
            if rank == 1:
                nums[i] = "Gold Medal"
            elif rank == 2:
                nums[i] = "Silver Medal"
            elif rank == 3:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(rank)
            rank += 1
    return nums
```