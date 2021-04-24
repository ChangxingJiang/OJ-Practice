from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2

        ans = 0
        for item in items:
            if item[index] == ruleValue:
                ans += 1
        return ans


if __name__ == "__main__":
    # 1
    print(Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
        ruleKey="color", ruleValue="silver"))

    # 2
    print(Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
        ruleKey="type", ruleValue="phone"))
