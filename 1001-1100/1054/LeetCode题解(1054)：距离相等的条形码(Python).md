# LeetCode题解(1054)：距离相等的条形码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distant-barcodes/)（中等）

标签：堆、哈希表、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 540ms (45.93%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（堆）：

```python
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)

        ans = []
        last = None
        while heap:
            v1, k1 = heapq.heappop(heap)
            if k1 != last:
                ans.append(k1)
                last = k1
                if v1 + 1 < 0:
                    heapq.heappush(heap, (v1 + 1, k1))
            else:
                v2, k2 = heapq.heappop(heap)
                ans.append(k2)
                last = k2
                heapq.heappush(heap, (v1, k1))
                if v2 + 1 < 0:
                    heapq.heappush(heap, (v2 + 1, k2))
        return ans
```