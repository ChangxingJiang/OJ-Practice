from typing import List


class CustomFunction:
    def f(self, x, y):
        return x + y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        idx1 = 1
        idx2 = 1000
        ans = []
        while idx1 <= 1000 and idx2 >= 1:
            if customfunction.f(idx1, idx2) < z:
                mid = (idx1 + idx2) // 2
                if customfunction.f(mid, idx2) < z:
                    idx1 = max(mid, idx1 + 1)
                else:
                    idx1 += 1
            elif customfunction.f(idx1, idx2) > z:
                mid = (idx1 + idx2) // 2
                if customfunction.f(idx1, mid) > z:
                    idx2 = min(mid, idx2 - 1)
                else:
                    idx2 -= 1
            else:
                ans.append([idx1, idx2])
                idx1 += 1
                idx2 -= 1
        return ans


if __name__ == "__main__":
    print(Solution().findSolution(CustomFunction(), 5))  # [[1,4],[2,3],[3,2],[4,1]]
