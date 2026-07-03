from ruamel.yaml import YAML
import os
import json

def set_version():
    with open('data/client/docs_version/version.json', 'r') as f:
        docs_version = json.load(f)['version']
    with open('data/meta.json', 'r') as f:
        product_version = json.load(f)['product_version']

    output = os.getenv('GITHUB_OUTPUT')
    with open(output, "a") as f:
        f.write(f'version={docs_version}-{product_version}\n')
        
def set_max_data():
    max_data={}
    with open("./data/tables/item_definition/character.json", "r", encoding="utf-8") as f:
        max_data["character"] = [character["id"] for character in json.load(f)]
    with open("./data/tables/item_definition/skin.json", "r", encoding="utf-8") as f:
        max_data["skin"] = [skin["id"] for skin in json.load(f)]
    with open("./data/tables/item_definition/title.json", "r", encoding="utf-8") as f:
        max_data["title"] = [title["id"] for title in json.load(f)]
    with open("./data/tables/item_definition/item.json", "r", encoding="utf-8") as f:
        max_data["item"] = [item["id"] for item in json.load(f) if item["category"] == 5]
    with open("./data/tables/item_definition/item.json", "r", encoding="utf-8") as f:
        max_data["loading_image"] = [loading_image["id"] for loading_image in json.load(f) if loading_image["category"] == 8]
    with open("./data/tables/item_definition/loading_image.json", "r", encoding="utf-8") as f:
        max_data["loading_image"] = list(set( max_data["loading_image"]+[loading_image["id"] for loading_image in json.load(f)]))
    max_data["emoji"]={}
    with open("./data/tables/character/emoji.json", "r", encoding="utf-8") as f:
        for emoji in json.load(f):
            if emoji["charid"] not in max_data["emoji"].keys():
                max_data["emoji"][emoji["charid"]] = []
            max_data["emoji"][emoji["charid"]].append(emoji["sub_id"])
    with open("./data/tables/spot/rewards.json", "r", encoding="utf-8") as f:
        max_data["endings"] = [endings["id"] for endings in json.load(f)]

    with open('max_data.json','w', encoding="utf-8") as f:
        json.dump({"mod": max_data}, f, separators=(',', ':'),indent =None)

    with open('max_data.yaml','w', encoding="utf-8") as f:
        yaml = YAML()
        yaml.dump({"mod": max_data}, f)


def main():
    set_version()
    set_max_data()

if __name__ == '__main__':
    main()
