import working_with_database as wwd


def list_file():  # Список всех учеников
  if wwd.open_file() != None:
    lin = wwd.open_file()
    sum = ""
    result = ""
    for i in lin:
      for j in i:
        if len(i[j]) < 18:
          sum += str(str(i[j])) + str(" " * int((18 - len(str(i[j])))))
      result += sum + "\n"
      sum = ""
    return result
  else:
    return 'Пока записей нет'
