"""
题目格式整理

题目列表Url：https://leetcode-cn.com/api/problems/all/
题目翻译Url：https://leetcode-cn.com/graphql
题目标签Url：https://leetcode-cn.com/problems/api/tags/
题目类型Url：https://leetcode-cn.com/problems/api/favorites/
"""

import json

if __name__ == "__main__":
    with open("题目列表(20200617).json", "r")as file:
        question_dict = json.loads(file.read())
    for question_item in question_dict["stat_status_pairs"][::-1]:
        num = question_item["stat"]["frontend_question_id"]  # 题目编号
        title = question_item["stat"]["question__title"]  # 题目标题
        url = "https://leetcode-cn.com/problems/" + question_item["stat"]["question__title_slug"] + "/"
        level = question_item["difficulty"]["level"]
        if level == 1:
            level_name = "简单"
        elif level == 2:
            level_name = "中等"
        elif level == 3:
            level_name = "困难"
        else:
            level_name = str(level)
        paid = question_item["paid_only"]
        if paid:
            paid_name = "付费"
        else:
            paid_name = "免费"

        print("| {} | {} | {} | {} | [原题]({}) |  |  |  |  |".format(num, title, level_name, paid_name, url))
