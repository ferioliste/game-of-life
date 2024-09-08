import pygame as pg
from .constants import SAVES_PATH, GameState, Colors
from .files_support import *

def run_main_menu(main_menu, manager, screen, inputs, game, time_delta):
    game_state = GameState.MAIN_MENU
    
    if inputs.resize == True:
        main_menu.update()

    if main_menu.gui_buttons[0] in inputs.pressed_menu_buttons:
        main_menu.close()
        game_state = GameState.SETUP
    elif main_menu.gui_buttons[1] in inputs.pressed_menu_buttons:
        game.grid_status.val = not game.grid_status.val
        main_menu.update()
    elif main_menu.gui_buttons[2] in inputs.pressed_menu_buttons:
        game.colored_cells_status.val = not game.colored_cells_status.val
        main_menu.update()

    manager.update(time_delta)
    screen.fill((0, 0, 0))

    main_menu.draw()

    return game_state

def run_setup_pause(setup_pause_menu, import_menu, export_menu, manager, screen, inputs, game, screen_settings, time_delta):
    game_state = GameState.SETUP_PAUSE
    
    if inputs.resize == True:
        setup_pause_menu.update()

    if setup_pause_menu.gui_buttons[0] in inputs.pressed_menu_buttons or pg.K_ESCAPE in inputs.newly_pressed_keys:
        setup_pause_menu.close()
        game_state = GameState.SETUP
    elif setup_pause_menu.gui_buttons[1] in inputs.pressed_menu_buttons:
        setup_pause_menu.close()
        game_state = GameState.IMPORT
        import_menu.open()
    elif setup_pause_menu.gui_buttons[2] in inputs.pressed_menu_buttons:
        setup_pause_menu.close()
        game_state = GameState.EXPORT
        export_menu.open()
    elif setup_pause_menu.gui_buttons[3] in inputs.pressed_menu_buttons:
        game.grid_status.val = not game.grid_status.val
        setup_pause_menu.update()
    elif setup_pause_menu.gui_buttons[4] in inputs.pressed_menu_buttons:
        game.colored_cells_status.val = not game.colored_cells_status.val
        setup_pause_menu.update()

    manager.update(time_delta)
    screen.fill((0, 0, 0))
    game.render(screen_settings)

    rect_surface = pg.Surface(screen_settings.size, pg.SRCALPHA)
    rect_surface.fill((127,127,127,127))
    screen.blit(rect_surface, (0,0))

    setup_pause_menu.draw()

    return game_state

def run_gameplay_pause(gameplay_pause_menu, manager, screen, inputs, game, screen_settings, time_delta):
    game_state = GameState.GAMEPLAY_PAUSE
    
    if inputs.resize == True:
        gameplay_pause_menu.update()

    if gameplay_pause_menu.gui_buttons[0] in inputs.pressed_menu_buttons or pg.K_ESCAPE in inputs.newly_pressed_keys:
        gameplay_pause_menu.close()
        game_state = GameState.GAMEPLAY
    elif gameplay_pause_menu.gui_buttons[1] in inputs.pressed_menu_buttons:
        gameplay_pause_menu.close()
        game.life_set = set(game.life_set_start)
        game_state = GameState.SETUP
    elif gameplay_pause_menu.gui_buttons[2] in inputs.pressed_menu_buttons:
        game.grid_status.val = not game.grid_status.val
        gameplay_pause_menu.update()
    elif gameplay_pause_menu.gui_buttons[3] in inputs.pressed_menu_buttons:
        game.colored_cells_status.val = not game.colored_cells_status.val
        gameplay_pause_menu.update()

    manager.update(time_delta)
    screen.fill((0, 0, 0))
    game.render(screen_settings)

    rect_surface = pg.Surface(screen_settings.size, pg.SRCALPHA)
    rect_surface.fill((127,127,127,127))
    screen.blit(rect_surface, (0,0))

    gameplay_pause_menu.draw()

    return game_state

def run_export(export_menu, setup_pause_menu, manager, screen, inputs, game, screen_settings, time_delta):
    game_state = GameState.EXPORT
    
    if inputs.resize == True:
        export_menu.update()

    if inputs.textbox_finished:
        file_path = SAVES_PATH + export_menu.gui_buttons[0].get_text() + ".txt"
        if file_exists(file_path):
            export_menu.buttons[2].name = "File already exists"
            export_menu.buttons[2].info.color = Colors.RED
            export_menu.update()
        else:
            write_tuples_to_file(game.life_set_start, file_path)
            export_menu.buttons[2].name = "File saved"
            export_menu.buttons[2].info.color = Colors.GREEN
            export_menu.update()
    
    if export_menu.gui_buttons[1] in inputs.pressed_menu_buttons:
        export_menu.buttons[2].name = ""
        export_menu.close()
        game_state = GameState.SETUP_PAUSE
        setup_pause_menu.open()

    manager.update(time_delta)
    screen.fill((0, 0, 0))
    game.render(screen_settings)

    rect_surface = pg.Surface(screen_settings.size, pg.SRCALPHA)
    rect_surface.fill((127,127,127,127))
    screen.blit(rect_surface, (0,0))

    export_menu.draw()

    return game_state

def run_import(import_menu, setup_pause_menu, manager, screen, inputs, game, screen_settings, time_delta):
    game_state = GameState.IMPORT
    
    if inputs.resize == True:
        import_menu.update()

    if inputs.textbox_finished:
        file_path = SAVES_PATH + import_menu.gui_buttons[0].get_text() + ".txt"
        if file_exists(file_path):
            game.import_life_set(read_tuples_from_file(file_path))
            import_menu.buttons[2].name = "File imported"
            import_menu.buttons[2].info.color = Colors.GREEN
            import_menu.update()
        else:
            import_menu.buttons[2].name = "File does not exist"
            import_menu.buttons[2].info.color = Colors.RED
            import_menu.update()
    
    if import_menu.gui_buttons[1] in inputs.pressed_menu_buttons:
        import_menu.buttons[2].name = ""
        import_menu.close()
        game_state = GameState.SETUP_PAUSE
        setup_pause_menu.open()

    manager.update(time_delta)
    screen.fill((0, 0, 0))
    game.render(screen_settings)

    rect_surface = pg.Surface(screen_settings.size, pg.SRCALPHA)
    rect_surface.fill((127,127,127,127))
    screen.blit(rect_surface, (0,0))

    import_menu.draw()

    return game_state