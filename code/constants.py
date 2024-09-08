from enum import Enum

INITIAL_WINDOW_SIZE = (800, 600)
TICK_RATE = 60

UPDATE_RATE = 5   # updates per second
DEFAULT_CELL_SIZE = 20   # in pixels
ZOOM_STEP = 1.25

MOVEMENT_BUTTON = 3
EDIT_BUTTON = 1

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (64, 64, 64)

OFFSETS = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))
class GameState(Enum):
    MAIN_MENU = 0
    SETUP = 1
    GAMEPLAY = 2
    GAMEPLAY_PAUSE = 3
    SETUP_PAUSE = 4
    IMPORT = 5
    EXPORT = 6

DEFAULT_GRID_STATUS = False
DEFAULT_COLORED_CELLS_STATUS = False
DEFAULT_MAX_BUTTON_WIDTH = 300
DEFAULT_MAX_BUTTON_HEIGHT = 50
MAX_BUTTON_PADDING = 20
MENU_FILL_PROPORTION = 0.9

SAVES_PATH = "./saves/"

BUTTONS_THEMES = {'#default_button': {
                    'colours': {
                        'normal_bg': "#{:02X}{:02X}{:02X}".format(*Colors.BLACK),  # Black background
                        'hovered_bg': "#{:02X}{:02X}{:02X}".format(32, 32, 32),
                        'active_bg': "#{:02X}{:02X}{:02X}".format(64, 64, 64),
                        'normal_border': '#FFFFFF',  # White border
                        'hovered_border': '#FFFFFF',
                        'active_border': '#FFFFFF',
                        'normal_text': '#FFFFFF',  # White text
                        'hovered_text': '#FFFFFF',
                        'active_text': '#FFFFFF',
                    },
                    'font': {
                        'name': 'default_font',
                        'size': 14,
                        'style': 'bold'},
                    'misc': {
                        'border_width': 1,
                        'shadow_width': 0}
                    },
                    '#active_button': {
                    'colours': {
                        'normal_bg': "#{:02X}{:02X}{:02X}".format(0, 127, 0),  # Black background
                        'hovered_bg': "#{:02X}{:02X}{:02X}".format(0, 159, 0),
                        'active_bg': "#{:02X}{:02X}{:02X}".format(0, 191, 0),
                        'normal_border': '#FFFFFF',  # White border
                        'hovered_border': '#FFFFFF',
                        'active_border': '#FFFFFF',
                        'normal_text': '#FFFFFF',  # White text
                        'hovered_text': '#FFFFFF',
                        'active_text': '#FFFFFF',
                    },
                    'font': {
                        'name': 'default_font',
                        'size': 14,
                        'style': 'bold'},
                    'misc': {
                        'border_width': 1,
                        'shadow_width': 0}
                    },
                    '#inactive_button': {
                    'colours': {
                        'normal_bg': "#{:02X}{:02X}{:02X}".format(127, 0, 0),  # Black background
                        'hovered_bg': "#{:02X}{:02X}{:02X}".format(159, 0, 0),
                        'active_bg': "#{:02X}{:02X}{:02X}".format(191, 0, 0),
                        'normal_border': '#FFFFFF',  # White border
                        'hovered_border': '#FFFFFF',
                        'active_border': '#FFFFFF',
                        'normal_text': '#FFFFFF',  # White text
                        'hovered_text': '#FFFFFF',
                        'active_text': '#FFFFFF',
                    },
                    'font': {
                        'name': 'default_font',
                        'size': 14,
                        'style': 'bold'},
                    'misc': {
                        'border_width': 1,
                        'shadow_width': 0}
                    }
                }
