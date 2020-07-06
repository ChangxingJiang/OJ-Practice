from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().buildArray(target=[1, 3], n=3))  # ["Push","Push","Pop","Push"]
    print(Solution().buildArray(target=[1, 2, 3], n=3))  # ["Push","Push","Push"]
    print(Solution().buildArray(target=[1, 2], n=4))  # ["Push","Push"]
    print(Solution().buildArray(target=[2, 3, 4], n=4))  # ["Push","Pop","Push","Push","Push"]
