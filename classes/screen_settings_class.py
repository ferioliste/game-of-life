from code.constants import DEFAULT_CELL_SIZE, MOVEMENT_BUTTON, ZOOM_STEP

class ScreenSettings():
    def __init__(self, screen_size):
        self.size = screen_size

        self.zoom = 1.
        self.center = (0., 0.)
    
        self.cell_size = DEFAULT_CELL_SIZE * self.zoom

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = tuple(float(size[i]) for i in (0,1))
        self.half_size = tuple(float(size[i]) / 2 for i in (0,1))

    def update_view(self, inputs):
        if MOVEMENT_BUTTON in inputs.pressed_mouse_buttons and MOVEMENT_BUTTON not in inputs.newly_pressed_mouse_buttons:
            self.center = tuple(self.center[i] - inputs.mouse_movement[i] for i in (0,1))
        if inputs.wheel_scroll != 0:
            zoom_increase = ZOOM_STEP ** inputs.wheel_scroll
            self.zoom *= zoom_increase
            self.cell_size = DEFAULT_CELL_SIZE * self.zoom
            self.center = tuple(self.half_size[i] - inputs.mouse_position[i] - zoom_increase * (self.half_size[i] - inputs.mouse_position[i] - self.center[i]) for i in (0,1))