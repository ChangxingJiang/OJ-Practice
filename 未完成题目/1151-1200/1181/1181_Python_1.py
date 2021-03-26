from typing import List


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["writing code rocks"]
    print(Solution().beforeAndAfterPuzzles(phrases=["writing code", "code rocks"]))

    # ["a chip off the old block party",
    #       "a man on a mission impossible",
    #       "a man on a mission statement",
    #       "a quick bite to eat my words",
    #       "chocolate bar of soap"]
    print(Solution().beforeAndAfterPuzzles(phrases=["mission statement",
                                                    "a quick bite to eat",
                                                    "a chip off the old block",
                                                    "chocolate bar",
                                                    "mission impossible",
                                                    "a man on a mission",
                                                    "block party",
                                                    "eat my words",
                                                    "bar of soap"]))

    # ["a"]
    print(Solution().beforeAndAfterPuzzles(phrases=["a", "b", "a"]))
