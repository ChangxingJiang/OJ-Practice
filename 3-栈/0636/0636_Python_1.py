from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().exclusiveTime(n=2,
                                   logs=["0:start:0",
                                         "1:start:2",
                                         "1:end:5",
                                         "0:end:6"]))  # [3,4]
