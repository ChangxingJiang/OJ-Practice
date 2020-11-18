from typing import List


# 情景模拟
# O(N)
# 数学

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        size = len(arr)

        # 处理长度超过总长的情况
        if k >= size:
            return max(arr)

        now = arr[0]
        win = 0
        idx = 1

        while win < k:
            if arr[idx] > now:
                now = arr[idx]
                win = 1
            else:
                win += 1

            idx = (idx + 1) % size

        return now


if __name__ == "__main__":
    print(Solution().getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2))  # 5
    print(Solution().getWinner(arr=[3, 2, 1], k=10))  # 3
    print(Solution().getWinner(arr=[1, 9, 8, 2, 3, 7, 6, 4, 5], k=7))  # 9
    print(Solution().getWinner(arr=[1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000))  # 99
