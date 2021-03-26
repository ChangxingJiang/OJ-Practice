# LeetCode精讲(0703)：数据流中的第K大元素(Python)

## 题目内容

设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

**示例：**

```
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
```

**说明：**

你可以假设 nums 的长度≥ k-1 且 k ≥ 1。

> 来源：力扣（LeetCode）
> 
> 链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream

## 解法效率

| 解法           | 时间复杂度                        | 空间复杂度 | 执行用时       |
| -------------- | --------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造：$O(NlogN)$；插入：$O(logN)$ | $O(N)$     | 192ms (39.20%) |
| Ans 2 (Python) | 构造：$O(NlogN)$；插入：$O(logk)$ | $O(N)$     | 160ms (50.05%) |
| Ans 3 (Python) | --                                | $O(N)$     | 104ms (99.51%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（二分插入）

> **【思路】**
>
> 根据题目要求，我们很容易想到建立一个排序数组，将每次添加的数字按顺序插入到数组中，并取出数组第k大的数值。
>
> 这种方法在构造时需要排序，时间复杂度为O(NlogN)；之后每次插入的时间复杂度都是二分查找的O(logN)。

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        left = 0
        right = len(self.nums)
        idx = (left + right) // 2
        while left < right:
            if val < self.nums[idx]:
                right = idx
            elif val > self.nums[idx]:
                left = idx + 1
            else:
                break
            idx = (left + right) // 2
        self.nums.insert(idx, val)
        return self.nums[-self.k]
```

### 解法二（二分插入；只存储最大的k个数）

> **【思路】**
>
> 因为我们只会向排序数组中添加新元素，而不会移除已有的元素，已经不是最大的k个数的数，将永远不会成为最大的k个数；所以，我们可以将最大的k个数以外的其他数移除，不再存储。
>
> 这种方法在构造时需要完整排序，时间复杂度为O(NlogN)；但是之后每次插入都是二分查找k个数，其时间复杂度为O(logk)。

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.k = k
        self.nums = nums[-self.k:]

    def add(self, val: int) -> int:
        left = 0
        right = len(self.nums)
        idx = (left + right) // 2
        while left < right:
            if val < self.nums[idx]:
                right = idx
            elif val > self.nums[idx]:
                left = idx + 1
            else:
                break
            idx = (left + right) // 2
        if len(self.nums) > self.k:
            if idx > 0:
                self.nums.insert(idx, val)
                self.nums.pop(0)
        else:
            self.nums.insert(idx, val)
        return self.nums[-self.k]
```

### 解法三（使用heapq）

> **【思路】**
>
> 因为我们每次都需要将排序数组中最小的元素取出，所以我们也可以使用heapq堆实现，一直维护k个最大的数的数组。
>
> heapq包含6个常用的函数：
>
> * heappush(heap, x)  将x压入堆
>
> * heappop(heap)  取出堆中最小的元素
> * heapify(heap)  让列表具备堆特征
> * heapreplace(heap, x)  弹出堆中最小的元素，再将x压入堆（注意先后顺序）
> * nlargest(n, iter)  返回堆中最大的n个元素
> * nsmallest(n, iter)  返回堆中最小的n个元素
>
> 具体实现如下：

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        if len(nums) == k - 1:
            self.heap = nums + [float("-inf")]
        else:
            self.heap = nums

        heapq.heapify(self.heap)

        print(self.heap)
        for _ in range(len(nums) - k):
            heapq.heappop(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        print(self.heap)
        return self.heap[0]
```