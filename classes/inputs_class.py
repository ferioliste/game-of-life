import pygame as pg
import pygame_gui

class Inputs():
    def __init__(self, manager):
        self.pressed_keys = set()
        self.pressed_mouse_buttons = set()
        self.wheel_scroll = 0
        self.mouse_position = (0., 0.)
        self.mouse_movement = (0., 0.)
        
        self.newly_pressed_keys = set()
        self.newly_pressed_mouse_buttons = set()

        self.quit = False
        self.resize = False
        self.new_window_size = (0., 0.)

        self.manager = manager
        self.pressed_menu_buttons = set()

        self.textbox_finished = False
        
    def update(self):
        self.newly_pressed_keys.clear()
        self.newly_pressed_mouse_buttons.clear()
        self.wheel_scroll = 0
        self.quit = False
        self.resize = False
        self.pressed_menu_buttons.clear()
        self.textbox_finished = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit = True
            
            elif event.type == pg.KEYDOWN:
                self.pressed_keys.add(event.key)
                self.newly_pressed_keys.add(event.key)
            elif event.type == pg.KEYUP:
                self.pressed_keys.discard(event.key)
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.pressed_mouse_buttons.add(event.button)
                self.newly_pressed_mouse_buttons.add(event.button)
            elif event.type == pg.MOUSEBUTTONUP:
                self.pressed_mouse_buttons.discard(event.button)
            
            elif event.type == pg.MOUSEWHEEL:
                self.wheel_scroll = event.y

            elif event.type == pg.VIDEORESIZE:
                self.resize = True
                self.new_window_size = event.size
            
            elif event.type == pg.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    self.pressed_menu_buttons.add(event.ui_element)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                self.textbox_finished = True

            self.manager.process_events(event)

        new_mouse_position = pg.mouse.get_pos()
        self.mouse_movement = tuple(new_mouse_position[i] - self.mouse_position[i] for i in (0,1))
        self.mouse_position = new_mouse_position