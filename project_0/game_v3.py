"""Игра угадай число.
Компьютер будет сам загадывать и сам угадывать число"""

import numpy as np
def smart_random_predict(number: int = 1) -> int:
    """Устанавливаем рандомное число от 0 до 100, устанавливаем левую и правую границы поиска нужного числа.
       Меняем границы поиска в зависимости от того больше число загаданного или меньше. 
       Новое случайное число берем как среднее интервала.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    left_number = 0
    right_number = 101
    while number != predict:
        count += 1
        if number > predict:
            left_number = predict
            predict = (left_number + right_number) // 2
        elif number < predict:
            right_number = predict
            predict = (left_number + right_number) // 2
    return count


def score_game(smart_random_predict) -> int:
    """За какое количество попыток в среднем угадывается наш алгоритм (из 1000 попыток)

    Args:
        smart_random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #количество попыток сохраняется в список
    np.random.seed(1) #фиксируем сид
    random_array = np.random.randint(1,101, size = (1000)) #список чисел
    
    for number in random_array:
        count_ls.append(smart_random_predict(number))
        
    score = int(np.mean(count_ls)) #Находим среднее
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(smart_random_predict)