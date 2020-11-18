from typing import List


class ThroneInheritance:
    class People:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.die = False

    def __init__(self, kingName: str):
        self.head = self.People(kingName)
        self.dic = {kingName: self.head}

    def birth(self, parentName: str, childName: str) -> None:
        people = self.People(childName)
        self.dic[parentName].children.append(people)
        self.dic[childName] = people

    def death(self, name: str) -> None:
        self.dic[name].die = True

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []

        def dfs(node):
            if node:
                if not node.die:
                    self.ans.append(node.name)
                for child in node.children:
                    dfs(child)

        dfs(self.head)

        return self.ans


if __name__ == "__main__":
    t = ThroneInheritance("king")
    t.birth("king", "andy")
    t.birth("king", "bob")
    t.birth("king", "catherine")
    t.birth("andy", "matthew")
    t.birth("bob", "alex")
    t.birth("bob", "asha")
    print(t.getInheritanceOrder())  # ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
    t.death("bob")
    print(t.getInheritanceOrder())  # ["king", "andy", "matthew", "alex", "asha", "catherine"]
