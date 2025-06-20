import pygame as pg
from settings import *
import os

# الحصول على المسار الحالي للملف
#current_dir = os.path.dirname('project1')


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()
        self.sky_image = self.get_texture(MAIN_SKY_IMAGE, (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.ground_image = self.get_texture(MAIN_GROUND_IMAGE, (WIDTH, HALF_HEIGHT))
        self.ground_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()


    def draw_ground(self):
        self.ground_offset = (self.ground_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.ground_image, (-self.ground_offset, HEIGHT - self.ground_image.get_height()))
        self.screen.blit(self.ground_image, (-self.ground_offset + WIDTH, HEIGHT - self.ground_image.get_height()))


    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))
        self.draw_ground()
        


    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.object_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res= (TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_texture(self):
        return {
            1 : self.get_texture('resources/game_texture/1.jpg'),
            2 : self.get_texture('resources/game_texture/2.jpg'),
            3 : self.get_texture('resources/game_texture/3.jpg'),
            4 : self.get_texture('resources/game_texture/4.jpg'),
            5 : self.get_texture('resources/game_texture/5.jpg'),
            6 : self.get_texture('resources/game_texture/6.jpg'),
            7 : self.get_texture('resources/game_texture/7.jpg'),
            8 : self.get_texture('resources/game_texture/8.jpg'),
            9 : self.get_texture('resources/game_texture/9.jpg'),

        }























