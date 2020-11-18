from typing import List


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["John(27)","Chris(36)"]
    print(Solution().trulyMostPopular(names=["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"],
                                      synonyms=["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]))
