from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_set = set()
        for order in orders:
            if order[2] not in food_set:
                food_set.add(order[2])

        food_lst = list(sorted(food_set))
        food_num = len(food_lst)
        food_dic = {food: i for i, food in enumerate(food_lst)}

        table_dic = {}
        for order in orders:
            table, food = int(order[1]), order[2]
            if table not in table_dic:
                table_dic[table] = [0] * food_num
            table_dic[table][food_dic[food]] += 1

        result = [["Table"] + food_lst]
        for table in sorted(table_dic.keys()):
            result.append([str(table)] + [str(n) for n in table_dic[table]])

        return result


if __name__ == "__main__":
    # [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
    print(Solution().displayTable(
        orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
