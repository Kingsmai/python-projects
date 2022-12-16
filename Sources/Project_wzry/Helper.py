from os import system, name
import math
import json
from textwrap import wrap

heroes_list = []
SCREEN_WIDTH = 48


def clear_scr():
    '''清屏操作'''
    if name == 'nt':
        # Windows
        system('cls')
    else:
        # MacOS or Linux
        system('clear')


def print_title(title: str, cls_scr=True):
    '''打印菜单标题'''
    # 清屏
    if cls_scr:
        clear_scr()
    length = SCREEN_WIDTH - calc_full_width_char(title)

    print((' ' + title + ' ').center(length, '='))


def print_menu(menuList: list):
    '''打印目录，并接受用户输入'''
    if (len(menuList) != 0):
        for idx, menuItem in enumerate(menuList):
            # 输出格式：
            # == 1. 选项 1           ==
            length = SCREEN_WIDTH - calc_full_width_char(menuItem)
            print(('== ' + str(idx + 1) + '. ' + menuItem).ljust(length - 3) + ' ==')
    # 最少输出 8 行
    for line in range(8 - len(menuList)):
        print("== ".ljust(SCREEN_WIDTH - 3) + " ==")
    print('== (Q)uit (E)xit. 返回上一级 / 退出系统'.ljust(SCREEN_WIDTH - 12) + ' ==')
    # 接受用户输入
    print(('== 请输入您的选择: ').ljust(SCREEN_WIDTH - 7, '='))
    userInput = input('(Input) > ')
    if userInput.isdigit():
        userInput = int(userInput) - 1
    elif userInput != '' or userInput.isspace():
        # 无视用户输入大小写，用作比较
        userInput = userInput.casefold()
        userInput = 'x' if userInput.startswith('q') or userInput.startswith('e') else userInput
    return userInput


def print_hero_info(info_str: str):
    length = SCREEN_WIDTH - calc_full_width_char(info_str)
    wrapped_text = wrap(info_str, length - 2)
    row_title = wrapped_text[0].split("：")[0] + '：'
    indent = len(row_title) + calc_full_width_char(row_title)
    for i, text in enumerate(wrapped_text):
        length = SCREEN_WIDTH - calc_full_width_char(text)
        if i > 0:
            print(('== ' + (' ' * indent) + text).ljust(length - 3) + ' ==')
        else:
            print(('== ' + text).ljust(length - 3) + ' ==')


def show_heroes_list(function_title: str):
    # 分页实现思路，参考 sql 的 LIMIT 语句
    currentPage = 0
    PAGE_SIZE = 10
    TOTAL_PAGE = math.ceil(len(heroes_list) / PAGE_SIZE) - 3
    while True:
        print_title(function_title)
        print_title("请选择英雄", False)
        hero_menu = []
        startIdx = currentPage * PAGE_SIZE
        stopIdx = min(currentPage * PAGE_SIZE + PAGE_SIZE, len(heroes_list))
        for i in range(startIdx, stopIdx):
            menu_row = [
                f'{str(i +  1).rjust(3)}. {heroes_list[i     ]["name"].ljust(12 - len(heroes_list[i     ]["name"]))}',
            ]
            if i + 10 < len(heroes_list):
                menu_row.append(
                    f'{str(i + 11).rjust(3)}. {heroes_list[i + 10]["name"].ljust(12 - len(heroes_list[i + 10]["name"]))}'
                )
            if i + 20 < len(heroes_list):
                menu_row.append(
                    f'{str(i + 21).rjust(3)}. {heroes_list[i + 20]["name"].ljust(12 - len(heroes_list[i + 20]["name"]))}'
                )
            hero_menu.append(menu_row)
        for menu_row in hero_menu:
            print(''.join(menu_row))

        if currentPage <= 0:
            print("= (.)next (q)uit")
        elif currentPage >= TOTAL_PAGE:
            print("= (,)prev (q)uit")
        else:
            print("= (,)prev (.)next (q)uit")

        choice = input('> ').casefold()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= len(heroes_list):
                return choice - 1
            else:
                input("ERROR: 错误的英雄 ID")
        elif choice.startswith(',') and currentPage > 0:
            currentPage -= 1
        elif choice.startswith('.') and currentPage < TOTAL_PAGE:
            currentPage += 1
        elif choice.startswith('q'):
            return 'x'
        elif choice != '' or choice.isspace():
            input("ERROR: 输入错误，请重新输入")


def show_hero_info(hero: dict):
    print_hero_info(f'英雄姓名：{hero["name"]}')
    print_hero_info(f'英雄性别：{hero["gender"]}')
    print_hero_info(f'英雄定位：{", ".join(hero["position"])}')
    print_hero_info(f'英雄价格：{hero["price"]}')
    print_hero_info(f'英雄技能：{", ".join(hero["skills"])}')
    print_hero_info(f'最大生命：{hero["maxHealth"]}')
    print_hero_info(f'物理攻击：{hero["attack"]["Physic"]}')
    print_hero_info(f'魔法攻击：{hero["attack"]["Magic"]}')
    print_hero_info(f'物理防御：{hero["defence"]["Physic"]}')
    print_hero_info(f'魔法防御：{hero["defence"]["Magic"]}')
    input(('== 按回车键继续: ').ljust(SCREEN_WIDTH - 6, '='))


def show_hero_info_mod(hero: dict):
    while True:
        print_title("将要修改的英雄属性为")
        print_hero_info(f'0 英雄姓名：{hero["name"]}')
        print_hero_info(f'1 英雄性别：{hero["gender"]}')
        print_hero_info(f'2 英雄定位：{", ".join(hero["position"])}')
        print_hero_info(f'3 英雄价格：{hero["price"]}')
        print_hero_info(f'4 英雄技能：{", ".join(hero["skills"])}')
        print_hero_info(f'5 最大生命：{hero["maxHealth"]}')
        print_hero_info(f'6 物理攻击：{hero["attack"]["Physic"]}')
        print_hero_info(f'7 魔法攻击：{hero["attack"]["Magic"]}')
        print_hero_info(f'8 物理防御：{hero["defence"]["Physic"]}')
        print_hero_info(f'9 魔法防御：{hero["defence"]["Magic"]}')
        print(('== 请输入需要修改的属性编号: ').ljust(SCREEN_WIDTH - 12, '='))
        print('== (Q)uit (E)xit. 返回上一级'.ljust(SCREEN_WIDTH - 8) + ' ==')
        userInput = input('> ')
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput >= 1 and userInput <= len(heroes_list):
                return userInput
            else:
                input("ERROR: 错误的编号")
        elif userInput.startswith('q') or userInput.startswith('e'):
            return 'x'
        elif userInput != '' or userInput.isspace():
            input("ERROR: 输入错误，请重新输入")


def load_data():
    '''
    从文件中读取英雄数据并保存在缓存中
    '''
    with open("./Output/wzry_heroes_data.json", "r", encoding='utf8') as heroesJson:
        heroes = json.load(heroesJson)
        for hero in heroes:
            heroes_list.append(hero)

def save_data():
    with open("./Output/wzry_heroes_data_s.json", "w", encoding='utf8') as outputJson:
        json.dump(heroes_list, outputJson, ensure_ascii=False)


def calc_full_width_char(base_string: str):
    # 一个汉字占两个字符，所以遇到每个汉字，需要对总长度 - 1
    count = 0
    for ch in base_string:
        if ch >= '\u4e00' and ch <= '\u9fa5' or ch >= '\uff00' and ch <= '\uffef':
            count += 1
    return count


if __name__ == "__main__":
    # 测试用例
    print_title("王者荣耀英雄管理系统")
    # print_title("wzryyxglxt")
    # print_menu(["选项 1", "xx 3", "option 2"])
    # print_menu([
    #     "创建英雄",
    #     "删除英雄",
    #     "查询英雄",
    #     "修改英雄",
    #     "战斗模拟"
    # ])
    print_hero_info("英雄技能：急速突进, 强力斩击, 力量觉醒·光, 力量觉醒·暗")
#     wrapped_text = wrap("英雄技能：急速突进, 强力斩击, 力量觉醒·光, 力量觉醒·暗", SCREEN_WIDTH - 26)
#     print(wrapped_text)
#     print(
#         """
# == 英雄技能：急速突进, 强力斩击, 力量觉醒·光, ==
# ==          力量觉醒·暗                       ==""")
