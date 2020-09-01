import re
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        regex = "^[a-z]*" + "[a-z]*".join(pattern) + "[a-z]*$"  # 整理正则表达式
        return [bool(re.match(regex, query)) for query in queries]


if __name__ == "__main__":
    print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                                pattern="FB"))  # [true,false,true,true,false]
    print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                                pattern="FoBa"))  # [true,false,true,false,false]
    print(Solution().camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                                pattern="FoBaT"))  # [false,true,false,false,false]
