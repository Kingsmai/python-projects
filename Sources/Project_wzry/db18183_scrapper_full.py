import json
import requests
from bs4 import BeautifulSoup

HERO_INFO_URL = "http://db.18183.com/wzry/hero/{}.html"

# 爬到极致：
# - 背景故事
# - 基础属性
# - 技能介绍

if __name__ == "__main__":
    with open("./Data/db18183.hero.json") as heroJsonFile:
        root = {"root": []}
        heroJson: dict = json.load(heroJsonFile)
        for idx, heroCode in enumerate(heroJson):
            print(f"{idx} / {len(heroJson)}: [{heroCode}] Proccessing...")
            heroInfo = heroJson[heroCode]

            webpage = requests.get(HERO_INFO_URL.format(heroInfo['hero_id']))
            webpage.encoding = webpage.apparent_encoding
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # 背景故事
            storyParagraph = soup.select_one("body > div.main > div > div.section.hero-details-box.mod-bg.clearfix > div.hero-otherinfo-box.mod-bg.fr > div.otherinfo-cont > div:nth-child(4) > div")
            heroInfo['story'] = storyParagraph.text

            # 角色属性
            heroAttributes = soup.select("body > div.main > div > div.section.hero-details-box.mod-bg.clearfix > div.hero-otherinfo-box.mod-bg.fr > div.otherinfo-cont > div:nth-child(5) > div > ul > li")
            attrs = {}
            for attribute in heroAttributes:
                attributeKP = attribute.text.split("：")
                attrs[attributeKP[0]] = attributeKP[1].strip()
            heroInfo['attributes'] = attrs

            # 技能
            skills = []
            skillContents = soup.select("#hero_skill > div.skill-introduce-box.mod-bg > div.bd > div.skill-cont > div")
            for skillContentHtml in skillContents:
                skillName = skillContentHtml.select_one("div.skill-contitem > div > span:nth-child(1)").text
                skillType = skillContentHtml.select_one("div.skill-contitem > div > span:nth-child(2)").text
                skillIntro = skillContentHtml.select_one("div.skill-contitem > p").text
                skills.append({
                    "skill_name": skillName,
                    "skill_type": skillType,
                    "skill_intro": skillIntro.strip()
                })
            heroInfo['skills'] = skills

            root["root"].append(heroInfo)

        with open("./Output/wzry_hero.db.json", "w", encoding='utf8') as outputFile:
            json.dump(root, outputFile, ensure_ascii=False)
