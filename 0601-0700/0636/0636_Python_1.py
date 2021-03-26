from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        last = 0
        stack = []
        for log in logs:
            idx, status, time = log.split(":")
            idx = int(idx)
            time = int(time)
            if status == "start":
                if stack:
                    ans[stack[-1]] += time - last - 1
                stack.append(idx)
                ans[idx] += 1
                last = time
            else:
                if not stack or stack[-1] != idx:
                    continue
                else:
                    ans[stack[-1]] += time - last
                    stack.pop()
                    last = time
        return ans


if __name__ == "__main__":
    print(Solution().exclusiveTime(n=2,
                                   logs=["0:start:0",
                                         "1:start:2",
                                         "1:end:5",
                                         "0:end:6"]))  # [3,4]
