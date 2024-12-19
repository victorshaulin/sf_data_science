import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число методом дихотомии.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    if number == 1: # одну попытку тратим на 1
        return 1
    elif number == 100: # вторую на 100
        return 2
    elif number == 50: # третью на 50
        return 3
    count = 2 # 2, потому что продолжаем на 50
    predict = 50 # продолжим с середины
    
    # попытки угадать другие числа    
    mi = 1; ma = 100 # заводим рамку, которая постепенно будет сужаться
    while number != predict:
        count += 1
        if number > predict: # если загаданное число больше, сдвинем минимум до этого предсказания
            mi = predict
        elif number < predict: # иначе, если загаданное число меньше, то сдвинем максимум
            ma = predict

        # установим предсказание примерно посередине минимума и максимума
        predict = ((ma - mi) // 2) + mi

    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)
    