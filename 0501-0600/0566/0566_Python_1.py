from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        total = []
        for n in nums:
            for m in n:
                total.append(m)

        size = len(total)
        if r * c != size:
            return nums

        ans = []
        for i in range(r):
            ans.append(total[i * c: i * c + c])
        return ans


if __name__ == "__main__":
    print(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4))  # [[1,2,3,4]]
    print(Solution().matrixReshape([[1, 2], [3, 4]], 2, 4))  # [[1,2],[3,4]]
