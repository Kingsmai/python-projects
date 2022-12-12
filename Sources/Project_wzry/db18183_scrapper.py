import json
import requests
from bs4 import BeautifulSoup

HERO_INFO_URL = "http://db.18183.com/wzry/hero/{}.html"

if __name__ == "__main__":
    with open("./Data/db18183.hero.json") as heroJsonFile:
        heroInfo = {
            'hero_id': '9538',
            'name': '李白',
            'nickname': '青莲剑仙',
            'category': 'fighter,assassin',
            'icon': 'https://img.18183.com/uploads/allimg/191025/266-1910251Q147.jpg',
            'gold': '18888',
            'diamond': '0',
            'ticket': '688',
            'tag': '近战,物理',
            'ability_hp': '3',
            'ability_attack': '6',
            'ability_skill': '8',
            'ability_diff': '6'
        }

        heroData = {
            "name": "",
            "position": [],
            "gold": 0,
            "skills": [],
            "baseHealth": 0,
            "attack": {
                "physic": 0,
                "magic": 0
            },
            "defence": {
                "physic": 0,
                "magic": 0
            }
        }
        
        heroData["name"] = heroInfo['name']
        heroData["position"] = heroInfo['category'].split(',')
        heroData["gold"] = heroInfo['gold']

        webpage = requests.get(HERO_INFO_URL.format(heroInfo['hero_id']))
        webpage.encoding = webpage.apparent_encoding
        soup = BeautifulSoup(webpage.text, 'html.parser')
        # 跳过被动
        skillContents = soup.select("#hero_skill > div.skill-introduce-box.mod-bg > div.bd > div.skill-cont > div")[1:]
        for skillContentHtml in skillContents:
            skillName = skillContentHtml.select_one("div.skill-contitem > div > span:nth-child(1)")
            heroData['skills'].append(skillName.text)
        # 角色属性
        heroAttributes = soup.select("body > div.main > div > div.section.hero-details-box.mod-bg.clearfix > div.hero-otherinfo-box.mod-bg.fr > div.otherinfo-cont > div:nth-child(5) > div > ul > li")
        heroData["baseHealth"] = heroAttributes[0].text.split("：")[-1]
        heroData["attack"]["physic"] = heroAttributes[2].text.split("：")[-1]
        heroData["attack"]["magic"] = heroAttributes[3].text.split("：")[-1]
        heroData["defence"]["physic"] = heroAttributes[4].text.split("：")[-1]
        heroData["defence"]["magic"] = heroAttributes[6].text.split("：")[-1]

        print(heroData)
        # heroJson: dict = json.load(heroJsonFile)
        # for heroCode in heroJson:
        #     heroInfo = heroJson[heroCode]
        #     print(heroInfo)
