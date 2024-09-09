import pygame as pg
import Level
import character


class GroupOfSprite:
    """Класс, в котором некоторые методы класса character.py применяются сразу для двух объектов."""
    def __init__(self, character1: character.Character, character2: character.Character):
        self.Character1 = character1
        self.Character2 = character2

    def go_to_initial_position(self):
        """Задание начальных координат и скоростей"""
        self.Character1.go_to_initial_position()
        self.Character2.go_to_initial_position()

    def set_level(self, current_level: Level.Level):
        """Установка текущего уровня игры"""
        self.Character1.set_level(current_level)
        self.Character2.set_level(current_level)

    def check_win_condition(self) -> bool:
        """Проверка победы в уровне"""
        return self.Character1.check_win_condition() and self.Character2.check_win_condition()

    def check_lose_condition(self):
        """Проверка проигрыша уровня"""
        return self.Character1.check_lose_condition() or self.Character2.check_lose_condition()

    def update(self):
        """Обновление движения и анимации"""
        self.Character1.update()
        self.Character2.update()

    def draw(self, screen: pg.surface.Surface):
        """Рисовка персонажей на экране"""
        self.Character1.draw(screen)
        self.Character2.draw(screen)
