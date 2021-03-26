# LeetCode题解(0406)：根据身高重建队列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 640ms (6.00%)  |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 108ms (90.43%) |
| Ans 3 (Python) |            |            |                |

解法一（贪心算法）：

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 以高度整理数据
        # 时间:O(N) 空间:O(N)
        count = defaultdict(list)
        for h, k in people:
            count[h].append(k)

        size = len(people)

        # 贪心算法：从小到大考虑填写
        ans = [[-1, -1]] * size
        for h in sorted(count.keys()):
            k_list = list(sorted(count[h]))

            j, now = 0, -1
            for i in range(size):
                if ans[i] == [-1, -1]:
                    now += 1
                    if now == k_list[j]:
                        ans[i] = [h, k_list[j]]
                        j += 1
                        if j == len(k_list):
                            break
            # print(ans)

        return ans
```

解法二（贪心算法）：

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 排序数组
        # 时间:O(NlogN) 空间:O(N)
        people.sort(key=lambda x: (-x[0], x[1]))

        # 从大到小插入
        # 时间:O(N^2) 空间:O(N)
        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans
```