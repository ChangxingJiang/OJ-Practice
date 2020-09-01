from typing import List


class Expression(set):
    def __add__(self, other):
        ans = Expression()
        for elem in self:
            ans.add(elem)
        for elem in other:
            ans.add(elem)
        return ans

    def __mul__(self, other):
        ans = Expression()
        for elem1 in self:
            for elem2 in other:
                ans.add(elem1 + elem2)
        return ans


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = [[Expression()]]
        for ch in expression:
            if ch.isalpha():
                if not stack[-1][-1]:
                    stack[-1][-1] = Expression((ch,))
                else:
                    stack[-1][-1] = stack[-1][-1] * Expression((ch,))
            else:
                if ch == "{":
                    stack.append([Expression()])
                elif ch == ",":
                    stack[-1].append(Expression())
                elif ch == "}":
                    now_exp = Expression()
                    for exp in stack.pop():
                        now_exp = now_exp + exp
                    if not stack[-1][-1]:
                        stack[-1][-1] = now_exp
                    else:
                        stack[-1][-1] = stack[-1][-1] * now_exp
            # print(ch, "->", stack)
        return sorted(list(stack[0][0]))


if __name__ == "__main__":
    print(Solution().braceExpansionII("{a,b}{c,{d,e}}"))  # ["ac","ad","ae","bc","bd","be"]
    print(Solution().braceExpansionII("{{a,z},a{b,c},{ab,z}}"))  # ["a","ab","ac","z"]
