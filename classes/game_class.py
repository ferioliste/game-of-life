from collections import defaultdict
from code.files_support import *
from code.utils import *
import pygame as pg

from code.constants import OFFSETS, EDIT_BUTTON, DEFAULT_GRID_STATUS, DEFAULT_COLORED_CELLS_STATUS, Colors

class Game():
    def __init__(self, screen, file_name = None):
        self.screen = screen
        if file_name is None:
            self.life_set = set()
        else:
            self.life_set = read_tuples_from_file("./" + file_name + ".txt")
        self.life_set_start = set(self.life_set)
        self.neighbor_dict = defaultdict(int)
        self.considered_set = set()
        self.color_dict = self._ColorDict()

        self.pressed_status = True

        self.update_counter = 0

        self.grid_status = EncapsuledVar(DEFAULT_GRID_STATUS)
        self.colored_cells_status = EncapsuledVar(DEFAULT_COLORED_CELLS_STATUS)

    def update(self):
        self.neighbor_dict.clear()
        self.considered_set.clear()

        for alive in self.life_set:
            self.considered_set.add(alive)
            for i in range(8):
                pos = (alive[0] + OFFSETS[i][0], alive[1] + OFFSETS[i][1])
                self.neighbor_dict[pos] += 1
                self.considered_set.add(pos)

        for pos in self.considered_set:
            if pos in self.life_set:
                if not (self.neighbor_dict[pos] == 2 or self.neighbor_dict[pos] == 3):
                    self.life_set.discard(pos)
            else:
                if self.neighbor_dict[pos] == 3:
                    self.life_set.add(pos)

    def update_every_(self, n):
        self.update_counter += 1
        if self.update_counter >= n:
            self.update_counter = 0
            self.update()

    def edit(self, inputs, screen_settings):
        if EDIT_BUTTON in inputs.pressed_mouse_buttons:
            pos = tuple(int((screen_settings.center[i] + inputs.mouse_position[i] - screen_settings.half_size[i]) // screen_settings.cell_size) for i in (0,1))
            if EDIT_BUTTON in inputs.newly_pressed_mouse_buttons:
                self.pressed_status = not (pos in self.life_set)
            if self.pressed_status:
                self.life_set.add(pos)
                self.life_set_start.add(pos)
            else:
                self.life_set.discard(pos)
                self.life_set_start.discard(pos)

    def render(self, screen_settings):
        for pos in self.life_set:
            color = self.color_dict[pos] if self.colored_cells_status.val else Colors.WHITE
            
            top_left_x = int(screen_settings.half_size[0] - screen_settings.center[0] + pos[0]*screen_settings.cell_size)
            top_left_y = int(screen_settings.half_size[1] - screen_settings.center[1] + pos[1]*screen_settings.cell_size)
            bottom_right_x = int(screen_settings.half_size[0] - screen_settings.center[0] + (pos[0]+1)*screen_settings.cell_size)
            bottom_right_y = int(screen_settings.half_size[1] - screen_settings.center[1] + (pos[1]+1)*screen_settings.cell_size)
            pg.draw.rect(self.screen, color, pg.Rect(top_left_x, top_left_y, bottom_right_x-top_left_x, bottom_right_y-top_left_y))

        if self.grid_status.val and screen_settings.cell_size >= 3.:
            self.render_grid(screen_settings)

    def render_grid(self, screen_settings):
        line_thickness = min(4, max(1, int(screen_settings.cell_size * 0.1)))

        center_pos = tuple(int((screen_settings.center[i] - screen_settings.half_size[i]) // screen_settings.cell_size) for i in (0,1))
        
        pos_x = center_pos[0]
        while True:
            x = int(screen_settings.half_size[0] - screen_settings.center[0] + pos_x*screen_settings.cell_size)
            if x >= screen_settings.size[0]:
                break
            else:
                pg.draw.rect(self.screen, Colors.GRAY, pg.Rect(x, 0, line_thickness, screen_settings.size[1]))
                pos_x = pos_x + 1
        pos_y = center_pos[1]
        while True:
            y = int(screen_settings.half_size[1] - screen_settings.center[1] + pos_y*screen_settings.cell_size)
            if y >= screen_settings.size[1]:
                break
            else:
                pg.draw.rect(self.screen, Colors.GRAY, pg.Rect(0, y, screen_settings.size[0], line_thickness))
                pos_y = pos_y + 1

    def import_life_set(self, new_life_set):
        self.life_set = set(new_life_set)
        self.life_set_start = set(new_life_set)

    class _ColorDict():
        def __init__(self):
            self._color_dict = dict()

        def __getitem__(self, key):
            if key in self._color_dict:
                return self._color_dict[key]
            else:
                self._color_dict[key] = random_color()
                return self._color_dict[key]

class EncapsuledVar():
    def __init__(self, val):
        self.val = val