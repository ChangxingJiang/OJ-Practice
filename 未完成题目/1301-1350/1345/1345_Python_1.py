from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))  # 3
    print(Solution().minJumps(arr=[7]))  # 3
    print(Solution().minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]))  # 3
    print(Solution().minJumps(arr=[6, 1, 9]))  # 3
    print(Solution().minJumps(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))  # 3
