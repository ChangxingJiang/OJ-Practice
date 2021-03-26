from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar = set()
        for similar_pair in similarPairs:
            similar.add(tuple(similar_pair))

        size1, size2 = len(sentence1), len(sentence2)

        if size1 != size2:
            return False

        for i in range(size1):
            word1, word2 = sentence1[i], sentence2[i]
            if word1 != word2 and (word1, word2) not in similar and (word2, word1) not in similar:
                return False

        return True


if __name__ == "__main__":
    # True
    print(Solution().areSentencesSimilar(
        ["great", "acting", "skills"],
        ["fine", "drama", "talent"],
        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]]
    ))

    # True
    print(Solution().areSentencesSimilar(
        ["great"],
        ["great"],
        []
    ))

    # True
    print(Solution().areSentencesSimilar(["an", "extraordinary", "meal"],
                                         ["one", "good", "dinner"],
                                         [["great", "good"], ["extraordinary", "good"], ["well", "good"],
                                          ["wonderful", "good"], ["excellent", "good"], ["fine", "good"],
                                          ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"],
                                          ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"],
                                          ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"],
                                          ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"],
                                          ["take", "have"], ["fruits", "meal"], ["brunch", "meal"],
                                          ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"],
                                          ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"],
                                          ["have", "own"], ["extremely", "very"], ["actually", "very"],
                                          ["really", "very"], ["super", "very"]]))

    # False
    print(Solution().areSentencesSimilar(["an", "extraordinary", "meal"],
                                         ["a", "good", "dinner"],
                                         [["great", "good"], ["extraordinary", "good"], ["well", "good"],
                                          ["wonderful", "good"], ["excellent", "good"], ["fine", "good"],
                                          ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"],
                                          ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"],
                                          ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"],
                                          ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"],
                                          ["take", "have"], ["fruits", "meal"], ["brunch", "meal"],
                                          ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"],
                                          ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"],
                                          ["have", "own"], ["extremely", "very"], ["actually", "very"],
                                          ["really", "very"], ["super", "very"]]))
