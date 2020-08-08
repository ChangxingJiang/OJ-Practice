from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().braceExpansionII("{a,b}{c,{d,e}}"))  # ["ac","ad","ae","bc","bd","be"]
    print(Solution().braceExpansionII("{{a,z},a{b,c},{ab,z}}"))  # ["a","ab","ac","z"]
