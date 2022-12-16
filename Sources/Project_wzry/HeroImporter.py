import json
import pprint
from Hero import *


def importFromFile(filePath: str):
    with open(filePath, "r", encoding="utf8") as inputFile:
        heroes = []
        heroList: list = json.load(inputFile)['root']
        for hero in heroList:
            CURRENT_HERO: dict = hero
            
            position = []
            categories = CURRENT_HERO['category'].split(',')
            for category in categories:
                if category == 'fighter':
                    position.append(Position.FIGHTER)
                elif category == 'tank':
                    position.append(Position.TANK)
                elif category == 'assassin':
                    position.append(Position.ASSASSIN)
                elif category == 'marksman':
                    position.append(Position.MARKSMAN)
                elif category == 'mage':
                    position.append(Position.MAGE)
                elif category == 'support':
                    position.append(Position.SUPPORT)

            skillList = []
            skills: list = CURRENT_HERO['skills'][1:]
            for skill in skills:
                skillList.append(skill['skill_name'])
            
            attributes: dict = CURRENT_HERO['attributes']
            currentHero = Hero(
                CURRENT_HERO['name'],
                Gender.UNCONFIRM,
                position,
                CURRENT_HERO['gold'],
                skillList,
                attributes['最大生命'],
                [attributes['物理攻击'], attributes['物理防御']],
                [attributes['法术攻击'], attributes['法术防御']]
            )
            heroes.append(currentHero.__dict__)
        with open("./Output/wzry_heroes_data.json", 'w', encoding='utf-8') as outputFile:
            json.dump(heroes, outputFile, ensure_ascii=False)

if __name__ == "__main__":
    importFromFile('./Data/wzry_hero.db.json')
