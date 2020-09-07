# LeetCode精讲(0475)：查找距离房间最近的供暖器(Python)

## 题目内容

冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。

所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

**说明：**

* 给出的房屋和供暖器的数目是非负数且不会超过 25000。
* 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
* 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
* 所有供暖器都遵循你的半径标准，加热的半径也一样。

**示例 1：**

```
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
```

**示例 2：**

```
输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
```

题目标签：二分查找、数组

> 来源：力扣（LeetCode）
> 
> 链接：https://leetcode-cn.com/problems/heaters
> 

本题的表述可能有一点不清楚（可能是我理解能力太差），给定数组中的数值就是房间或供暖器的坐标，需要求房间到最近的供暖器的最大距离。

## 解法效率

| 解法           | 时间复杂度                    | 空间复杂度                     | 执行用时        |
| -------------- | ----------------------------- | ------------------------------ | --------------- |
| Ans 1 (Python) | O(i) : i为最大房间/供暖器坐标 | O(i) : i为最大房间/供暖器坐标  | 超出内存限制    |
| Ans 2 (Python) | $O(nlogn)$                    | O(m) : m为供暖器数             | 460ms (48.05%)  |
| Ans 3 (Python) | $O(nlogn)$                    | O(n+m): n为房间数，m为供暖器数 | 304ms (100.00%) |

### 解法一（双向遍历暴力解法）：

> **【思路】**
>
> 根据示例的数据，很容易想到通过最基本的双向遍历，来暴力地求出房间距离两侧最近的供暖器的坐标差。但是，因为在测试用例中，存在特别大的坐标；所以这种方法不出意外地超出了内存限制。

```python
def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    # 标注供暖器位置
    distance = [-1] * max(houses + heaters)
    for i in heaters:
        distance[i - 1] = 0

    # 双向遍历
    for i in range(len(distance)):
        if i > 0 and distance[i] == -1 and distance[i - 1] != -1:
            distance[i] = distance[i - 1] + 1

    for i in range(len(distance) - 1, - 1, -1):
        if i < len(distance) - 1 and distance[i + 1] != -1:
            if distance[i] == -1 or distance[i] > distance[i + 1] + 1:
                distance[i] = distance[i + 1] + 1

    # 计算最大值
    maximum = 0
    for i in houses:
        if distance[i - 1] > maximum:
            maximum = distance[i - 1]
    return maximum
```

### 解法二（二分查找）：

> **【思路】**
>
> 因为坐标很大，所以又很容易地想到用二分查找来查找最近的供暖器，并计算坐标差。
>
> 在实现中，先将供暖器的坐标排序，再使用二分查找查找距离房间最近的供暖器并计算房间到供暖器的坐标差。
>
> 这种方法的时间复杂度为排序的O(mlogm)和遍历的O(nlogm)，合计为O((m+n)logm)，最终为O(nlogn)。

```python
def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    heaters.sort()
    # print(heaters)
    maximum = 0
    for idx in houses:
        left = 0
        right = len(heaters) - 1
        distance = 0
        while right - left > 1:
            mid = (left + right) // 2
            if heaters[mid] < idx:
                left = mid
            elif heaters[mid] == idx:
                break
            else:
                right = mid
        else:
            distance = min(abs(idx - heaters[left]), abs(heaters[right] - idx))
        # print(idx, distance, heaters[left], heaters[right])
        if distance > maximum:
            maximum = distance
    return maximum
```

### 解法三（双指针顺序查找）：

> **【思路】**
>
> 因为这里并不是单一的一次查找，而是连续的多次查找，而且在测试用例中，房间数和供暖器数的数量不会很大。
>
> 所以，可以考虑先将房间列表和供暖器列表依据坐标排序，然后使用双指针顺序查找距离房间最近的供暖器，并计算坐标差。
>
> 在实现中，我们直接遍历房间坐标，作为第一个指针；然后使用pos变量存储距离当前房间最近的供暖器坐标，作为第二个指针。
>
> 这种方法的时间复杂度为排序的O(nlogn+mlogm)和遍历的O(n+m)，最终为O(nlogn)。

```python
def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()
    size = len(heaters)
    maximum = 0
    pos = 0
    for idx in houses:
        while pos < size and heaters[pos] < idx:
            pos += 1
        if pos == 0:
            distance = heaters[0] - idx
        elif pos == size:
            distance = idx - heaters[-1]
        else:
            distance = min(idx - heaters[pos - 1], heaters[pos] - idx)
        if distance > maximum:
            maximum = distance
    return maximum
```

