from datetime import datetime
import colorsys
import random

def get_current_time_formatted():
    return datetime.now().strftime('%Y%m%d_%H%M%S')

def random_color():
    brightness = random.uniform(0.7, 1.0)
    hue = random.random()
    saturation = random.uniform(0.5, 1.0)

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, brightness)
    
    return (int(r * 255), int(g * 255), int(b * 255))