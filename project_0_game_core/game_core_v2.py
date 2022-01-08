"""Компьютер загадывает целое число от 1 до 100. Программа находит случайное 
число за минимальное количество попыток."""

import numpy as np
from numpy import random


def random_predict_core(number: int=1) -> int:
    """Сначала устанавливаем любое random число. Потом в зависимости
    от того, больше это random число или меньше, уменьшаем отрезок поиска.
    Продолжаем уменьшать, пока компьютер не угадает число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 1 # количество попыток угадать число
    limit_a = 1 # нижняя граница поиска
    limit_b = 101 # верхняя граница поиска
    predict = np.random.randint(limit_a, limit_b)
    
    while predict != number:
        count += 1
        if predict < number:
            limit_a = predict
            predict = np.random.randint(limit_a, limit_b)
            
        elif predict > number:
            limit_b = predict
            predict = np.random.randint(limit_a, limit_b)
    
    return count
        
    


def score_game(random_predict_core) -> int:
    """Функция определяет среднее количество попыток, 
    за которое программа угадывает 1000 случайных random чисел
    от 1 до 100.

    Args:
        random_predict_core ([type]): проверяемая программа

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #инициируем генерацию случайных чисел
    random_array = np.random.randint(1, 101, size = (1000)) #список 1000 случайных чисел
    
    for number in random_array:
        count_ls.append(random_predict_core(number))
        
    score = int(np.mean(count_ls))
    print(f'Программа угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":

#RUN
score_game(random_predict_core)
        
    
            