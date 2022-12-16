from Helper import *
from Hero import *
import random


def main_menu():
    while True:
        print_title("王者荣耀英雄管理系统")
        MENU = (
            "创建英雄",
            "删除英雄",
            "查询英雄",
            "修改英雄",
            "战斗模拟",
            "保存数据"
        )
        choice = print_menu(MENU)
        if choice == MENU.index('创建英雄'):
            create_hero()
        elif choice == MENU.index('删除英雄'):
            delete_hero()
        elif choice == MENU.index('查询英雄'):
            view_hero()
        elif choice == MENU.index('修改英雄'):
            modify_hero()
        elif choice == MENU.index('战斗模拟'):
            battle()
        elif choice == MENU.index('保存数据'):
            save_data()
        elif choice == 'x':
            # TODO: 保存英雄信息
            print_title("感谢使用本系统", False)
            print("=" * SCREEN_WIDTH)
            return
        elif choice != '' or choice.isspace():
            input("ERROR: 输入错误，请重新输入")


def create_hero():
    '''创建英雄'''
    print_title("创建英雄")
    print_title("请输入英雄信息", False)
    new_hero = create_new_hero()
    if new_hero.startswith('^'):
        print("操作取消")
        return
    heroes_list.append(new_hero.__dict__)


def delete_hero():
    '''删除英雄'''
    print_title("删除英雄")
    userInput = show_heroes_list("删除英雄")
    if userInput == 'x':
        return
    else:
        print_title("将要删除的英雄属性为")
        show_hero_info(heroes_list[userInput])
        print(f"将删除英雄，确定吗？")
        if input("[y / (n)] > ").casefold().startswith('y'):
            deleted_hero = heroes_list.pop(userInput)
            input(f"成功删除英雄{deleted_hero['name']}")
        else:
            input("操作取消！")


def view_hero():
    '''查看英雄'''
    while True:
        userInput = show_heroes_list("查看英雄")
        print_title("查看英雄")
        if userInput == 'x':
            return
        else:
            # 必然是数字
            show_hero_info(heroes_list[userInput])


def modify_hero():
    '''修改英雄'''
    print_title("修改英雄")
    userInput = show_heroes_list(function_title="修改英雄")
    if userInput == 'x':
        return
    else:
        hero = heroes_list[userInput]
        userInput = show_hero_info_mod(hero)
        if userInput == 'x':
            return
        else:
            # Prompt the user for the new value of the selected property
            if userInput == 0:
                hero["name"] = input_hero_name()
            elif userInput == 1:
                hero["gender"] = input_hero_gender()
            elif userInput == 2:
                hero["position"] = input_hero_position()
            elif userInput == 3:
                hero["price"] = input_hero_numeric("售价")
            elif userInput == 4:
                hero["skills"] = input_hero_skills()
            elif userInput == 5:
                hero["maxHealth"] = input_hero_numeric("最大生命值")
            elif userInput == 6:
                hero["attack"]["Physic"] = input_hero_numeric("物理攻击力")
            elif userInput == 7:
                hero["attack"]["Magic"] = input_hero_numeric("魔法攻击力")
            elif userInput == 8:
                hero["defence"]["Physic"] = input_hero_numeric("物理防御力")
            elif userInput == 9:
                hero["defence"]["Magic"] = input_hero_numeric("魔法防御力")

            print("英雄信息已更新。")


def battle():
    '''
    设计一个模拟对战系统，要求能够随机生成两个队伍，\n
    每个队伍 5 人，覆盖 5 种职业和 2 种性别，\n
    然后根据自定义规则进行对战\n
    （根据最大生命、攻击、防御等属性设计一个胜负规则），\n
    最后显示对战结果即可
    '''
    print_title("模拟战")
    print("生成英雄中。。。")
    # 遍历（坦克 / 战士）、法师、刺客、射手、辅助 五个职业
    # 随机抽取一个下标，找到对应英雄
    # 判断该英雄是否属于对应职业
    # 是的话，加入队列。并去掉这个数值（比如记录 ID 在另一个数组）
    # 不是的话，重复抽取 ID 的步骤
    # ========
    # 战斗开始
    # 遍历每个职业，并进行两两对战
    random_pos = [Position.TANK, Position.FIGHTER]
    choosen = []
    battle_teams = {
        "蓝方英雄": [],
        "红方英雄": []
    }
    # Generate formation
    for team in battle_teams:
        print(f'正在生成：{team}')
        battle_pos = [
            random.choice(random_pos),
            Position.MAGE,
            Position.ASSASSIN,
            Position.MARKSMAN,
            Position.SUPPORT
        ]
        for pos in battle_pos:
            while True:
                pick_hero = random.choice(heroes_list)
                if pos in pick_hero['position'] and pick_hero not in choosen:
                    battle_teams[team].append(pick_hero)
                    break
                choosen.append(pick_hero)
    print("英雄生成成功！")
    print_title("阵容预览", False)
    print("=" * SCREEN_WIDTH)
    print_teams_info(battle_teams)
    input("按 ENTER 开始战斗！")

    # ===================================================
    # 战斗开始
    # ===================================================
    while True:
        # 遍历双方，随机选择一路进行攻击（双向）
        for team in battle_teams:
            opponent = "红方英雄" if team == "蓝方英雄" else "蓝方英雄"
            for hero in battle_teams[team]:
                # 如果该英雄已经死亡，则跳过他
                if hero['maxHealth'] <= 0:
                    continue
                enemy = random.choice(battle_teams[opponent])
                dmg = sum(hero['attack'].values()) - sum(enemy['defence'].values())
                enemy['maxHealth'] -= dmg
                # 敌方英雄已阵亡
                if enemy['maxHealth'] <= 0:
                    continue
                edmg = sum(enemy['attack'].values()) - sum(hero['defence'].values())
                hero['maxHealth'] -= edmg
                print(f'{hero["name"]} 对 {enemy["name"]} 造成 {dmg} 点伤害')
                print(f'{enemy["name"]} 对 {hero["name"]} 造成 {edmg} 点伤害')
        print_teams_info(battle_teams)
        input("按 ENTER 继续")
        # 计算死亡英雄
        b_death_hero = [h for h in battle_teams["蓝方英雄"] if h["maxHealth"] < 0]
        r_death_hero = [h for h in battle_teams["红方英雄"] if h["maxHealth"] < 0]
        if len(b_death_hero) == 5:
            print_title("战斗结束")
            print_title("红方胜利", False)
            break
        elif len(r_death_hero) == 5:
            print_title("战斗结束")
            print_title("蓝方胜利", False)
            break
    print_teams_info(battle_teams)
    input("按 ENTER 返回")
    pass


def print_teams_info(battle_teams):
    for team in battle_teams:
        print(team.center(SCREEN_WIDTH - calc_full_width_char(team)))
        print('-' * SCREEN_WIDTH)
        print(f'{"Hero Name".rjust(12)} |  HP  | ATK | MTK | DEF | MDF')
        print('-' * SCREEN_WIDTH)
        for hero in battle_teams[team]:
            col1 = str(hero["name"]).rjust(12 - calc_full_width_char(hero["name"]))
            health = hero["maxHealth"] if hero["maxHealth"] > 0 else 'DEAD'
            col2 = str(health).center(4)
            col3 = str(hero["attack"]["Physic"]).center(3)
            col4 = str(hero["attack"]["Magic"]).center(3)
            col5 = str(hero["defence"]["Physic"]).center(3)
            col6 = str(hero["defence"]["Magic"]).center(3)
            print(col1 + ' | ' + col2 + ' | ' + col3 + ' | ' + col4 + ' | ' + col5 + ' | ' + col6)
        print("=" * SCREEN_WIDTH)


if __name__ == "__main__":
    load_data()
    main_menu()
