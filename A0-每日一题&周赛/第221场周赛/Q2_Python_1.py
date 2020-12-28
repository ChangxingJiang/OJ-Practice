import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)

        heap = []
        ans = 0

        now = 0

        while now < n or heap:
            # 先接收当天的苹果
            if now < n:
                heapq.heappush(heap, (now + days[now], apples[now]))

            # 再腐烂旧苹果
            while heap and (heap[0][0] <= now or heap[0][1] == 0):
                heapq.heappop(heap)

            if heap:
                heap[0] = (heap[0][0], heap[0][1] - 1)
                ans += 1

            now += 1

        return ans


if __name__ == "__main__":
    print(Solution().eatenApples(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))  # 7
    print(Solution().eatenApples(apples=[3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2]))  # 5
