from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(n):
            return bin(n).count("1"), n

        return sorted(arr, key=helper)


if __name__ == "__main__":
    print(Solution().sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))  # [0,1,2,4,8,3,5,6,7]
    print(
        Solution().sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))  # [1,2,4,8,16,32,64,128,256,512,1024]
    print(Solution().sortByBits(arr=[10000, 10000]))  # [10000,10000]
    print(Solution().sortByBits(arr=[2, 3, 5, 7, 11, 13, 17, 19]))  # [2,3,5,17,7,11,13,19]
