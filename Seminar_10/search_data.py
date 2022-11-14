import working_with_database as wwd


def search_name_in_db(name):
  collection = []
  data = wwd.open_file()
  if data != None:
    for i in data:
      if i["name"] == name:
        collection.append(i)
        sum = ""
        result = ""
        for i in collection:
          for j in i:
            if len(i[j]) < 18:
              sum += str(str(i[j])) + str(" " * int((18 - len(str(i[j])))))
          result += sum + "\n"
          sum = ""
    return result
  else:
    return 'Такой ученик не найден'


def search_birthday_in_db(day):
  collection = []
  data = wwd.open_file()
  for i in data:
    if day == i["hb"]:
      collection.append(i)
  if len(collection) != 0:
    sum = ""
    result = ""
    for i in collection:
      for j in i:
        if len(i[j]) < 18:
          sum += str(str(i[j])) + str(" " * int((18 - len(str(i[j])))))
      result += sum + "\n"
      sum = ""
    return result
  else:
    return 'По такой дате рождения никто не найден'


def search_class_in_db(grade):
  collection = []
  data = wwd.open_file()
  for i in data:
    if grade in i["class"]:
      collection.append(i)
  if len(collection) != 0:
    sum = ""
    result = ""
    for i in collection:
      for j in i:
        if len(i[j]) < 18:
          sum += str(str(i[j])) + str(" " * int((18 - len(str(i[j])))))
      result += sum + "\n"
      sum = ""
    return result
  else:
    return 'Такого класса нет'


def search_status_in_db(status):
  collection = []
  data = wwd.open_file()
  for i in data:
    if status in i["status"]:
      collection.append(i)
  if len(collection) != 0:
    sum = ""
    result = ""
    for i in collection:
      for j in i:
        if len(i[j]) < 18:
          sum += str(str(i[j])) + str(" " * int((18 - len(str(i[j])))))
      result += sum + "\n"
      sum = ""
    return result
  else:
    return 'С такой успеваемостью никто не найден'
