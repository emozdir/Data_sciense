"""Игра угадай число.
Компьютер будет сам загадывать и сам угадывать число"""

import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно укадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем угадывается наш алгоритм (из 1000 попыток)

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #количество попыток сохраняется в список
    np.random.seed(1) #фиксируем сид
    random_array = np.random.randint(1,101, size = (1000)) #список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #Находим среднее
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)