from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction
import time
from datetime import datetime
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface(MINIMAP_RES)

sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, sc_map, player, clock)
interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
interaction.play_music()
print(map_now)
print(player_pos)

start_time = datetime.now()

player.movement()
drawing.background(player.angle)
walls, wall_shot = ray_casting_walls(player, drawing.textures)
drawing.world(walls + [obj.object_locate(player, sc, drawing, sprites, ray_casting_walls) for obj in sprites.list_of_objects])
drawing.fps(clock)
drawing.player_weapon([wall_shot, sprites.sprite_shot])

while map_now[0] != "title":
    interaction.interaction_objects(player)
    interaction.npc_action()
    interaction.clear_world()

    if all([obj.pause for obj in sprites.list_of_objects]):
        player.movement()
        drawing.background(player.angle)
        walls, wall_shot = ray_casting_walls(player, drawing.textures)
        drawing.world(walls + [obj.object_locate(player, sc, drawing, sprites, ray_casting_walls) for obj in sprites.list_of_objects])
        drawing.fps(clock)
        drawing.player_weapon([wall_shot, sprites.sprite_shot])
    

    pygame.display.flip()
    clock.tick()
score = str(datetime.now() - start_time).split(".")
print(score)
drawing.credits(score[0])
