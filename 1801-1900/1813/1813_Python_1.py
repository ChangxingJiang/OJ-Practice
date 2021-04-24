class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1, sentence2 = sentence1.split(" "), sentence2.split(" ")
        size1, size2 = len(sentence1), len(sentence2)

        i, j = 0, 0

        while i < size1 and i < size2:
            if sentence1[i] == sentence2[i]:
                i += 1
            else:
                break

        while j < size1 - i and j < size2 - i:
            if sentence1[size1 - j - 1] == sentence2[size2 - j - 1]:
                j += 1
            else:
                break

        return i + j == min(size1, size2) or (i == size1 == size2 and j == 0)


if __name__ == "__main__":
    print(Solution().areSentencesSimilar(sentence1="My name is Haley", sentence2="My Haley"))  # True
    print(Solution().areSentencesSimilar(sentence1="of", sentence2="A lot of words"))  # False
    print(Solution().areSentencesSimilar(sentence1="Eating right now", sentence2="Eating"))  # True
    print(Solution().areSentencesSimilar(sentence1="Luky", sentence2="Lucccky"))  # False

    # 测试用例101
    print(Solution().areSentencesSimilar(sentence1="Ogn WtWj HneS", sentence2="Ogn WtWj HneS"))  # True

    # 测试用例132
    print(Solution().areSentencesSimilar(sentence1="a", sentence2="a aa a"))  # True
