from datetime import datetime as dt


def write(designation,data):
    time = dt.now().strftime('Дата: %d.%m Время: %H:%M')
    with open("log_file.csv", "a") as log:
        log.write(f'{time} {designation}: {data}\n')

def read():
    try:
        with open("log_file.csv", "r") as log:
            history_log = log.read()
            return history_log
    except FileNotFoundError:
        return None