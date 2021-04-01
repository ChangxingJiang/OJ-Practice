from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        near = defaultdict(set)
        count = Counter()

        for n1, n2 in adjacentPairs:
            near[n1].add(n2)
            near[n2].add(n1)
            count[n1] += 1
            count[n2] += 1

        start = 0
        for num in count:
            if count[num] == 1:
                start = num
                break

        ans = [start]
        while near[ans[-1]]:
            now = ans[-1]
            nxt = near[now].pop()
            near[nxt].remove(now)
            ans.append(nxt)

        return ans


if __name__ == "__main__":
    # [1,2,3,4]
    print(Solution().restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]]))

    # [-2,4,1,-3]
    print(Solution().restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]))

    # [100000,-100000]
    print(Solution().restoreArray(adjacentPairs=[[100000, -100000]]))
