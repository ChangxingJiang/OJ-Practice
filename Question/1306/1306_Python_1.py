import collections
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)

        dp = [False] * size
        dp[start] = True

        queue = collections.deque([start])

        while queue:
            now_idx = queue.popleft()

            # 已经找到结果
            if arr[now_idx] == 0:
                return True

            next_lst = [now_idx - arr[now_idx], now_idx + arr[now_idx]]
            for next_idx in next_lst:
                if 0 <= next_idx < size and not dp[next_idx]:
                    dp[next_idx] = True
                    queue.append(next_idx)

        return False


if __name__ == "__main__":
    print(Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))  # True
    print(Solution().canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))  # True
    print(Solution().canReach(arr=[3, 0, 2, 1, 2], start=2))  # False
