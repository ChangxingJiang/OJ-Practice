from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        ans = 0
        for n in arr:
            if n + 1 in arr_set:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countElements([1, 2, 3]))  # 2
    print(Solution().countElements([1, 1, 3, 3, 5, 5, 7, 7]))  # 0
    print(Solution().countElements([1, 3, 2, 3, 5, 0]))  # 3
    print(Solution().countElements([1, 1, 2, 2]))  # 2
