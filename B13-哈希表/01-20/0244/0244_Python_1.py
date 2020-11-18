from typing import List


class WordDistance:

    def __init__(self, words: List[str]):
        pass

    def shortest(self, word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    obj = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(obj.shortest("coding", "practice"))  # 3
    print(obj.shortest("makes", "coding"))  # 1
