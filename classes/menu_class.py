import pygame as pg
import pygame_gui
from code.constants import MENU_FILL_PROPORTION, BUTTONS_THEMES, Colors

class Menu:
    def __init__(self, buttons, screen, manager, screen_settings, max_button_width, max_button_height, max_button_padding):
        self.buttons = buttons
        self.manager = manager
        self.screen = screen
        self.screen_settings = screen_settings

        self.max_button_size = max_button_width
        self.max_button_height = max_button_height
        self.max_button_padding = max_button_padding

        self.manager.get_theme().load_theme(BUTTONS_THEMES)
        
        self.fonts = self._FontDict()
        
        self.texts = []
        self.gui_buttons = []

    def create_buttons(self):
        button_width = min(self.max_button_size, int(self.screen_settings.size[0] * MENU_FILL_PROPORTION))
        max_total_height = (len(self.buttons)-1) * (self.max_button_height+self.max_button_padding) + self.max_button_height
        if max_total_height > MENU_FILL_PROPORTION * self.screen_settings.size[1]:
            total_height = int(MENU_FILL_PROPORTION * self.screen_settings.size[1])
            button_height = int(self.max_button_height * MENU_FILL_PROPORTION * self.screen_settings.size[1] / max_total_height)
            button_padding = int(self.max_button_padding * MENU_FILL_PROPORTION * self.screen_settings.size[1] / max_total_height)
        else:
            total_height = max_total_height
            button_height = self.max_button_height
            button_padding = self.max_button_padding

        for (i, button) in enumerate(self.buttons):
            if button.type == "text":
                font = self.fonts[button.info.size]
                text_surface = font.render(button.name, True, button.info.color)
                text_rect = text_surface.get_rect(center=(self.screen_settings.size[0] // 2, (self.screen_settings.size[1] - total_height) // 2 + (button_height+button_padding)*i + button_height//2))

                self.texts.append((text_surface, text_rect))
            elif button.type == "textbox":
                gui_button = pygame_gui.elements.UITextEntryLine(
                    relative_rect=pg.Rect(((self.screen_settings.size[0] - button_width) // 2, (self.screen_settings.size[1] - total_height) // 2 + (button_height+button_padding)*i),
                                            (button_width, button_height)
                                            ),
                    manager=self.manager, object_id='#default_button'
                    )
                self.gui_buttons.append(gui_button)
            else:
                button_type = '#default_button' if button.info is None else ('#active_button' if button.info.val else '#inactive_button')
                gui_button = pygame_gui.elements.UIButton(
                    relative_rect=pg.Rect(((self.screen_settings.size[0] - button_width) // 2, (self.screen_settings.size[1] - total_height) // 2 + (button_height+button_padding)*i),
                                            (button_width, button_height)
                                            ),
                    text=button.name, manager=self.manager, object_id=button_type
                    )
                self.gui_buttons.append(gui_button)

    def destroy_buttons(self):
        for gui_button in self.gui_buttons:
            gui_button.kill()
        self.texts.clear()
        self.gui_buttons.clear()

    def open(self):
        self.create_buttons()
    def close(self):
        self.destroy_buttons()

    def update(self):
        self.destroy_buttons()
        self.create_buttons()
    
    def draw(self):
        for text in self.texts:
            self.screen.blit(*text)
        
        self.manager.draw_ui(self.screen)

    class _FontDict():
        def __init__(self):
            self._font_dict = dict()
        def __getitem__(self, key):
            if key in self._font_dict:
                return self._font_dict[key]
            else:
                self._font_dict[key] = pg.font.SysFont(None, key)
                return self._font_dict[key]

class Button():
    def __init__(self, name, type = "clickable", info = None):
        self.name = name
        self.type = type
        self.info = info

class FontInfo():
    def __init__(self, size, color):
        self.size = size
        self.color = color