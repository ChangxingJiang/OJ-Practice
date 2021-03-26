# LeetCode题解(0358)：K距离间隔重排字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rearrange-string-k-distance-apart/)（困难）

标签：堆、贪心算法、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogK)$ | $O(N+K)$   | 100ms (89.09%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        size = len(s)

        # 生成字符数量堆
        count = collections.Counter(s)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)

        # 生成字符等待队列
        queue = collections.deque()

        ans = []
        for i in range(size):
            # 取出等待队列队首的字符
            if i >= k and queue:
                element = queue.popleft()
                if element != (None, None):
                    heapq.heappush(heap, element)

            # 从堆中提取频率最高的字符
            if not heap:
                return ""
            count, ch = heapq.heappop(heap)

            # 将字符添加到结果
            ans.append(ch)

            # 将字符添加到等待队列
            if count + 1 < 0:
                queue.append((count + 1, ch))
            else:
                queue.append((None, None))  # 如果字符已经用完则添加空位

        return "".join(ans)
```