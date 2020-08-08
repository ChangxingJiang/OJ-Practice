from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().spellchecker(wordlist=["KiTe", "kite", "hare", "Hare"],
                                  queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet",
                                           "keto"]))  # ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
