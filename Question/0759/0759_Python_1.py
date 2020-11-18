import heapq


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # 初始化员工下一次工作开始的时间堆
        # O(NlogN)
        heap = []
        for p in range(len(schedule)):
            people = schedule[p]
            heapq.heappush(heap, (people[0].start, p, 0))
        print(heap)

        # 不断推移时间线
        # O(N^2)
        ans = []
        finish_time = -1
        while heap:
            now_time, p, i = heapq.heappop(heap)

            # 如果工作时间开始于上一段工作时间结束之后，则添加空闲时间段
            if finish_time != -1 and now_time > finish_time:
                ans.append(Interval(finish_time, now_time))

            # 如果当前工作的结束时间比上一段工作的结束时间更晚，则更新工作结束时间
            if schedule[p][i].end > finish_time:
                finish_time = schedule[p][i].end

            # 将该员工下一次工作添加到堆
            if i + 1 < len(schedule[p]):
                heapq.heappush(heap, (schedule[p][i + 1].start, p, i + 1))

        return ans


if __name__ == "__main__":
    # [[3,4]]
    print(Solution().employeeFreeTime([
        [Interval(1, 2), Interval(5, 6)],
        [Interval(1, 3), Interval(4, 10)],
    ]))

    # [[5,6],[7,9]]
    print(Solution().employeeFreeTime([
        [Interval(1, 3), Interval(6, 7)],
        [Interval(2, 4)],
        [Interval(2, 5), Interval(9, 12)],
    ]))
