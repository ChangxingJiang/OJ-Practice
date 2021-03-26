# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, lst):
        self.lst = lst

    def get(self, index: int) -> int:
        return self.lst[index]

    def length(self) -> int:
        return len(self.lst)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])))

    # -1
    print(Solution().findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1])))
