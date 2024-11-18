import json
import pygame as pgm
import class_ as game
import random

# Settings
FPS = 10
timer = pgm.time.Clock()
window_size = [1000, 800]
pgm.display.set_caption("AI playing tag game")
BG = [255, 255, 255]
INNOCENT = [0, 255, 0]
HUNTER = [255, 0, 0]
object_list = [game.Entity(game.IT, [random.randint(0, 80), random.randint(0, 80)], []), game.Entity(game.RUNNER, [random.randint(0, 80), random.randint(0, 80)], [])]
object_list[0].objects = object_list
object_list[1].objects = object_list
not_closed = True
screen = pgm.display.set_mode(window_size)

# Run programm
while not_closed:
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            not_closed = False
    screen.fill(BG)
    for object_ in object_list:
        if object_.about == game.IT:
            pgm.draw.rect(screen, HUNTER, [object_.pos[0] / 80 * 1000, object_.pos[1] / 80 * 800, 5, 5])
        if object_.about == game.RUNNER:
            pgm.draw.rect(screen, INNOCENT, [object_.pos[0] / 80 * 1000, object_.pos[1] / 80 * 800, 5, 5])
        object_.update()
    timer.tick(FPS)
    pgm.display.update()
    
pgm.quit()
