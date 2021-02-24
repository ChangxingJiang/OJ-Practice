from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1
        for i, n in enumerate(nums):
            if n == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        return True


if __name__ == "__main__":
    print(Solution().kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))  # True
    print(Solution().kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))  # False
    print(Solution().kLengthApart(nums=[1, 1, 1, 1, 1], k=0))  # True
    print(Solution().kLengthApart(nums=[0, 1, 0, 1], k=1))  # True
