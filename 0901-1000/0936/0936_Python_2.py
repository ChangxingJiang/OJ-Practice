import collections
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)

        queue = collections.deque()  # 当前新变化的坐标
        done = [False] * N  # 完成情况

        ans = []

        # 生成完成列表
        A = []
        for i in range(N - M + 1):
            made, todo = set(), set()
            for j, sch in enumerate(stamp):
                tch = target[i + j]
                if tch == sch:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))

            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        while queue:
            i = queue.popleft()
            for j in range(max(0, i - M - 1), min(N - M, i) + 1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for m in A[j][0]:
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        if all(done):
            return ans[::-1]
        else:
            return []


if __name__ == "__main__":
    print(Solution().movesToStamp(stamp="abc", target="ababc"))  # [0,2]
    print(Solution().movesToStamp(stamp="abca", target="aabcaca"))  # [3,0,1]
    print(Solution().movesToStamp(stamp="zbs", target="zbzbsbszbssbzbszbsss"))  # [11,9,17,10,6,5,3,1,16,14,13,8,4,0,15,12,7,2]
