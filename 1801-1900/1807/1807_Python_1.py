from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {key: value for key, value in knowledge}

        ans = []
        left, right = -1, -1
        for i, ch in enumerate(s):
            if ch == "(":
                left = i
                ans.append(s[right + 1:left])
            elif ch == ")":
                right = i
                key = s[left + 1:right]
                if key in knowledge:
                    ans.append(knowledge[key])
                else:
                    ans.append("?")
        ans.append(s[right + 1:])

        return "".join(ans)


if __name__ == "__main__":
    # "bobistwoyearsold"
    print(Solution().evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
    # "hi?"
    print(Solution().evaluate(s="hi(name)", knowledge=[["a", "b"]]))
    # "yesyesyesaaa"
    print(Solution().evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]]))
    # "ba"
    print(Solution().evaluate(s="(a)(b)", knowledge=[["a", "b"], ["b", "a"]]))
