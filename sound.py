import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'pain1.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'death_scream.mp3')
        self.npc_shot = pg.mixer.Sound(self.path + 'enemey_shotgun.mp3')
        self.player_pain = pg.mixer.Sound(self.path + 'bruh.mp3')
        self.theme = pg.mixer.Sound(self.path + 'doom.mp3')
        self.shotgun.set_volume(0.1)




















