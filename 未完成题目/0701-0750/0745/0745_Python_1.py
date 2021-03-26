from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        pass

    def f(self, prefix: str, suffix: str) -> int:
        pass


if __name__ == "__main__":
    obj = WordFilter(["apple"])
    print(obj.f("a", "e"))  # 0
    print(obj.f("b", ""))  # -1
