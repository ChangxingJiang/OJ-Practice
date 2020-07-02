from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {
            "5": 0,  # 5美元的数量
            "10": 0  # 10美元的数量
        }
        
        for bill in bills:
            if bill == 5:
                count["5"] += 1
            elif bill == 10:
                if count["5"] < 1:
                    return False
                else:
                    count["5"] -= 1
                    count["10"] += 1
            else:
                if count["10"] < 1:
                    if count["5"] < 3:
                        return False
                    else:
                        count["5"] -= 3
                else:
                    if count["5"] < 1:
                        return False
                    else:
                        count["5"] -= 1
                        count["10"] -= 1
        else:
            return True


if __name__ == "__main__":
    print(Solution().lemonadeChange([5, 5, 5, 10, 20]))  # True
    print(Solution().lemonadeChange([5, 5, 10]))  # True
    print(Solution().lemonadeChange([10, 10]))  # False
    print(Solution().lemonadeChange([5, 5, 10, 10, 20]))  # False
