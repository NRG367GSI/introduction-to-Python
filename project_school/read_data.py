def read_data():
    lst_students = []
    with open('student_repo.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_students.append(temp)
    return lst_students