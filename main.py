import pygame as pg
import pygame_gui
import sys
import numpy as np

from classes.game_class import Game
from classes.inputs_class import Inputs
from classes.screen_settings_class import ScreenSettings
from classes.menu_class import Button, FontInfo, Menu
from code.menu_functions import *
from code.game_functions import *

pg.init()

# import constants
from code.constants import INITIAL_WINDOW_SIZE, TICK_RATE
from code.constants import DEFAULT_MAX_BUTTON_WIDTH, DEFAULT_MAX_BUTTON_HEIGHT, MAX_BUTTON_PADDING
from code.constants import GameState, Colors

# setup pygame env
screen = pg.display.set_mode(INITIAL_WINDOW_SIZE, pg.RESIZABLE)
pg.display.set_caption("Game of life")
manager = pygame_gui.UIManager(INITIAL_WINDOW_SIZE)
clock = pg.time.Clock()

game = Game(screen)
game_state = GameState.MAIN_MENU
inputs = Inputs(manager)
screen_settings = ScreenSettings(INITIAL_WINDOW_SIZE)

main_menu_buttons = [
                Button("Game of Life", "text", FontInfo(48, Colors.WHITE)),
                Button("Start game", "clickable"),
                Button("Toggle grid", "toggle", game.grid_status),
                Button("Toggle colored cells",  "toggle", game.colored_cells_status)
                ]
main_menu = Menu(main_menu_buttons,
                screen, manager, screen_settings,
                DEFAULT_MAX_BUTTON_WIDTH, DEFAULT_MAX_BUTTON_HEIGHT, MAX_BUTTON_PADDING
                )

setup_pause_menu_buttons = [
                Button("Resume", "clickable"),
                Button("Import", "clickable"),
                Button("Export", "clickable"),
                Button("Toggle grid", "toggle", game.grid_status),
                Button("Toggle colored cells", "toggle", game.colored_cells_status)
                ]
setup_pause_menu = Menu(setup_pause_menu_buttons,
                screen, manager, screen_settings,
                DEFAULT_MAX_BUTTON_WIDTH, DEFAULT_MAX_BUTTON_HEIGHT, MAX_BUTTON_PADDING
                )

gameplay_pause_menu_buttons = [
                Button("Resume", "clickable"),
                Button("Go back to edit", "clickable"),
                Button("Toggle grid", "toggle", game.grid_status),
                Button("Toggle colored cells", "toggle", game.colored_cells_status)
                ]
gameplay_pause_menu = Menu(gameplay_pause_menu_buttons,
                screen, manager, screen_settings,
                DEFAULT_MAX_BUTTON_WIDTH, DEFAULT_MAX_BUTTON_HEIGHT, MAX_BUTTON_PADDING
                )

export_menu_buttons = [
                Button("Enter the name of the new file", "text", FontInfo(28, Colors.WHITE)),
                Button("", "textbox"),
                Button("", "text", FontInfo(28, Colors.GREEN)),
                Button("Go back", "clickable"),
                ]
export_menu = Menu(export_menu_buttons,
                screen, manager, screen_settings,
                DEFAULT_MAX_BUTTON_WIDTH, DEFAULT_MAX_BUTTON_HEIGHT, MAX_BUTTON_PADDING
                )

import_menu_buttons = [
                Button("Enter the file to import", "text", FontInfo(28, Colors.WHITE)),
                Button("", "textbox"),
                Button("", "text", FontInfo(28, Colors.GREEN)),
                Button("Go back", "clickable"),
                ]
import_menu = Menu(import_menu_buttons,
                screen, manager, screen_settings,
                DEFAULT_MAX_BUTTON_WIDTH, DEFAULT_MAX_BUTTON_HEIGHT, MAX_BUTTON_PADDING
                )

main_menu.open()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    inputs.update()
    if inputs.quit == True:
        running = False
    if inputs.resize == True:
        screen_settings.size = inputs.new_window_size
        manager.set_window_resolution(inputs.new_window_size)

    match game_state:
        case GameState.MAIN_MENU:
            game_state = run_main_menu(main_menu, manager, screen, inputs, game, time_delta)
        case GameState.GAMEPLAY_PAUSE:
            game_state = run_gameplay_pause(gameplay_pause_menu, manager, screen, inputs, game, screen_settings, time_delta)
        case GameState.SETUP_PAUSE:
            game_state = run_setup_pause(setup_pause_menu, import_menu, export_menu, manager, screen, inputs, game, screen_settings, time_delta)
        case GameState.EXPORT:
            game_state = run_export(export_menu, setup_pause_menu, manager, screen, inputs, game, screen_settings, time_delta)
        case GameState.IMPORT:
            game_state = run_import(import_menu, setup_pause_menu, manager, screen, inputs, game, screen_settings, time_delta)
        case GameState.SETUP:
            game_state = run_setup(screen, game, screen_settings, inputs, setup_pause_menu)
        case GameState.GAMEPLAY:
            game_state = run_gameplay(screen, game, screen_settings, inputs, gameplay_pause_menu)
        case _:
            print("Something has gone wrong with the game state :(")

    pg.display.flip()
    clock.tick(TICK_RATE)

pg.quit()
sys.exit()