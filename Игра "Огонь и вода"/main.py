from character import Character
from Level import Level
from screen import SCREEN_WIDTH, SCREEN_HEIGHT
from Group import GroupOfSprite
from Processing import *


def create_tuple_levels() -> tuple:
    """Считывает входные файлы и создает кортеж уровней"""
    with open("./levels/level1.txt", 'r') as f1:
        l1 = f1.readlines()
        level1 = Level(l1)
    with open("./levels/level2.txt", 'r') as f2:
        l2 = f2.readlines()
        level2 = Level(l2)
    with open("./levels/level3.txt", 'r') as f3:
        l3 = f3.readlines()
        level3 = Level(l3)
    with open("./levels/level4.txt", 'r') as f4:
        l4 = f4.readlines()
        level4 = Level(l4)
    return level1, level2, level3, level4


def start_options(players: GroupOfSprite, current_level: Level, screen: pg.surface.Surface):
    """Начальные условия"""
    players.go_to_initial_position()
    players.set_level(current_level)
    current_level.draw(screen)
    players.draw(screen)
    text_start(screen)
    text_helpers(screen)
    text_stopwatch(screen, stopwatch_count(pg.time.get_ticks()))
    pg.display.flip()
    frozen_display()


def main():
    time_for_all_levels = 0
    pg.init()
    pg.display.set_caption("Огонь и вода")
    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.KEYUP])  #команды, которые мы считываем
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()  # Скорость обновления экрана
    # Создаем игроков
    player1 = Character('fire/fire.png',
                        ['fire/fire_left_1.png', 'fire/fire_left_2.png',
                         'fire/fire_left_3.png', 'fire/fire_left_4.png'],
                        ['fire/fire_right_1.png', 'fire/fire_right_2.png',
                         'fire/fire_right_3.png', 'fire/fire_right_4.png'], "fire")
    player2 = Character('water/water.png',
                        ['water/water_left_1.png', 'water/water_left_2.png',
                         'water/water_left_3.png', 'water/water_left_4.png'],
                        ['water/water_right_1.png', 'water/water_right_2.png',
                         'water/water_right_3.png', 'water/water_right_4.png'], "water")
    players = GroupOfSprite(player1, player2)
    # Устанавливаем текущий уровень
    number_of_levels = 1
    tuple_of_levels = create_tuple_levels()
    current_level = tuple_of_levels[number_of_levels-1]
    #начальные настройки
    start_options(players, current_level, screen)
    # begin_of_time_count - на каком тике начался данный уровень
    begin_of_time_count = pg.time.get_ticks()
    # Цикл будет до тех пор, пока пользователь не нажмет кнопку закрытия
    done = False
    # Основной цикл программы
    while not done:
        #keyboard_processing возвращает 0, если не было пауз, иначе: кол-во тиков в паузу
        begin_of_time_count += keyboard_processing(tuple_of_levels, number_of_levels, players, player1, player2)
        flipping(current_level, screen, number_of_levels, begin_of_time_count, players, clock)
        if players.check_win_condition():
            time_for_win = (pg.time.get_ticks() - begin_of_time_count) // 100
            players_win_level(players, number_of_levels, screen, time_for_win)
            time_for_all_levels += time_for_win
            number_of_levels += 1
            begin_of_time_count = pg.time.get_ticks()
            if check_final_win(tuple_of_levels, number_of_levels):
                done = True
            else:
                current_level = tuple_of_levels[number_of_levels - 1]
        elif players.check_lose_condition():
            players.go_to_initial_position()
            begin_of_time_count = pg.time.get_ticks()

    text_final_win(screen, time_for_all_levels)
    pg.display.flip()
    frozen_display()
    # Корректное закрытие программы
    pg.quit()


if __name__ == '__main__':
    main()
