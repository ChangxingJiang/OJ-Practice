from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(q):
            i = 0
            for ch in q:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                else:
                    if ch.isupper():
                        return False
            return i == len(pattern)

        return [check(query) for query in queries]


if __name__ == "__main__":
    print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                                pattern="FB"))  # [true,false,true,true,false]
    print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                                pattern="FoBa"))  # [true,false,true,false,false]
    print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                                pattern="FoBaT"))  # [false,true,false,false,false]
