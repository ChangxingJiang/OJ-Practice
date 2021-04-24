import collections
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        count = collections.defaultdict(set)

        for u, t in logs:
            count[u].add(t)

        ans = [0] * k

        for lst in count.values():
            v = len(lst)
            if v - 1 < k:
                ans[v - 1] += 1

        return ans


if __name__ == "__main__":
    # [0,2,0,0,0]
    print(Solution().findingUsersActiveMinutes(logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5))

    # [1,1,0,0]
    print(Solution().findingUsersActiveMinutes(logs=[[1, 1], [2, 2], [2, 3]], k=4))

    # [3, 1]
    print(Solution().findingUsersActiveMinutes(
        logs=[[283268890, 14532], [283268891, 14530], [283268889, 14530], [283268892, 14530], [283268890, 14531]], k=2))
