from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))  # 3
    print(Solution().numOfSubarrays(arr=[1, 1, 1, 1, 1], k=1, threshold=0))  # 5
    print(Solution().numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))  # 6
    print(Solution().numOfSubarrays(arr=[7, 7, 7, 7, 7, 7, 7], k=7, threshold=7))  # 1
    print(Solution().numOfSubarrays(arr=[4, 4, 4, 4], k=4, threshold=1))  # 1
