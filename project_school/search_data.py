import working_with_database as wwd
def search_name(sur_name, name):
    data = wwd.open_file()
    if data != None: #проверяем если по чему итерироваться, если нет то возращаем что ничего нет
        for i in data:
            if i["surname"] == sur_name and i["name"] == name:
                return i
    return None

def search_birthday(day):
    data = wwd.open_file()
    for i in data:
        if day in i["hb"]:
            return i
        else:
            return None

def search_class(day):
    data = wwd.open_file()
    for i in data:
        if day in i["class"]:
            return i
        else:
            return None


def search_status(status):
    data = wwd.open_file()
    for i in data:
        if status in i["status"]:
            return i
        else:
            return None

#print(search_status("5"))


