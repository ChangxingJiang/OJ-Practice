from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(v):
            hashmap = set()
            for i in range(len(A) - v + 1):
                hashmap.add("".join(str(a) for a in A[i:i + v]))
            for i in range(len(B) - v + 1):
                if "".join(str(b) for b in B[i:i + v]) in hashmap:
                    return True
            return False

        ans = 0
        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


if __name__ == "__main__":
    print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
    print(Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))  # 5
