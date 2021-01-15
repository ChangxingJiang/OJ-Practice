import bisect
from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        C = [0]
        R = [0]
        H = [0]
        for c, r, h in increase:
            C.append(C[-1] + c)
            R.append(R[-1] + r)
            H.append(H[-1] + h)

        ans = []
        for c, r, h in requirements:
            d1 = bisect.bisect_left(C, c)
            d2 = bisect.bisect_left(R, r)
            d3 = bisect.bisect_left(H, h)
            d = max(d1, d2, d3)
            ans.append(d if d <= len(increase) else -1)

        return ans


if __name__ == "__main__":
    # [2,-1,3,-1]
    print(Solution().getTriggerTime(increase=[[2, 8, 4], [2, 5, 0], [10, 9, 8]],
                                    requirements=[[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]))

    # [-1,4,3,3,3]
    print(Solution().getTriggerTime(increase=[[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]],
                                    requirements=[[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]]))

    # [0]
    print(Solution().getTriggerTime(increase=[[1, 1, 1]],
                                    requirements=[[0, 0, 0]]))
