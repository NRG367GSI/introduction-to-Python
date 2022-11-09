import json
def open_file():
    try:
        with open("BD.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None


def save():
    bd = [{"surname": "Фамилия", "name": "Имя", "hb": ["Дата рождния"], "class": ["Класс"], "status": "Оценки"}]
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

def deleting(surname, name):
    exsapel = []
    with open("BD.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
    for i in data:
        
        if surname in i["surname"]  and name in i["name"]:
            print(i["surname"])
            exsapel.append(i)
            data.remove(i)
            with open("BD.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False)
    if len(exsapel) != 0:
        return exsapel
    else:
        return None

        
    
    




