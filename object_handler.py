from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprite/npc/'
        self.static_sprite_path = 'resources/sprites/static/'
        self.anim_sprite_path = 'resources/sprites/animated/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        
        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.15, 1.15)))
        add_sprite(AnimatedSprite(game, pos=(7.25, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(7.25, 6.25)))
        add_sprite(AnimatedSprite(game, pos=(6.75, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(6.75, 5.75)))
        add_sprite(AnimatedSprite(game, pos=(7.25, 1.05)))
        add_sprite(AnimatedSprite(game, pos=(7.25, 1.95)))
        add_sprite(AnimatedSprite(game, pos=(7.25, 6.05)))
        add_sprite(AnimatedSprite(game, pos=(7.25, 7.95)))
        add_sprite(AnimatedSprite(game, pos=(3.25, 3.15)))
        add_sprite(AnimatedSprite(game, pos=(3.25, 5.85)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(10.95, 7.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(12.95, 7.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(10.95, 5.85)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(12.95, 5.85)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(10.95, 9.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(12.95, 9.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(10.95, 7.85)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(12.95, 7.85)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(09.95, 7.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(11.95, 7.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(09.95, 6.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'redlight/1.png', pos=(11.95, 6.15)))


        # npc map 
        add_npc(NPC(game))


    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)










