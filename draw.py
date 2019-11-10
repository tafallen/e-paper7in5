from PIL import Image, ImageDraw, ImageFont
import constants

## Helper Functions ######
def create_display():
    return Image.new('L', constants.screen_dimensions, constants.font_colour)

def get_font(size):
    return ImageFont.truetype(constants.font_name, size)

def get_text_size(image, text, size):
    d = ImageDraw.Draw(image)
    return d.textsize(text = text, font = get_font(size))

def get_center_positon(image, text, font_size, origin, panel):
    size = get_text_size(image, text, font_size)
    width = size[0]
    avail = panel[0] - origin[0]
    return int((avail - width)/2)

def get_right_align_positon(image, text, font_size, origin, panel):
    size = get_text_size(image, text, font_size)
    width = size[0]
    avail = panel[0] - origin[0]
    return avail - width

def get_resized_image(image_dimensions):
    original_icon = Image.open('icons/1.bmp')
    return original_icon.resize(image_dimensions)

## Line Drawing Functions ######
def draw_grid(image):
    d = ImageDraw.Draw(image)
    x = 0
    while x <= constants.screen_dimensions[0]:
        d.line([(x, 0),(x, constants.screen_dimensions[1])], fill=0, width=1)
        x+=constants.grid_increment
    y = 0
    while y <= constants.screen_dimensions[1]:
        d.line([(0, y),(constants.screen_dimensions[0], y)], fill=0, width=1)
        y+=constants.grid_increment

def draw_diagonals(image):
    d = ImageDraw.Draw(image)
    d.line([(0,0),(constants.screen_dimensions)], fill=0, width=1)
    d.line([(0,constants.screen_dimensions[1]),(constants.screen_dimensions[0]),0], fill=0, width=1)
    
## Text Drawing Functions ######
def draw_text(image, location, text, size):
    d = ImageDraw.Draw(image)
    d.text(location, text, fill=0, font=get_font(size))

def draw_centered_text(image, origin, panel_size, text, size):
    x = get_center_positon(image, text, size, origin, panel_size)
    draw_text(image, (x, origin[1]), text, size)

def draw_right_align_text(image, origin, panel_size, text, size):
    x = get_right_align_positon(image, text, size, origin, panel_size)
    draw_text(image, (x, origin[1]), text, size)

def draw_text_sample(image):
    text_origin = (10, 10)
    font_index = 0
    text = " - AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

    while text_origin[1] < constants.screen_dimensions[1] and font_index < len(constants.font_sizes):
        font_size = constants.font_sizes[font_index]
        text_size = get_text_size(image, str(font_size) + text, font_size)
        
        draw_text(image, text_origin, str(font_size) + text, font_size)
        new_text_origin = (text_origin[0], (text_origin[1] + text_size[1] + 5))
        
        text_origin = new_text_origin
        font_index += 1

    draw_text(image, (0,475), "Left Align", 24)
    draw_centered_text(image, (0, 475), (384, 640), "Centered", 24)
    draw_right_align_text(image, (0, 475), (384, 640), "Right Align", 24)

## Image Drawing Functions ######
def draw_image(image, origin, image_dimensions):
    box = (origin[0], origin[1], origin[0] + image_dimensions[0], origin[1] + image_dimensions[1])
    image.paste(get_resized_image(image_dimensions), box)

def draw_image_sample(image):
    draw_image(image, (20,520), (50,50))
    draw_image(image, (90,520), (60,60))
    draw_image(image, (170,520), (80,80))
    draw_image(image, (270,520), (100,100))
