from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    #  [1, 4, 1, 5, 1, 6]
    lst = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(lst)
    print(lst)

    #  [2, 3, 1, 3, 1, 2]
    lst = [1, 3, 2, 2, 3, 1]
    Solution().wiggleSort(lst)
    print(lst)
