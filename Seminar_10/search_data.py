import working_with_database as wwd


def search_name_in_db(name):
  collection = []
  data = wwd.open_file()
  if data != None:
    for i in data:
      if i["name"] == name:
        collection.append(i)
        return collection
  else:
    return None


def search_birthday_in_db(day):
  collection = []
  data = wwd.open_file()
  for i in data:
    if day == i["hb"]:
      collection.append(i)
  if len(collection) != 0:
    return collection
  else:
    return None


def search_class_in_db(grade):
  collection = []
  data = wwd.open_file()
  for i in data:
    if grade in i["class"]:
      collection.append(i)
  if len(collection) != 0:
    return collection
  else:
    return None


def search_status_in_db(status):
  collection = []
  data = wwd.open_file()
  for i in data:
    if status in i["status"]:
      collection.append(i)
  if len(collection) != 0:
    return collection
  else:
    return None
