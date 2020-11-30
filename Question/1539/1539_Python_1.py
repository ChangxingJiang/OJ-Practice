from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        for n in arr:
            last += 1
            if n - last >= k:
                return last + k - 1
            else:
                k -= n - last
                last = n
        return last + k


if __name__ == "__main__":
    print(Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5))  # 9
    print(Solution().findKthPositive(arr=[1, 2, 3, 4], k=2))  # 6
    print(Solution().findKthPositive(arr=[2], k=1))  # 1
