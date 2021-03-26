from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        now = 0
        for log in logs:
            if log == "../":
                now = max(0, now - 1)
            elif log == "./":
                continue
            else:
                now += 1
        return now


if __name__ == "__main__":
    print(Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))  # 2
    print(Solution().minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]))  # 3
    print(Solution().minOperations(logs=["d1/", "../", "../", "../"]))  # 0
