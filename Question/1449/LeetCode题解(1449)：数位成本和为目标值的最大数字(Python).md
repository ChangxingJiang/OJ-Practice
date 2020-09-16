# LeetCode题解(1449)：数位成本和为目标值的最大数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target/)（困难）

标签：字符串、动态规划

| 解法           | 时间复杂度                           | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(9^N)$ : 其中N为最长可能结果的位数 | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(T)$ : 其中T为target的值           | $O(T)$     | 420ms (43.94%) |
| Ans 3 (Python) | $O(T)$ : 其中T为target的值           | $O(T)$     | 224ms (92.94%) |

解法一（异常暴力到难以想象的回溯算法）：

```python
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 排序的所有成本选择
        ordered_cost = list(sorted(set(cost)))
        N = len(ordered_cost)

        # 回溯算法计算最多位数的选择
        length = target // ordered_cost[0]  # 最大可能位数
        lst = [0] * length  # 当前成本列表
        now = ordered_cost[0] * length  # 当前总成本
        maybe_lst = []
        while True:
            # 如果等于目标结果，则提取目标结果
            if now == target:
                maybe_lst.append(tuple(lst))

            # 继续完成回溯算法
            this_idx = lst.pop()  # 当前被替换对象
            next_idx = this_idx + 1
            now -= ordered_cost[this_idx]
            # 如果当前最后一位可以被替换为更大的且不超过target，则替换最后一位
            if next_idx < N and now + ordered_cost[next_idx] <= target:
                num = (target - now) // ordered_cost[next_idx]
                lst += [next_idx] * num
                now += ordered_cost[next_idx] * num

            # 如果当前最后一位不能被替换为更大的且不超过target，则替换前一位
            elif lst:
                this_idx = lst.pop()  # 当前被替换对象
                now -= ordered_cost[this_idx]
                next_idx = this_idx + 1
                if next_idx < N and now + ordered_cost[next_idx] <= target:
                    num = (target - now) // ordered_cost[next_idx]
                    lst += [next_idx] * num
                    now += ordered_cost[next_idx] * num

            # 如果已回溯到开头
            else:
                break

        # 如果没有回溯到结果则返回"0"
        if not maybe_lst:
            return "0"

        # 生成成本和最大数字的对应表
        cost_dict = {}
        for i, ch in enumerate(reversed(cost)):
            if ch not in cost_dict:
                cost_dict[ch] = 9 - i

        # 生成所有可能的结果
        ans = []
        for elem in maybe_lst:
            maybe_ans = [cost_dict[ordered_cost[elem]] for elem in elem]
            maybe_ans = int("".join([str(elem) for elem in sorted(maybe_ans, reverse=True)]))
            ans.append(maybe_ans)

        return str(max(ans))
```

解法二（动态规划）：

```python
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 生成状态列表
        dp = [tuple()] * (target + 1)
        dp[0] = (0,)

        # 生成成本和最大数字的对应表
        cost_dict = {}
        for i, ch in enumerate(reversed(cost)):
            if ch not in cost_dict:
                cost_dict[ch] = 9 - i

        # 计算状态列表
        for i in range(1, target + 1):
            maybe_lst = []
            for c in cost_dict:
                idx = i - c
                if idx >= 0 and dp[idx]:
                    maybe_lst.append(dp[idx] + (cost_dict[c],))
            if maybe_lst:
                dp[i] = max(maybe_lst, key=lambda x: (len(x), x))

        # 返回结果
        return "".join([str(elem) for elem in dp[-1][1:]]) if dp[-1] else "0"
```

解法三（优化解法二）：

> 使用字符串替换元组

```python
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 生成状态列表
        dp = [""] * (target + 1)
        dp[0] = "0"

        # 生成成本和最大数字的对应表
        cost_dict = {}
        for i, ch in enumerate(reversed(cost)):
            if ch not in cost_dict:
                cost_dict[ch] = str(9 - i)

        # 计算状态列表
        for i in range(1, target + 1):
            maybe_lst = []
            for c in cost_dict:
                idx = i - c
                if idx >= 0 and dp[idx]:
                    maybe_lst.append(dp[idx] + cost_dict[c])
            if maybe_lst:
                dp[i] = max(maybe_lst, key=lambda x: (len(x), x))

        # 返回结果
        return dp[-1][1:] if dp[-1] else "0"
```



