import working_with_database as wwd
import search_data as sd
import loger as lg


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


def name_search():
  # arr = []
  full_name = gio.input_name()
  if full_name == None:
    return None
  else:
    surname = full_name[0]
    name = full_name[1]
    quesion = sd.search_name(surname, name)
    if quesion == None:
      return gio.none_output()
    else:
      return str(gio.output(quesion))


def birthdey_search():
  birthdey = gio.input_birthday()
  search = sd.search_birthday(birthdey)
  if search != None:
    return str(gio.output(search))
  else:
    return gio.none_output()


def grade_search():
  grade = gio.input_clas()
  search = sd.search_class(grade[0])
  if search != None:
    return str(gio.output(search))
  else:
    return gio.none_output()


def performance_serch():
  perf = gio.input_performance()
  search = sd.search_status(perf)
  if search != None:
    return str(gio.output(search))
  else:
    return gio.none_output()


def add_record():
  add = ui.add_data()
  if add != None:
    lg.write('Добавлен', add)
    return gio.addad()
  else:
    return gio.exist()


def deleted():
  name = gio.input_name()
  oper = wwd.deleting(name[0], name[1])
  if oper != None:
    lg.write('Удален', oper)
    return gio.del_print()
  else:
    return gio.none_output()


def read_log():
  if lg.read() != None:
    gio.output(lg.read())
  else:
    gio.none_output()
