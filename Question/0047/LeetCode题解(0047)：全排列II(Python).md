# LeetCode题解(0047)：实现可包含重复数字序列的全排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/permutations-ii/)（中等）

标签：回溯算法、集合

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×N!)$  | $O(N)$     | 868ms (18.30%) |
| Ans 2 (Python) | $O(N×N!)$  | $O(N)$     | 680ms (18.69%) |
| Ans 3 (Python) | $O(N×N!)$  | $O(N)$     | 48ms (84.10%)  |
| Ans 4 (Python) | $O(N×N!)$  | $O(1)$     | 64ms (37.83%)  |

解法一（没有剪枝的回溯算法）：

```python
class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = set()
        self.now = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def track_back():
            if len(self.now) == len(nums):
                self.ans.add(tuple([nums[i] for i in self.now]))
            for i in range(len(nums)):
                if i not in self.visited:
                    self.visited.add(i)
                    self.now.append(i)
                    track_back()
                    self.now.pop()
                    self.visited.remove(i)

        track_back()

        return [list(e) for e in self.ans]
```

解法二（直接向暂存数组中写入实际值）：

```python
class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = set()
        self.now = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def track_back():
            if len(self.now) == len(nums):
                self.ans.add(tuple(self.now[:]))
            for i in range(len(nums)):
                if i not in self.visited:
                    self.visited.add(i)
                    self.now.append(nums[i])
                    track_back()
                    self.now.pop()
                    self.visited.remove(i)

        track_back()

        return [list(e) for e in self.ans]
```

解法三（增加剪枝条件）：

```python
class Solution:
    def __init__(self):
        self.visited = set()
        self.ans = []
        self.now = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def track_back():
            if len(self.now) == n:
                self.ans.append(self.now[:])
            tmp_set = set()
            for i in range(n):
                if i not in self.visited:
                    if nums[i] in tmp_set:
                        continue
                    tmp_set.add(nums[i])

                    self.visited.add(i)
                    self.now.append(nums[i])
                    track_back()
                    self.now.pop()
                    self.visited.remove(i)

        track_back()

        return self.ans
```

解法四（不占用额外空间）：

```python
class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def track_back(now_idx):
            if now_idx == n - 1:
                self.ans.append(nums[:])
            tmp_set = set()
            for i in range(now_idx, n):
                # 剪枝条件
                if nums[i] in tmp_set:
                    continue
                tmp_set.add(nums[i])

                nums[i], nums[now_idx] = nums[now_idx], nums[i]
                track_back(now_idx + 1)
                nums[i], nums[now_idx] = nums[now_idx], nums[i]

        track_back(0)

        return self.ans
```



