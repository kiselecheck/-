import pygame as pg


def text_helpers(screen: pg.surface.Surface):
    """Текст подсказка по управлению"""
    #Шрифт
    text_font1 = pg.font.Font(None, 30)
    text_font2 = pg.font.Font(None, 35)
    text_font3 = pg.font.Font(None, 35)
    text_font4 = pg.font.Font(None, 35)
    #Текст
    str1 = f'Esc-пауза'
    str2 = f'Управление:'
    str3 = f'Используйте стрелочки, чтобы управлять огнем'
    str4 = f'Используйте W, A, D, чтобы управлять водой'
    #Surface
    text1 = text_font1.render(str1, True, (119, 221, 119))
    text2 = text_font2.render(str2, True, (119, 221, 119))
    text3 = text_font3.render(str3, True, (255, 127, 127))
    text4 = text_font4.render(str4, True, (66, 170, 255))
    #Отрисовка
    screen.blit(text1, (5, 5))
    screen.blit(text2, (16, 650))
    screen.blit(text3, (16, 680))
    screen.blit(text4, (16, 710))


def text_start(screen: pg.surface.Surface):
    """Текст при запуске игры"""
    text_font1 = pg.font.Font(None, 50)  # шрифт
    str1 = f'Нажмите любую клавишу, чтобы начать'
    text1 = text_font1.render(str1, True, (255, 255, 255))  # текст
    screen.blit(text1, (50, 300))


def text_win(number_of_levels: int, screen: pg.surface.Surface, time_for_win: float):
    """Текст при прохождении уровня"""
    win_font = pg.font.Font(None, 60)  # шрифт
    click_font = pg.font.Font(None, 50)  # шрифт
    win_text = win_font.render('Вы прошли ' + str(number_of_levels) + ' уровень!',
                               True, (255, 255, 255))  # текст
    time_to_win_text = win_font.render('Время прохождения: ' + str(time_for_win/10) + ' с',
                               True, (255, 255, 255))  # текст
    click_text = click_font.render('Нажмите любую клавишу, ',
                                   True, (119, 221, 119))  # текст
    click_text_2 = click_font.render('чтобы перейти на следующий уровень ',
                                   True, (119, 221, 119))  # текст
    screen.blit(win_text, (170, 300))
    screen.blit(time_to_win_text, (130, 400))
    screen.blit(click_text, (170, 645))
    screen.blit(click_text_2, (55, 685))
    pg.display.flip()


def text_stopwatch(screen: pg.surface.Surface, str2: float):
    """Текст секундомера уровня"""
    text_font2 = pg.font.Font(None, 40)  # шрифт
    text2 = text_font2.render(str(str2)+' с', True, (167, 143, 255))  # текст
    screen.blit(text2, (375, 0))


def text_number_of_level(screen: pg.surface.Surface, number_of_levels: int):
    text_font1 = pg.font.Font(None, 30)  # шрифт
    str1 = f'Уровень {number_of_levels}'
    text1 = text_font1.render(str1, True, (119, 221, 119))  # текст
    screen.blit(text1, (695, 5))


def text_final_win(screen: pg.surface.Surface, time_for_all_levels: float):
    """Выводит на экран надпись в момент прохождения всей игры"""
    #Шрифты
    font_for_congratulations = pg.font.Font(None, 70)
    font_for_last_info = pg.font.Font(None, 50)
    kol_sec = time_for_all_levels/10
    #Тексты
    text_congratulations = font_for_congratulations.render('Поздравляем! Вы прошли игру!',
                                                           True, (255, 255, 255))
    win_text_last = font_for_last_info.render(f'Общее время прохождения {kol_sec} секунд',
                                              True, (255, 255, 255))
    last_text = font_for_last_info.render('Нажмите на любую клавишу,',
                                          True, (255, 255, 255))
    last_text_2 = font_for_last_info.render('чтобы закрыть игру',
                                          True, (255, 255, 255))
    screen.blit(pg.image.load("./photos/win_last_bg.jpg"), (0, 0))
    screen.blit(text_congratulations, (20, 300))
    screen.blit(win_text_last, (70, 400))
    screen.blit(last_text, (170, 645))
    screen.blit(last_text_2, (235, 685))
