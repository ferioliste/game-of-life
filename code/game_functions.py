from .constants import TICK_RATE, UPDATE_RATE, GameState, Colors
import pygame as pg

def run_setup(screen, game, screen_settings, inputs, setup_pause_menu):
    game_state = GameState.SETUP
    
    game.edit(inputs, screen_settings)

    screen_settings.update_view(inputs)

    if pg.K_RETURN in inputs.pressed_keys:
        game_state = GameState.GAMEPLAY
    if pg.K_ESCAPE in inputs.newly_pressed_keys:
        setup_pause_menu.open()
        game_state = GameState.SETUP_PAUSE

    screen.fill(Colors.BLACK)
    game.render(screen_settings)

    return game_state

def run_gameplay(screen, game, screen_settings, inputs, gameplay_pause_menu):
    game_state = GameState.GAMEPLAY
    
    game.update_every_(TICK_RATE // UPDATE_RATE)
    screen_settings.update_view(inputs)

    if pg.K_ESCAPE in inputs.newly_pressed_keys:
        gameplay_pause_menu.open()
        game_state = GameState.GAMEPLAY_PAUSE

    screen.fill(Colors.BLACK)
    game.render(screen_settings)

    return game_state