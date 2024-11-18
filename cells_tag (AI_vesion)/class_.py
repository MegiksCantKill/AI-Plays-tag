# In this version only runner will be AI supported
import pygame as pgm
import random
import funcs
import numpy as np
import json
import math
import ai

RUNNER = 0
IT = 1

pretrained = json.load(open("weights.json", "r", encoding = "utf-8"))
pretrained = pretrained["weights"]

class Entity:
    def __init__ (self, about: int, init_pos: list, objects: list):
        """Object memory

        Args:
            init_weights (list),
            learn_rate (float),
            about (int),
            init_pos (list)
        """
        self.about = about
        self.pos = init_pos
        self.objects = objects
    def update(self):
        if self.about == RUNNER:
            hunters_list = [x for x in self.objects if x.about == IT]
            hunters_positions = [x.pos for x in hunters_list]
            hunter_avg = funcs.vector_avg(hunters_positions)
            pretrained_ai = ai.AI(0.01, pretrained, 200)
            self.pos = pretrained_ai.predict(self.pos[0], self.pos[1], hunter_avg[0], hunter_avg[1])
            
            if self.pos[0] > 80:
                self.pos[0] = 80
            if self.pos[0] < 0:
                self.pos[0] = 0
            if self.pos[1] > 80:
                self.pos[1] = 80
            if self.pos[1] < 0:
                self.pos[1] = 0

            for pos_ in hunters_positions:
                if self.pos == pos_:
                    print(f"Object \"{self}\" lost")
                
        if self.about == IT:
            innocents_list = [x for x in self.objects if x.about == RUNNER]
            innocents_list_pos = [x.pos for x in innocents_list]
            innocent_avg = funcs.vector_avg(innocents_list_pos)
            
            if int(self.pos[0]) > int(innocent_avg[0]):
                self.pos[0] -= 1
            if int(self.pos[0]) < int(innocent_avg[0]):
                self.pos[0] += 1

            if int(self.pos[1]) > int(innocent_avg[1]):
                self.pos[1] -= 1
            if int(self.pos[1]) < int(innocent_avg[1]):
                self.pos[1] += 1
            