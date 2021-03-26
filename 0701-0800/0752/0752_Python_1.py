import collections
from typing import List


class Solution:
    def openLock(self, dead_ends: List[str], target: str) -> int:
        def neighbors(ss):
            res = []
            for ii in range(4):
                res.append(ss[:ii] + str((int(ss[ii]) - 1) % 10) + ss[ii + 1:])
                res.append(ss[:ii] + str((int(ss[ii]) + 1) % 10) + ss[ii + 1:])
            return res

        dead_ends = set(dead_ends)
        if "0000" in dead_ends or target in dead_ends:
            return -1
        if target == "0000":
            return 0

        visited = dead_ends | {target}
        queue = collections.deque([target])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                s1 = queue.popleft()
                for s2 in neighbors(s1):
                    if s2 == "0000":
                        return step
                    if s2 not in visited:
                        visited.add(s2)
                        queue.append(s2)

        return -1


if __name__ == "__main__":
    # 6
    print(Solution().openLock(dead_ends=["0201", "0101", "0102", "1212", "2002"], target="0202"))

    # 1
    print(Solution().openLock(dead_ends=["8888"], target="0009"))

    # -1
    print(Solution().openLock(dead_ends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
                              target="8888"))

    # -1
    print(Solution().openLock(dead_ends=["0000"], target="8888"))
