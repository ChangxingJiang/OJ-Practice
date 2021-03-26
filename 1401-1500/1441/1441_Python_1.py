from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        source = [i for i in range(1, n + 1)]
        ans = []
        while target and source:
            if target[0] == source[0]:
                target.pop(0)
                source.pop(0)
                ans.append("Push")
            else:
                source.pop(0)
                ans.append("Push")
                ans.append("Pop")
        return ans


if __name__ == "__main__":
    print(Solution().buildArray(target=[1, 3], n=3))  # ["Push","Push","Pop","Push"]
    print(Solution().buildArray(target=[1, 2, 3], n=3))  # ["Push","Push","Push"]
    print(Solution().buildArray(target=[1, 2], n=4))  # ["Push","Push"]
    print(Solution().buildArray(target=[2, 3, 4], n=4))  # ["Push","Pop","Push","Push","Push"]
