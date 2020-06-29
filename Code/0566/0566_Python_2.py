from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        ans = []
        for n in nums:
            for m in n:
                temp.append(m)
                if len(temp) == c:
                    ans.append(temp)
                    temp = []
        else:
            if len(temp) == c:
                ans.append(temp)
            elif len(temp) != 0:
                return nums
        if len(ans) == r:
            return ans
        else:
            return nums


if __name__ == "__main__":
    print(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4))  # [[1,2,3,4]]
    print(Solution().matrixReshape([[1, 2], [3, 4]], 2, 4))  # [[1,2],[3,4]]
