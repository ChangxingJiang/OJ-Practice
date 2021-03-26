from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            nid, status, time = log.split(":")
            nid = int(nid)
            time = int(time)
            if status == "start":
                stack.append([nid, time])
            else:
                lid, last = stack.pop()
                interval = time - last + 1
                ans[lid] += interval
                if stack:
                    ans[stack[-1][0]] -= interval
        return ans


if __name__ == "__main__":
    print(Solution().exclusiveTime(n=2,
                                   logs=["0:start:0",
                                         "1:start:2",
                                         "1:end:5",
                                         "0:end:6"]))  # [3,4]
