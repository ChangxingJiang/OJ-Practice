import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r"^ *[-+]?(\d+\.?\d*|\.\d+)([Ee][-+]?\d+|) *$", s) is not None


if __name__ == "__main__":
    pass
