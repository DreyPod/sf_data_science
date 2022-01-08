"""Компьютер загадывает целое число от 1 до 100. Программа находит случайное 
число за минимальное количество попыток."""

import numpy as np
from numpy import random

number = np.random.randint(1, 101) #компьютер загадывает число

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
        
    print(f"Программа угадала число за {count} попыток")
    return count
            


random_predict_core(number)