# Проект FitLife - MVP версия 1.0


import os

ML_IN_L = 1000
PEP_STR_LEN = 79


def clear_console():
    """Функция очищения консоли"""
    # 'nt' если Windows, в остальных случаях *NIX
    os.system('cls' if os.name == 'nt' else 'clear')


def print_head():
    """Функция печати заголовка"""
    project_name = 'FITLIFE'
    len_project_name = len(project_name)
    mid_str_symbol_len = (PEP_STR_LEN - len_project_name) // 2 - 1
    print('*' * PEP_STR_LEN)
    print('*' * mid_str_symbol_len, end=' ')
    print(project_name, end=' ')
    print('*' * mid_str_symbol_len)
    print('*' * PEP_STR_LEN)


def enter_name():
    """Функция ввода имени"""
    while True:
        user_name = input('Как Вас зовут? ').strip().title()
        if user_name:
            break
        print('Имя должно содержать символы!')
    print('Рад приветствовать,', user_name, end='! ')
    return user_name


def enter_age():
    """Функция ввода возраста"""
    while True:
        try:
            print('Сколько вам полных лет?', end=' ')
            user_age = int(input('(Пример: 32): '))
            if 6 <= user_age <= 110:
                break
            else:
                print('Введите реальный возраст (от 6 до 110)!')
        except ValueError:
            print('Ошибка формата ввода данных')
    return user_age


def enter_weight():
    """Функция ввода веса"""
    while True:
        try:
            print('Какой ваш вес в килограммах?', end=' ')
            user_weight = float(input('(Пример: 79.4 или 85): '))
            if 20 <= user_weight <= 200:
                break
            else:
                print('Введите реальный вес (от 20 до 200)!')
        except ValueError:
            print('Ошибка формата ввода данных')
    return user_weight


def enter_height():
    """Функция ввода роста"""
    while True:
        try:
            print('Укажите Ваш рост в метрах.', end=' ')
            user_height = float(input('(Пример: 1.81 или 2): '))
            if 0.5 <= user_height <= 2.5:
                break
            else:
                print('Введите реальный рост (от 0.5 до 2.5 метров)!')
        except ValueError:
            print('Ошибка формата ввода данных')
    return user_height


def hello_user():
    """Функция приветствует пользователя, получает от него данные"""
    # Приветствуем пользователя и спрашиваем его имя. Из полученного ответа
    # удаляем пробелы в начале и в конце, первые буквы слов делаем заглавными.
    # Записываем резельтат в переменную user_name
    print('Привет! Я бот Fitlife. Давайте знакомиться!')
    user_name = enter_name()
    # Выводим на экран общую информацию о возможностях нашей программы
    print('Я помогу Вам высчитать индекс массы тела')
    print('и дам рекомендации по суточной норме воды.')
    print('Для этого мне потребуются от вас некоторые данные.')
    print('Прошу вводить их в указанных единицах для корректности подсчётов.')
    # Считываем введённые данные о возрасте, весе, росте, приводим их
    # к нужному типу и присваиваем значение переменным
    user_age = enter_age()
    user_weight = enter_weight()
    user_height = enter_height()
    return user_name, user_age, user_weight, user_height


def calculate_bmi(weight, height):
    """Функция для подсчёта индекса массы тела"""
    return round((weight / height ** 2), 1)


def calculate_daily_water(weight):
    """Функция для подсчёта нормы воды в день"""
    ML_PER_KG = 30
    return weight * ML_PER_KG


def calc_print_result(user_name, user_age, user_weight, user_height):
    """Функция выводит на экран вычисленные значения"""
    print('=' * PEP_STR_LEN)
    print(f'{user_name}, возраст: {user_age}, ', end='')
    # Выводим на экран BMI
    bmi = round(calculate_bmi(user_weight, user_height), 1)
    print(f'Ваш индекс массы тела (BMI): {bmi}')
    # Выводим на экран норму воды в день
    daily_water = round((calculate_daily_water(user_weight) / ML_IN_L), 1)
    print(f'Норма потребления воды в день: {daily_water} л')


# очищаем консоль перед выполнением программы
clear_console()
# Рисуем шапку
print_head()
# Запрашиваем данные у пользователя, преобразуем их, записываем результат
name, age, weight, height = hello_user()
# Считаем и выводим нужные параметры
calc_print_result(name, age, weight, height)
