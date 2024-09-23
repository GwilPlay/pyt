# Словарь = Dict(dict): {"key1": "value1", ... "keyN": "valueN"}

import random, time
from typing import List, Any

print("<-------- Игра: версия 1 -------->")

# name = input("Введите имя:")
HERO = {
    "name": "test"
}

CHRS = {
    "Сила": random.randint(15, 45),
    "Выносливость": random.randint(15, 45)
}

MODEL_HERO = "$"
MODEL_ENEMY = "!"

HERO["Характеристики"] = CHRS
HERO["Модель"] = MODEL_HERO

MAP = ["0", "0", "0", "0", "0"]
HERO['Position'] = [0, 0]
i = 0
MAP[i] = MODEL_HERO

MAP = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
max_enemys = 3
enemys = 0
hero_counter = 0
for y in range(len(MAP)):
    for x in range(5):
        spawn = random.randint(1, 10)
        if spawn in [6, 8]:
            if enemys > max_enemys - 1 or y != 0:
                MAP[y][x] = MODEL_ENEMY
                enemys += 1

MAP[0][2] = MODEL_HERO
HERO['Position'] = [0,2]
for i in MAP:
    print(''.join(str(i)))

input("Нажмите Enter для продолжения..")

HERO["З"] = 100

inventory = {
    "Броня": 25,
    "Зелье здоровья": 1,
    "Меч": 15
}

HERO["И"] = inventory
HERO["Базовый Урон"] = 15
HERO["Удар мечом"] = HERO["Базовый Урон"] + HERO["И"]["Меч"]

ENEMY = {
    "Хп": 100,
    "Урон": 25,
    "Картошка": 15
}

ENEMY["Общ урон"] = ENEMY["Урон"] + ENEMY["Картошка"]

while True:
    max = 1000
    symb_load = '\\|/-\\|/-'
    count = 0
    length_load = len(symb_load)
    height = 5
    # for iter in range(max):
    #     time.sleep(0.001)
    #     temp = int(round(iter * 100 / 1000) // 2)
    #     if count >= length_load - 1:
    #         count = 0
    #     else:
    #         count += 1
    #     print(height * '\n', f'/{symb_load[count]} - Загрузка', height * '\n')
    move = int(input('---> Ваш ход (1 - влево , 2 - право , 3 - вниз , 4 - вверх)'))

    if move == 1:
        MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
        MAP[HERO['Position'][0]][HERO['Position'][1]-1] = MODEL_HERO
        HERO['Position'] = [HERO['Position'][0],[HERO['Position'][1]-1]]
    if move == 2:
        MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
        MAP[HERO['Position'][0]][HERO['Position'][1] + 1] = MODEL_HERO
        HERO['Position'] = [HERO['Position'][0], [HERO['Position'][1] + 1]]
    if move == 3:
        MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
        MAP[HERO['Position'][0]+1][HERO['Position'][1]] = MODEL_HERO
        HERO['Position'] = [HERO['Position'][0]+1, [HERO['Position'][1]]]
    if move == 4:
        MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
        MAP[HERO['Position'][0]-1][HERO['Position'][1] - 1] = MODEL_HERO
        HERO['Position'] = [HERO['Position'][0]-1, [HERO['Position'][1]]]

    for i in MAP:
        print(''.join(str(i)))

    input("Нажмите Enter для продолжения..")

    if random.randint(1, 6) in [1, 3, 6]:
        print("--->Обычный удар<---")
        ENEMY["Хп"] = ENEMY["Хп"] - HERO["Базовый Урон"]
        if random.randint(1, 6) in [2]:
            print(
                "         |          \n         |          \n         |          \n         |          \n---->Удар мечом<----")
            ENEMY["Хп"] = ENEMY["Хп"] - HERO["Удар мечом"]
        health_icon = "♥"
        Hero_health_bar = int(HERO["З"] // 10) * health_icon
        Enemy_health_bar = int(ENEMY["Хп"] // 10) * health_icon
        print(
            f'HEADER STATISTIC\nHERO - {Hero_health_bar}\nENEMY - {Enemy_health_bar}\nСила HERO - {HERO['Характеристики']['Сила']}\nВыносливость HERO - {HERO['Характеристики']['Выносливость']}')
        time.sleep(5)
        if ENEMY["Хп"] <= 0:
            print("---->ВЫ ПОБЕДИЛИ<----")
            time.sleep(5)
            exit(0)
        else:
            pass
    else:
        print("---->MISS<----")
        HERO["З"] = HERO['З'] + HERO["И"]["Броня"] - ENEMY["Общ урон"]
        health_icon = "♥"
        Hero_health_bar = int(HERO["З"] // 10) * health_icon
        Enemy_health_bar = int(ENEMY["Хп"] // 10) * health_icon
        print(
            f'HEADER STATISTIC\nHERO - {Hero_health_bar}\nENEMY - {Enemy_health_bar}\nСила HERO - {HERO['Характеристики']['Сила']}\nВыносливость HERO - {HERO['Характеристики']['Выносливость']}')
        time.sleep(5)
        if HERO["З"] <= 0:
            print("---->ВЫ ПРОИГРАЛИ<----")
            time.sleep(5)
            exit(0)
        else:
            pass
