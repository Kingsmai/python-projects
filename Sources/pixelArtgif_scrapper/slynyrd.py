from html.parser import HTMLParser
from urllib.parse import unquote
import requests

sourceUrl = "https://www.pixelgif.art/tutorials/slynyrd/images/"

with open("./Data/slynyrd.html", "r", encoding="utf8") as file:
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a' and 'item' in attrs[0]:
                url = unquote(attrs[1][1].split('/')[-1])
                response = requests.get(sourceUrl + url)
                with open(f'Output/Slynyrd/{url}.gif', 'wb') as handle:
                    handle.write(response.content)
                print(url)

        # def handle_endtag(self, tag):
        #     print("Encountered an end tag :", tag)

        # def handle_data(self, data):
        #     print("Encountered some data  :", data)

    parser = MyHTMLParser()
    parser.feed(file.read())