from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        size = len(books)

        dp = [1000000] * (size + 1)
        dp[0] = 0

        for i in range(1, size + 1):
            now_width, now_height = 0, 0
            j = i
            while j > 0:
                now_width += books[j - 1][0]
                now_height = max(now_height, books[j - 1][1])
                if now_width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j - 1] + now_height)
                j -= 1

        return dp[-1]


if __name__ == "__main__":
    # 6
    print(Solution().minHeightShelves(books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelf_width=4))
