from typing import List

# O(N*m*k)

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            if arr[i:i + m * k] == arr[i:i + m] * k:
                return True
        return False


if __name__ == "__main__":
    print(Solution().containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))  # True
    print(Solution().containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))  # True
    print(Solution().containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))  # False
    print(Solution().containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))  # False
    print(Solution().containsPattern(arr=[2, 2, 2, 2], m=2, k=3))  # False
    print(Solution().containsPattern(arr=[2, 2], m=1, k=2))  # True
