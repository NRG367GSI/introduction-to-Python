import working_with_database as wwd
def search_name(sur_name, name):
    collection = []
    data = wwd.open_file()
    if data != None:
        for i in data:
            if i["surname"] == sur_name and i["name"] == name: #sur_name in i['surname'] and name in i["name"]:#
                collection.append(i)
                print(collection)
        return collection
    else:
        return None
            

def search_birthday(day):
    collection = []
    data = wwd.open_file()
    for i in data:
        if day == i["hb"]:
            collection.append(i)
    if len(collection) != 0:
        return collection
    else:
        return None
    
        


def search_class(grade):
    collection = []
    data = wwd.open_file()
    for i in data:
        if grade in i["class"]:
            collection.append(i)
    if len(collection) != 0:
        return collection
    else:
        return None


def search_status(status):
    collection = []
    data = wwd.open_file()
    for i in data:
        if status in i["status"]:
            collection.append(i)
    if len(collection) != 0:
        return collection
    else:
        return None



