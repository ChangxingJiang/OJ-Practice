# LeetCode题解(1439)：有序矩阵中的第k个最小数组和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)（困难）

标签：堆

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(Klog(NK))$ | $O(N×K)$   | 128ms (93.80%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # k不大于200，但是所有可能的组合有m^n种，所以用堆可能更合适
        size1, size2 = len(mat), len(mat[0])

        heap = []
        visited = {(0,) * size1}
        heapq.heappush(heap, (sum(m[0] for m in mat), (0,) * size1))

        for _ in range(k - 1):
            val, lst = heapq.heappop(heap)
            for k in range(size1):
                if lst[k] + 1 < size2:
                    new_lst = lst[:k] + (lst[k] + 1,) + lst[k + 1:]
                    if new_lst not in visited:
                        visited.add(new_lst)
                        heapq.heappush(heap, (val + mat[k][lst[k] + 1] - mat[k][lst[k]], tuple(new_lst)))

        return heapq.heappop(heap)[0]
```