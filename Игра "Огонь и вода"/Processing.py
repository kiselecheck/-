from Texts import *


def frozen_display():
    """Картинка не меняется, пока не нажмем на любую кнопку"""
    end_key = True
    while end_key:  # закрытие программы после нажатия любой кнопки
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit(0)
            if i.type == pg.KEYDOWN:
                end_key = False


def stopwatch_count(begin_of_time_count: float):
    """Секундомер"""
    cur_time = pg.time.get_ticks() - begin_of_time_count
    str2 = cur_time // 100 / 10
    return str2


def pause() -> float:
    a = pg.time.get_ticks()
    frozen_display()
    return pg.time.get_ticks() - a


def keyboard_processing(tuple_of_levels, number_of_levels, players, player1, player2) -> float:
    """Обработка всех возможных действий с пользователем"""
    current_level = tuple_of_levels[number_of_levels - 1]
    players.set_level(current_level)
    # Отслеживание действий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
        # Если нажали на стрелки клавиатуры, то двигаем объект
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:  # 1 игрок
                player1.go_left()
            if event.key == pg.K_RIGHT:
                player1.go_right()
            if event.key == pg.K_UP:
                player1.jump()
            if event.key == pg.K_a:  # 2 игрок
                player2.go_left()
            if event.key == pg.K_d:
                player2.go_right()
            if event.key == pg.K_w:
                player2.jump()
            if event.key == pg.K_ESCAPE:
                return pause()
        elif event.type == pg.KEYUP:  # Отпустили клавиши
            if event.key == pg.K_LEFT and player1.movespeed_x < 0:
                player1.stop()
            if event.key == pg.K_RIGHT and player1.movespeed_x > 0:
                player1.stop()
            if event.key == pg.K_a and player2.movespeed_x < 0:
                player2.stop()
            if event.key == pg.K_d and player2.movespeed_x > 0:
                player2.stop()
    return 0


def drawing(current_level, screen, number_of_levels, begin_of_time_count: float, players):
    """Отрисовка"""
    current_level.draw(screen)
    players.draw(screen)
    sec = stopwatch_count(begin_of_time_count)
    text_stopwatch(screen, sec)
    text_number_of_level(screen, number_of_levels)
    text_helpers(screen)


def flipping(current_level, screen, number_of_levels, begin_of_time_count, players, clock):
    """Обновление"""
    players.update()
    drawing(current_level, screen, number_of_levels, begin_of_time_count, players)
    clock.tick(30)  # Устанавливаем количество фреймов
    pg.display.flip()  # Обновляем экран после рисования объектов


def check_final_win(tuple_levels: tuple[int], number_of_levels: int) -> bool:
    """Проверяет условие прохождения игры"""
    return number_of_levels > len(tuple_levels)


def players_win_level(players, number_of_levels, screen, time_for_win):
    """Скрипт при победе уровня"""
    players.go_to_initial_position()
    bg_win = pg.image.load('./photos/bg_win.png')
    screen.blit(bg_win, (0, 0))
    text_win(number_of_levels, screen, time_for_win)
    frozen_display()
