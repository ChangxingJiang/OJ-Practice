import re


class Solution:
    def countSegments(self, s: str) -> int:
        return sum([1 for i in re.split(" +", s) if len(i) > 0])


if __name__ == "__main__":
    print(Solution().countSegments("Hello, my name is John"))  # 5
    print(Solution().countSegments("Of all the gin joints in all the towns in all the world,   "))  # 13
