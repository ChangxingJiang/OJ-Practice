from typing import List


class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        word_lst = set()
        for word1, word2 in pairs:
            word_lst.add(word1)
            word_lst.add(word2)
        word_lst = list(word_lst)
        word_dic = {word: i for i, word in enumerate(word_lst)}

        size = len(word_lst)
        dsu = DSU(size)

        for word1, word2 in pairs:
            dsu.union(word_dic[word1], word_dic[word2])

        for i in range(len(words1)):
            word1, word2 = words1[i], words2[i]

            if word1 != word2:
                if word1 not in word_dic or word2 not in word_dic or dsu.find(word_dic[word1]) != dsu.find(word_dic[word2]):
                    return False

        return True


if __name__ == "__main__":
    # True
    print(Solution().areSentencesSimilarTwo(
        words1=["great", "acting", "skills"],
        words2=["fine", "drama", "talent"],
        pairs=[["great", "fine"], ["acting", "drama"], ["skills", "talent"]]))

    # True
    print(Solution().areSentencesSimilarTwo(
        words1=["great"],
        words2=["great"],
        pairs=[]))

    # False
    print(Solution().areSentencesSimilarTwo(
        words1=["great"],
        words2=["doubleplus", "good"],
        pairs=[]))
