import working_with_database as wwd
import search_data as sd
import gui_input_output as gio


def add_data():
    full_name = gio.input_name()
    students = {}
    if sd.search_name(full_name[0].capitalize(), full_name[1].capitalize()) == None:
        students['surname'] = full_name[0].capitalize()
        students['name'] = full_name[1].capitalize()
    
        students['hb'] = gio.input_birthday()
        students['class'] = gio.input_clas()
        students['status'] = gio.input_performance()
        wwd.add_in_file(students)
        return students
    else:
        return None





