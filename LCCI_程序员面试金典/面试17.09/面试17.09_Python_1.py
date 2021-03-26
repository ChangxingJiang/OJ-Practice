import heapq


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


if __name__ == "__main__":
    print(Solution().getKthMagicNumber(5))  # 9
