import heapq


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


if __name__ == "__main__":
    print(Solution().getKthMagicNumber(5))  # 9
    print(Solution().getKthMagicNumber(7))  # 21
