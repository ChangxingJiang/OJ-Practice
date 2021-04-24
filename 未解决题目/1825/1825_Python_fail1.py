import collections
import heapq


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.c = m - 2 * k  # 有效数值数量

        self._queue = collections.deque()  # 当前容器的双端队列
        self._min_remove = collections.Counter()  # 最小值分界的移除列表
        self._min_left = []  # 最小值区域的堆
        self._min_right = []  # 除最小区域以外的堆
        self._max_remove = collections.Counter()  # 最大值分界的移除列表
        self._max_left = []  # 除最大值区域以外的堆
        self._max_right = []  # 最大区域的堆

        self._sum = 0  # 当前容器中的和（不包括最小值和最大值列表中的数）

    def addElement(self, num: int) -> None:
        print(self._queue, self._min_left, self._min_right, self._max_left, self._max_right)

        # 处理数据流中元素不足的情况
        if len(self._queue) < self.m - 1:
            self._queue.append(num)

        # 处理数据流中元素刚好达到要求的情况
        elif len(self._queue) == self.m - 1:
            # 添加元素
            self._queue.append(num)

            # 构造最小值列表的堆和最大值列表的堆+计算当前容器的和
            sorted_queue = sorted(self._queue)
            self._sum = sum(sorted_queue[self.k:self.m - self.k])
            for i in range(self.m):
                if i < self.k:  # 最小值区域
                    heapq.heappush(self._min_left, -sorted_queue[i])
                    heapq.heappush(self._max_left, -sorted_queue[i])
                elif i < self.m - self.k:  # 使用区域
                    heapq.heappush(self._min_right, sorted_queue[i])
                    heapq.heappush(self._max_left, -sorted_queue[i])
                else:  # 最大值区域
                    heapq.heappush(self._min_right, sorted_queue[i])
                    heapq.heappush(self._max_right, sorted_queue[i])

        # 处理数据流中元素充足的情况
        else:  # len(self._queue) == self.m
            # 处理元素变化
            remove = self._queue.popleft()
            self._min_remove[remove] += 1
            self._max_remove[remove] += 1
            self._queue.append(num)

            # 移除元素和添加元素均在使用区
            if self._min_right[0] <= remove <= -self._max_left[0] and self._min_right[0] <= num <= -self._max_left[0]:
                self._sum = self._sum - remove + num
                heapq.heappush(self._min_right, num)
                heapq.heappush(self._max_left, -num)

            # 移除元素在使用区、添加元素在最小值区域
            if self._min_right[0] <= remove <= -self._max_left[0] and num <= -self._min_left[0]:
                diff = -heapq.heappop(self._min_left[0])  # 从最小值区域移动到使用区的元素
                heapq.heappush(self._min_right, diff)

                self._sum = self._sum - remove + diff

                heapq.heappush(self._min_left, -num)
                heapq.heappush(self._max_left, -num)

            # 移除元素在使用区、添加元素在最大值区域
            if self._min_right[0] <= remove <= -self._max_left[0] and num >= self._max_right[0]:
                diff = heapq.heappop(self._max_right[0])  # 从最大值区域移动到使用区的元素
                heapq.heappush(self._max_left, -diff)

                self._sum = self._sum - remove + diff

                heapq.heappush(self._min_right, num)
                heapq.heappush(self._max_right, num)

            # 移除元素在最小值区域、添加元素在使用区
            elif remove <= -self._min_left[0] and self._min_right[0] <= num <= -self._max_left[0]:
                diff = heapq.heappop(self._min_right[0])  # 从使用区域移动到最小值的元素
                heapq.heappush(self._min_left, -diff)

                self._sum = self._sum - diff + remove

                heapq.heappush(self._min_right, num)
                heapq.heappush(self._max_left, -num)

            # 移除元素和添加元素均在最小值区域
            elif remove <= -self._min_left[0] and num <= -self._min_left[0]:
                heapq.heappush(self._min_left, -num)
                heapq.heappush(self._max_left, -num)

            # 移除元素在最小值区域、添加元素在最大值区域
            elif remove <= -self._min_left[0] and self._min_right[0] <= num <= -self._max_left[0]:
                diff1 = heapq.heappop(self._min_right[0])  # 从使用区域移动到最小值的元素
                heapq.heappush(self._min_left, -diff1)
                diff2 = heapq.heappop(self._max_right[0])  # 从最大值区域移动到使用区域的元素
                heapq.heappush(self._max_left, -diff2)

                self._sum = self._sum + diff2 - diff1

                heapq.heappush(self._min_right, num)
                heapq.heappush(self._max_right, num)

            # 移除元素在最大值区域、添加元素在使用区
            elif remove >= self._max_right[0] and self._min_right[0] <= num <= -self._max_left[0]:
                diff = -heapq.heappop(self._max_left[0])  # 从使用区域移动到最大值的元素
                heapq.heappush(self._max_right, diff)

                self._sum = self._sum - diff + remove

                heapq.heappush(self._min_right, num)
                heapq.heappush(self._max_left, -num)

            # 移除元素在最大值区域、添加元素在最小值区域
            elif remove >= self._max_right[0] and num <= -self._min_left[0]:
                diff1 = -heapq.heappop(self._min_left[0])  # 从最小值区域移动到使用区域的元素
                heapq.heappush(self._min_left, diff1)
                diff2 = -heapq.heappop(self._max_left[0])  # 从使用区域移动到最大值区域的元素
                heapq.heappush(self._max_left, diff2)

                self._sum = self._sum + diff1 - diff2

                heapq.heappush(self._min_left, -num)
                heapq.heappush(self._max_left, -num)

            # 移除元素和添加元素均在最大值区域
            elif remove >= self._max_right[0] and num >= self._max_right[0]:
                heapq.heappush(self._min_right, num)
                heapq.heappush(self._max_right, num)

            # 更新已被移除的元素的情况
            while self._min_remove[-self._min_left[0]] > 0:
                remove = -self._min_left[0]
                heapq.heappop(self._min_left)
                self._min_remove[remove] -= 1

            while self._min_remove[self._min_right[0]] > 0:
                remove = self._min_right[0]
                heapq.heappop(self._min_remove[remove])
                self._min_remove[remove] -= 1

    def calculateMKAverage(self) -> int:
        # 处理数据流中元素不足的情况
        if len(self._queue) < self.m:
            return -1

        # 处理数据流中元素充足的情况
        else:
            return round(self._sum / self.c)


if __name__ == "__main__":
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    print(obj.calculateMKAverage())  # -1
    obj.addElement(10)
    print(obj.calculateMKAverage())  # 3
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())  # 5
