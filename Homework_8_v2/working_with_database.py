import json
def open_file():
    try:
        with open("BD.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None


def save():
    bd = []
    with open('BD.json', 'w', encoding = 'utf-8') as saves:
		    saves.write(json.dumps(bd, ensure_ascii=False))


def add_in_file(text):
    try:
        with open("BD.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        save()
        with open("BD.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    data.append(text)
    with open("BD.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

def deleting(sur_name, name):
    with open("BD.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for i in range(len(data)):
        if data[i]["surname"] == sur_name and data[i]["name"] == name:
            data.pop(i)
            with open("BD.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False)
        return None
    
    




