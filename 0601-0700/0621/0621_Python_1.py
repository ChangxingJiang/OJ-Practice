import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        ans = 0
        while True:
            now = 0
            for elem in count.most_common(n + 1):
                if elem[1] > 0:
                    count[elem[0]] -= 1
                    now += 1
                else:
                    break
            if count.most_common(1)[0][1] == 0:
                return ans + now
            ans += max(now, n + 1)


if __name__ == "__main__":
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))  # 8
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))  # 6
    print(Solution().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))  # 16
