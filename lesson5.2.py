# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Первому надо взять 20, а дальше по формуле - *все конфеты* % (*максимум конфет за один ход* + 1)
# В итоге в конце остается 29 конфет и ход соперника, сколько бы он не взял(кроме нуля, что в программе предусмотренно, вроде), выйграет первый
# Подумайте как наделить бота ""интеллектом""? - ну, типо реплики добавил, ну, а как еще я не знаю 


from random import *
import os


welcome_text = ('Доброго врмени суток, мой дорогой гость.\n'
                'Если ты сюда пришел, то значит решил сыграть в нашу "сладкую" игру.\n'
                'Для начала я расскажу правила:\n'
                'Будет ровно 2021 конфета, вы будете ходить по очереди,\n'
                'за один раз можно взять от 1-й до 28-и конфет.\n'
                'Все конфеты заберет тот, кто сделает последний ход.\n'
                'Начнем же нашу игру :)')
print(welcome_text)

modes_text = int(input('Выберите режим:\n'
              '1 - Игра друг против друга.\n'               
              '2 - Игра против бота.\n'))

message = ['хватай конфетки', 'пора бы уже решить сколько, бери', 'бери больше', 'подумай хорошенько',
           'бери быстрее', 'смотри, чтобы в карманы поместилось', 'больше лучше, но так ли это']

message_me = ['опа, моя очередь', 'кто же выйграет?)', 'победа за мной', 'хм, сколько же взять',
           'так, ну возьму столько', 'вот выйграю и объемся, хаха', 'сколько бы в этот раз взять?']

if modes_text == 1:
    def pvp():
        candies_total = 2021
        max_take = 28
        count = 0
        player_1 = input('Как тебя зовут?: ')
        player_2 = input('А твоего соперника?: ') 

        print(f'\nНу чтож {player_1} и {player_2} да начнется игра!')
        print('А кто будет ходить первый первый, определит рандом)')

        a = randint(1, 2)
        if a == 1:
            lucky = player_1
            loser = player_2
            print(f'\nНачинает {lucky}, удачи!!')
        else:
            lucky = player_2
            loser = player_1
            print(f'\nНачинает {lucky}, удачи!!')

        while candies_total > 0:
            if count == 0:
                step = int(input(f'\n{choice(message)}, {lucky}: '))
                if step > max_take or step > candies_total:
                    while step > 28:
                        step = int(input(f'Так не пойдет {lucky}, играй по правилам, возьми еще раз: '))
                if step <= 0:
                    while step <= 0:
                        step = int(input(f'Так не пойдет {lucky}, играй по правилам, возьми еще раз: '))
                candies_total = candies_total - step
            if candies_total > 0:
                count = 1
                print(f'Осталось еще {candies_total} конфет')
            else:
                print('Конфеты кончились, мои дорогие игроки')

            if count == 1:
                step = int(input(f'\n{choice(message)}, {loser}: '))
                if step > max_take or step > candies_total:
                    while step > max_take or step > candies_total:
                        step = int(input(f'Так не пойдет {loser}, играй по правилам, возьми еще раз: '))
                if step <= 0:
                    while step <= 0:
                        step = int(input(f'Так не пойдет {loser}, играй по правилам, возьми еще раз: '))
                candies_total = candies_total - step
            if candies_total > 0:
                count = 0
                print(f'Осталось еще {candies_total} конфет')
            else:
                print('\nКонец игры\n'
                      'Приходите еще)')

        if count == 1:
            print(f'И наш победитель - это {loser}')
        if count == 0:
            print(f'И наш победитель - это {lucky}')
            
            
    pvp()

if modes_text == 2:
    def pvb():
        candies_total = 2021
        max_take = 28
        count = 0
        player_1 = input('Как тебя зовут?: ')
        player_2 = 'Компьютер'

        print(f'\nНу чтож, да начнется игра!')

        a = randint(1, 1)
        if a == 1:
            lucky = player_2
            loser = player_1
            print(f'\nНачину, пожалуй, Великий Я')
        else:
            lucky = player_2
            loser = player_1
            print(f'\nНачину, пожалуй, Великий Я')

        while candies_total > 0:
            if count == 0:
                print(f'\n{choice(message_me)}, {lucky}: ')
                if candies_total < 29:
                    step = candies_total
                else:
                    step = candies_total % (max_take+1)
                    if step == 0:
                        step = max_take
                print(step)
                candies_total = candies_total - step
            if candies_total > 0:
                count = 1
                print(f'Осталось еще {candies_total} конфет')
            else:
                print('Конфеты кончились')

            if count == 1:
                step = int(input(f'\n{choice(message)}, {loser}: '))
                if step > max_take or step > candies_total:
                    while step > 28 or step > candies_total:
                        step = int(input(f'Так не пойдет {loser}, играй по правилам, возьми еще раз: '))
                if step <= 0:
                    while step <= 0:
                        step = int(input(f'Так не пойдет {loser}, играй по правилам, возьми еще раз: '))
                candies_total = candies_total - step
            if candies_total > 0:
                count = 0
                print(f'Осталось еще {candies_total} конфет')
            else:
                print('\nКонец игры\n'
                      'Приходите еще)')

        if count == 1:
            print(f'И наш победитель - это {loser}')
        if count == 0:
            print(f'И наш победитель - это Я:)')

    pvb()