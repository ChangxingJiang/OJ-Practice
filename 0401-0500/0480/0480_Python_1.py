import collections
import heapq
from typing import List


class MedianQueue:
    def __init__(self):
        self._left = self._right = 0  # 当前数组中比中位数小和比中位数大的数值数量

        self._smaller = []  # 小于中位数的堆
        self._bigger = []  # 大于中位数的堆
        self._median = None  # 中位数

        self.remove_set = collections.Counter()  # 被移除的值列表

    def append(self, num):
        """将数值添加到集合"""
        self._update()

        if self._left == 0 and self._right == 0:
            # 处理0个值的情况
            if self._median is None:
                self._median = num

            # 处理1个值的情况
            else:
                self._smaller, self._bigger, self._median = [-min(self._median, num)], [max(self._median, num)], None
                self._left += 1
                self._right += 1

        # 处理2+个值的情况
        else:
            # 处理当前有偶数个元素的情况
            if self._median is None:
                if -self._smaller[0] <= num <= self._bigger[0]:
                    self._median = num
                elif num < -self._smaller[0]:
                    heapq.heappush(self._smaller, -num)
                    self._median = -heapq.heappop(self._smaller)
                elif num > self._bigger[0]:
                    heapq.heappush(self._bigger, num)
                    self._median = heapq.heappop(self._bigger)

            # 处理当前有奇数个元素的情况
            else:
                if self._median <= num:
                    heapq.heappush(self._bigger, num)
                    heapq.heappush(self._smaller, -self._median)
                    self._median = None
                else:
                    heapq.heappush(self._smaller, -num)
                    heapq.heappush(self._bigger, self._median)
                    self._median = None
                self._left += 1
                self._right += 1

        # print(self._smaller, self._median, self._bigger, self.remove_set)

    def remove(self, num):
        """将数值移出集合"""
        self._update()

        # 处理第1个值的情况
        if self._left == 0 and self._right == 0:
            self._median = None

        # 处理第2+个值的情况
        else:
            # 处理当前有偶数个元素的情况
            if self._median is None:
                if num <= -self._smaller[0]:
                    self._median = heapq.heappop(self._bigger)
                elif num >= self._bigger[0]:
                    self._median = -heapq.heappop(self._smaller)
                self._left -= 1
                self._right -= 1
                self.remove_set[num] += 1

            # 处理当前有奇数个元素的情况
            else:
                if num > self._median:
                    heapq.heappush(self._bigger, self._median)
                    self._median = None
                    self.remove_set[num] += 1
                elif num < self._median:
                    heapq.heappush(self._smaller, -self._median)
                    self._median = None
                    self.remove_set[num] += 1
                else:
                    self._median = None

        # print(self._smaller, self._median, self._bigger, self.remove_set)

    def median(self):
        """获取当前集合中位数"""
        if self._median is not None:
            return self._median
        else:
            return (self._bigger[0] + (-self._smaller[0])) / 2

    def _update(self):
        """移除延迟删除的内容：中位数旁边已经被移除的值"""
        while self._smaller and self.remove_set[-self._smaller[0]] > 0 and self._left < len(self._smaller):
            self.remove_set[-self._smaller[0]] -= 1
            heapq.heappop(self._smaller)
        while self._bigger and self.remove_set[self._bigger[0]] > 0 and self._right < len(self._bigger):
            self.remove_set[self._bigger[0]] -= 1
            heapq.heappop(self._bigger)


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        queue = MedianQueue()
        for i in range(len(nums)):
            # print("ADD:", nums[i])
            queue.append(nums[i])
            if i >= k:
                # print("REMOVE:", nums[i - k])
                queue.remove(nums[i - k])
            if i >= k - 1:
                ans.append(queue.median())
        return ans


if __name__ == "__main__":
    # [1,-1,-1,3,5,6]
    print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

    # [1,1,1]
    print(Solution().medianSlidingWindow([1, 1, 1, 1], 2))

    # [2.0,3.0,3.0,3.0,2.0,3.0,2.0]
    print(Solution().medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))

    # [8.0,6.0,8.0,8.0,5.0]
    print(Solution().medianSlidingWindow([7, 0, 3, 9, 9, 9, 1, 7, 2, 3], 6))
