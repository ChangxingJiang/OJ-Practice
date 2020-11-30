from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    lst = [1, 1, 1, 2, 2, 3]
    print(Solution().removeDuplicates(lst))  # 5
    print(lst)  # [1,1,2,2,3]

    lst = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().removeDuplicates(lst))  # 7
    print(lst)  # [0,0,1,1,2,3,3]
