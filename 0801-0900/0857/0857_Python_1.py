import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        size = len(quality)

        people = [(wage[i] / quality[i], wage[i], quality[i]) for i in range(size)]
        people.sort()
        print(people)

        ans = float("inf")
        heap = []  # 当前工作质量堆
        now = 0

        for person in people:
            heapq.heappush(heap, -person[2])
            now += person[2]

            if len(heap) > K:
                now += heapq.heappop(heap)

            if len(heap) == K:
                ans = min(ans, now * person[0])

        return ans


if __name__ == "__main__":
    # 105.00000
    print(Solution().mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], K=2))

    # 30.66667
    print(Solution().mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], K=3))
