from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        l1, r1 = intervals[0]
        for i in range(1, len(intervals)):
            l2, r2 = intervals[i]
            if r1 < l2:
                ans.append([l1, r1])
                l1, r1 = l2, r2
            else:  # l2 <= r1
                r1 = max(r1, r2)
        ans.append([l1, r1])
        return ans


if __name__ == "__main__":
    # [[1,6],[8,10],[15,18]]
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))

    # [[1,5]]
    print(Solution().merge(intervals=[[1, 4], [4, 5]]))
