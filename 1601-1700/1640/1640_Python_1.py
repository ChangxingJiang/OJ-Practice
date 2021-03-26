from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lst = {num: idx for idx, num in enumerate(arr)}
        for piece in pieces:
            last = -1
            for num in piece:
                if num not in lst:
                    return False
                if lst[num] < last:
                    return False
                last = lst[num]
        return True


if __name__ == "__main__":
    print(Solution().canFormArray(arr=[85], pieces=[[85]]))  # True
    print(Solution().canFormArray(arr=[15, 88], pieces=[[88], [15]]))  # True
    print(Solution().canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]))  # False
    print(Solution().canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]))  # True
    print(Solution().canFormArray(arr=[1, 3, 5, 7], pieces=[[2, 4, 6, 8]]))  # False
