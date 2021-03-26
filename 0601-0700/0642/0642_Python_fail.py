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

        def __contains__(self, sentence):
            for node in self.sentence:
                if node.sentence == sentence:
                    return True
            return False

        def sort(self):
            self.sentence.sort(reverse=True)

    def __init__(self, sentences: List[str], times: List[int]):
        self.tree = self.Tree()
        self.nodes = {}

        for i in range(len(sentences)):
            self._add_new_sentence(sentences[i], times[i])

        self.now = self.tree
        self.ss = ""

    def _add_new_sentence(self, sentence: str, times: int):
        if sentence not in self.nodes:
            node = self.Node(sentence, times)
            self.nodes[sentence] = node
            tree = self.tree
            for ch in sentence:
                tree.add(node)
                if ch not in tree.children:
                    tree.children[ch] = self.Tree()
                tree = tree.children[ch]
            tree.add(node)
            tree.children["#"] = True
        else:
            node = self.nodes[sentence]
            node.times += times
            tree = self.tree
            for ch in sentence:
                if sentence in tree:
                    tree.sort()
                else:
                    tree.add(node)
                tree = tree.children[ch]

    def input(self, c: str) -> List[str]:
        self.ss += c

        # 处理当前输入结束的情况
        if c == "#":
            self._add_new_sentence(self.ss[:-1], 1)
            self.now = self.tree
            self.ss = ""
            return []

        # 处理已经没有找到的情况
        if self.now is None:
            return []

        # 当前能够找到的情况
        elif c in self.now.children:
            self.now = self.now.children[c]
            return [str(node) for node in self.now.sentence]

        # 当前未能找到的情况
        else:
            self.now = None
            return []


if __name__ == "__main__":
    obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    print(obj.input("i"))  # ["i love you", "island","i love leetcode"]
    print(obj.input(" "))  # ["i love you","i love leetcode"]
    print(obj.input("a"))  # []
    print(obj.input("#"))  # []
    print(obj.input("i"))  # ["i love you", "island","i love leetcode"]
    print(obj.input(" "))  # ["i love you","i love leetcode","i a"]
    print(obj.input("a"))  # ["i a"]
    print(obj.input("#"))  # []
    print(obj.input("i"))  # ["i love you","island","i a"]
    print(obj.input(" "))  # ["i love you","i a","i love leetcode"]
    print(obj.input("a"))  # ["i a"]
    print(obj.input("#"))  # []
