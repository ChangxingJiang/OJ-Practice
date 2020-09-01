# LeetCode题解(0632)：包含每个列表中至少一个整数的最小区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/)（困难）

标签：双指针、哈希表、滑动窗口、数学

| 解法           | 时间复杂度         | 空间复杂度 | 执行用时       |
| -------------- | ------------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2×K)$         | $O(N×K)$   | 超出时间限制   |
| Ans 2 (Python) | $O(N^2×K)$         | $O(N×K)$   | 572ms (30.00%) |
| Ans 3 (Python) | $O((N×K)log(N×K))$ | $O(N×K)$   | 228ms (97.85%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（朴素的暴力解法）：

```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 生成初始范围
        scopes = [(n, n) for n in nums[0]]

        # 不断更新范围
        for num in nums[1:]:
            i1, i2 = 0, 0
            new_scopes = []
            while i1 < len(scopes) and i2 < len(num):
                scope = scopes[i1]
                n = num[i2]
                if n <= scope[0]:
                    new_scopes.append((n, scope[1]))
                    i2 += 1
                elif scope[0] < n < scope[1]:
                    new_scopes.append(scope)
                    i1 += 1
                else:
                    new_scopes.append((scope[0], n))
                    i1 += 1
            scopes = new_scopes

        return list(min(scopes, key=lambda s: s[1] - s[0]))
```

解法二（改进的暴力解法）：

```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 生成初始范围
        scopes = [(n, n) for n in nums[0]]

        # 不断更新范围
        for num in nums[1:]:
            i1, i2 = 0, 0
            new_scopes = []
            while i1 < len(scopes) and i2 < len(num):
                scope = scopes[i1]
                n = num[i2]
                if n < scope[0]:
                    if not new_scopes or new_scopes[-1][0] < n:
                        new_scopes.append((n, scope[1]))
                    i2 += 1
                elif scope[0] <= n <= scope[1]:
                    new_scopes.append(scope)
                    i1 += 1
                else:
                    if new_scopes and new_scopes[-1][1] == n:
                        new_scopes.pop()
                    new_scopes.append((scope[0], n))
                    i1 += 1
            scopes = new_scopes

        return list(min(scopes, key=lambda s: s[1] - s[0]))
```

解法三（滑动窗口）：

```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 生成包含序列
        num_count = collections.defaultdict(list)
        for i, num in enumerate(nums):
            for n in num:
                num_count[n].append(i)

        # 依据值排序序列
        idxs = sorted(num_count.keys())

        ans = [idxs[0], idxs[-1]]
        left = 0
        count = collections.Counter()
        need = len(nums)
        for right in idxs:
            for n in num_count[right]:
                count[n] += 1
                if count[n] == 1:
                    need -= 1
            if need == 0:
                while need == 0:
                    for n in num_count[idxs[left]]:
                        count[n] -= 1
                        if count[n] == 0:
                            need += 1
                    left += 1
                if right - idxs[left - 1] < ans[1] - ans[0]:
                    ans = [idxs[left - 1], right]

        return ans
```

