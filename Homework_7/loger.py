from datetime import datetime as dt


def write(data):
    processed_data = data.split('=')
    time = dt.now().strftime('Дата: %d.%m Время: %H:%M')
    with open("log_file.csv", "a") as log:
        log.write(f'{time} Входные данные: {processed_data[0]} Ответ: {processed_data[1]}\n')

def read():
    with open("log_file.csv", "r") as log:
        print(log.read())