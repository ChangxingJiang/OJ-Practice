from typing import List


class AutocompleteSystem:
    class Node:
        __slots__ = ("sentence", "times")

        def __init__(self, sentence, times):
            self.sentence = sentence
            self.times = times

        def __lt__(self, other):
            return (-self.times, self.sentence) > (-other.times, other.sentence)

        def __gt__(self, other):
            return (-self.times, self.sentence) < (-other.times, other.sentence)

        def __str__(self):
            return self.sentence

    class Tree:
        __slots__ = ("children", "sentence")

        def __init__(self):
            self.children = {}
            self.sentence = []

        def add(self, node):
            if len(self.sentence) < 3:
                self.sentence.append(node)
                self.sentence.sort(reverse=True)
            elif self.sentence[-1] < node:
                self.sentence.append(node)
                self.sentence.sort(reverse=True)
                self.sentence.pop()

    def __init__(self, sentences: List[str], times: List[int]):
        self.tree = self.Tree()

        for i in range(len(sentences)):
            self._add_new_sentence(sentences[i], times[i])

        self.now = self.tree

    def _add_new_sentence(self, sentence: str, times: int):
        node = self.Node(sentence, times)
        tree = self.tree
        for ch in sentence:
            tree.add(node)
            if ch not in tree.children:
                tree.children[ch] = self.Tree()
            tree = tree.children[ch]
        tree.add(node)
        tree.children["#"] = True

    def input(self, c: str) -> List[str]:
        # 处理已经没有找到的情况
        if self.now is None:
            res = []

        # 当前能够找到的情况
        elif c in self.now.children:
            self.now = self.now.children[c]
            res = [str(node) for node in self.now.sentence]

        # 当前未能找到的情况
        else:
            self.now = None
            res = []

        if c == "#":
            self.now = self.tree

        return res


if __name__ == "__main__":
    obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    print(obj.input("i"))  # ["i love you", "island","i love leetcode"]
    print(obj.input(" "))  # ["i love you","i love leetcode"]
    print(obj.input("a"))  # []
    print(obj.input("#"))  # []
