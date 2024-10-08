import pygame as pg
import Level


class Character(pg.sprite.Sprite):
    """Класс, в котором создаются Персонажи"""
    def __init__(self, idle_image: str, move_images_left: list[str], move_images_right: list[str], name: str):
        """Задает начальное изображение персонажей, скорость, анимацию."""
        super().__init__()
        # Изображения
        self.level = None
        self.idle_image = pg.image.load(idle_image)  #фото для стоячего положения
        self.move_images_left = [pg.image.load(img) for img in move_images_left]  #фото для бега влево
        self.move_images_right = [pg.image.load(img) for img in move_images_right]  # фото для бега вправо
        self.image = self.idle_image  #image - отвечает за рисунок объекта на экране, изначально - стоячее положение
        self.name = name
        self.rect = self.image.get_rect()  # задаем высоту и ширину модельки персонажа по иконке
        self.rect.width = 30  #ширина
        # Задаем начальную скорость игрока
        self.movespeed_x = 0
        self.movespeed_y = 0
        # Дополнительные переменные для анимации
        self.counter_move_frame = 0  #Какая из иконок на экране(номер)
        self.last_update = pg.time.get_ticks()  #Время последнего обновления
        self.frame_rate = 100  # Скорость смены кадров анимации

    def go_to_initial_position(self):
        """Задание начальных координат и скоростей"""
        self.rect.x = 40
        self.rect.y = 595
        self.movespeed_x = 0
        self.movespeed_y = 0

    def set_level(self, level: Level.Level):
        """Установка текущего уровня игры"""
        self.level = level

    def check_lose_condition(self):
        """Проверка проигрыша уровня"""
        water_blocks = pg.sprite.spritecollideany(self, self.level.water_block_list)
        fire_blocks = pg.sprite.spritecollideany(self, self.level.fire_block_list)
        dead_blocks = pg.sprite.spritecollideany(self, self.level.dead_block_list)
        return (water_blocks and self.name == "fire") or (fire_blocks and self.name == "water") or dead_blocks

    def check_win_condition(self) -> bool:
        """Проверка победы в уровне"""
        return pg.sprite.spritecollideany(self, self.level.win_list)

    def jump(self):
        """ Нам нужно проверять здесь, контактируем ли мы с чем-либо, чтобы нельзя было прыгать в воздухе.
        Опускаемся на 1 единицу, проверяем соприкосновение и далее поднимаемся обратно.
        """
        self.rect.y += 1
        platform_hit_list = pg.sprite.spritecollideany(self, self.level.platform_list)
        self.rect.y -= 1
        if platform_hit_list:  #Если под нами есть земля, прыгаем
            self.movespeed_y = -12

    def go_left(self):
        self.movespeed_x = -8

    def go_right(self):
        self.movespeed_x = 8

    def stop(self):
        #Вызываем этот метод, когда не нажимаем на клавиши
        self.movespeed_x = 0

    def vertical_move(self):
        """Расчет вертикального движения"""
        self.movespeed_y += 1  # Гравитация тянет вниз на 1 единицу
        self.rect.y += self.movespeed_y
        block_hit = pg.sprite.spritecollideany(self, self.level.platform_list)  # Следим ударяем ли мы платформу
        if block_hit:
            # Устанавливаем нашу позицию на основе верхней / нижней части объекта,
            # на который мы попали
            if self.movespeed_y > 0:
                self.rect.bottom = block_hit.rect.top
            elif self.movespeed_y < 0:
                self.rect.top = block_hit.rect.bottom
            self.movespeed_y = 0

    def horizontal_move(self):
        """Расчет горизонтального движения"""
        self.rect.x += self.movespeed_x  # Передвигаемся по оси x
        block_hit = pg.sprite.spritecollideany(self, self.level.platform_list)
        if block_hit:
            #Если мы идем вправо, то наша правая сторона = левая сторона стены
            #Если мы идем влево, то наша левая сторона = правая сторона стены
            if self.movespeed_x > 0:
                self.rect.right = block_hit.rect.left
            elif self.movespeed_x < 0:

                self.rect.left = block_hit.rect.right

    def animate(self):
        """Расчет анимации движения """
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.counter_move_frame = (self.counter_move_frame + 1) % len(self.move_images_left)
            if self.movespeed_x > 0:
                self.image = self.move_images_right[self.counter_move_frame]
            elif self.movespeed_x < 0:
                self.image = self.move_images_left[self.counter_move_frame]
            else:  # Если игрок стоит
                self.image = self.idle_image

    def update(self):
        """Обновление движения и анимации"""
        self.vertical_move()
        self.horizontal_move()
        self.animate()

    def draw(self, screen: pg.surface.Surface):
        """Рисовка персонажа на экране"""
        screen.blit(self.image, self.rect)
