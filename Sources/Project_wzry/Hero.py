from enum import Enum
import re


class Gender(str, Enum):
    UNCONFIRM = '未确认'
    MALE = '男'
    FEMALE = '女'


class Position(str, Enum):
    UNPOSITION = '未分配'
    TANK = '坦克'
    FIGHTER = '战士'
    ASSASSIN = '刺客'
    MAGE = '法师'
    MARKSMAN = '射手'
    SUPPORT = '辅助'


class Hero:
    '''
    Hero class
    '''

    name = ''
    gender = Gender.UNCONFIRM
    position = []
    price = 0
    skills = []
    maxHealth = 0
    attack = {
        "Physic": 0,
        "Magic": 0
    }
    defence = {
        "Physic": 0,
        "Magic": 0
    }

    def __init__(
        self,
        name: str,
        gender: Gender,
        position: list,
        price: int,
        skills: list,
        maxHealth: int,
        attack: list,
        defence: list
    ):
        '''
        创建一个新英雄
        @param name 英雄名
        @param gender 性别
        @param position 站位（职位）
        @param price 售价（金币）
        @param skills 技能
        @param maxHealth 最大生命值
        @param attack 攻击力，第一个值是物理、第二个是魔法
        @param defence 防御力，第一个值是物理、第二个是魔法
        '''
        self.name = name
        self.gender = gender
        self.position = position
        self.price = price
        self.skills = skills
        self.maxHealth = maxHealth
        self.attack = {
            "Physic": attack[0],
            "Magic": attack[1]
        }
        self.defence = {
            "Physic": defence[0],
            "Magic": defence[1]
        }


def input_hero_name():
    print("请输入英雄姓名")
    print("输入 ^ 回车以退出")
    hero_name = input("> ")
    return hero_name


def input_hero_gender():
    while True:
        print("请输入英雄性别【男 (M)ale / 女 (F)emale】")
        print("输入 ^ 回车以退出")
        gender = input("> ").casefold()
        if gender.startswith('^'):
            return '^'
        if gender == '男' or gender.startswith('m'):
            hero_gender = Gender.MALE
            break
        elif gender == '女' or gender.startswith('f'):
            hero_gender = Gender.FEMALE
            break
        else:
            print("输入错误，请重新输入")
    return hero_gender


def input_hero_position():
    while True:
        print("请输入英雄定位，用逗号隔开")
        print("坦克 (T)ank")
        print("战士 (W)arrior")
        print("法师 (M)age")
        print("刺客 (A)ssassin")
        print("射手 (G)Marksman")
        print("辅助 (S)upport")
        print("输入 ^ 回车以退出")
        position = input('> ')
        if position.startswith('^'):
            return '^'
        position = [word.strip().casefold() for word in re.split(r'[,，]', position)]
        hero_position = []
        for pos in position:
            if pos.startswith('t'):
                hero_position.append(Position.TANK)
            elif pos.startswith('w'):
                hero_position.append(Position.FIGHTER)
            elif pos.startswith('m'):
                hero_position.append(Position.MAGE)
            elif pos.startswith('a'):
                hero_position.append(Position.ASSASSIN)
            elif pos.startswith('g'):
                hero_position.append(Position.MARKSMAN)
            elif pos.startswith('s'):
                hero_position.append(Position.SUPPORT)
            else:
                input("其中一个或多个值有问题，请重新输入")
                continue
        break
    return hero_position


def input_hero_numeric(attr: str):
    while True:
        print(f"请输入英雄{attr}")
        print("输入 ^ 回车以退出")
        hero_price = input("> ")
        if hero_price.startswith('^'):
            return '^'
        if hero_price.isdigit():
            hero_price = int(hero_price)
        else:
            input("只支持数值输入，请重试")
            continue
        break
    return hero_price

def input_hero_skills():
    while True:
        print("请输入英雄技能，用逗号隔开")
        print("输入 ^ 回车以退出")
        hero_skills = input('> ')
        if hero_skills.startswith('^'):
            return '^'
        hero_skills = [word.strip() for word in re.split(r'[,，]', hero_skills)]
        if len(hero_skills) > 4 or len(hero_skills) < 3:
            input("技能数量不够 / 太多（最少三个，最多四个）")
            continue
        break
    return hero_skills


def create_new_hero():
    hero_name = input_hero_name()
    if hero_name.startswith('^'):
        return '^'
    hero_gender = input_hero_gender()
    if hero_gender.startswith('^'):
        return '^'
    hero_position = input_hero_position()
    if hero_position.startswith('^'):
        return '^'
    hero_price = input_hero_numeric("售价")
    if hero_price.startswith('^'):
        return '^'
    hero_skills = input_hero_skills()
    if hero_skills.startswith('^'):
        return '^'
    hero_values_verify = False
    while not hero_values_verify:
        print("请分别输入：最大生命值，物理攻击，法术攻击，物理防御，法术防御值")
        print("输入 ^ 回车以退出")
        hero_values = input('> ')
        if hero_values.startswith('^'):
            return
        hero_values = [word.strip().casefold() for word in re.split(r'[,，]', hero_values)]
        if len(hero_values) != 5:
            input("请输入五个整数型数据")
            continue
        for value in hero_values:
            if value.isdigit():
                hero_values_verify = True
            else:
                hero_values_verify = False
                break
        if not hero_values_verify:
            input("一个或多个数据不正确")
    new_hero = Hero(
        hero_name,
        hero_gender,
        hero_position,
        hero_price,
        hero_skills,
        hero_values[0],
        [hero_values[1], hero_values[2]],
        [hero_values[3], hero_values[4]]
    )
    return new_hero
