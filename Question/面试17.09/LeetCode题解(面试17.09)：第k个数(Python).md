# LeetCode题解(面试17.09)：第k个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/get-kth-magic-number-lcci/)（中等）

标签：堆、数学、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K^3)$   | $O(K^3)$   | 超出时间限制  |
| Ans 2 (Python) | $O(K)$     | $O(K)$     | 44ms (57.61%) |
| Ans 3 (Python) | $O(K)$     | $O(K)$     | 40ms (77.28%) |

解法一（暴力堆）：

```python
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        # 每个数的最多次数
        num = k // 3 + 1

        heap = []
        for i3 in range(num + 1):
            for i5 in range(num + 1):
                for i7 in range(num + 1):
                    heapq.heappush(heap, (3 ** i3) * (5 ** i5) * (7 ** i7))

        for i in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)
```

解法二（维护最小倍数堆）：

```python
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        heap = [1]
        heap_set = {1}

        for _ in range(k - 1):
            x = heapq.heappop(heap)
            bigger = x * 3, x * 5, x * 7
            for y in bigger:
                if y not in heap_set:
                    heap_set.add(y)
                    heapq.heappush(heap,y)

        return heapq.heappop(heap)
```

解法三（三指针）：

```python
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        lst = [0] * k
        lst[0] = 1
        p3 = p5 = p7 = 0  # *3、*5、*7分别乘过的坐标
        for i in range(1, k):
            lst[i] = (min(lst[p3] * 3, lst[p5] * 5, lst[p7] * 7))

            # 通过分别比较3个数实现去重（如果同时是两个的倍数，两个数乘到的位置均加1）
            if lst[i] == lst[p3] * 3:
                p3 += 1
            if lst[i] == lst[p5] * 5:
                p5 += 1
            if lst[i] == lst[p7] * 7:
                p7 += 1

        return lst[k - 1]
```