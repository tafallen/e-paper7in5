from PIL import Image, ImageDraw
import draw
import constants
import epd7in5

def display_on_e_paper(image):
     buffer = epd.getbuffer(image)
     epd.display(buffer)
     epd.sleep()

image = draw.create_display()

draw.draw_diagonals(image)
draw.draw_grid(image)
draw.draw_text_sample(image)

epd = epd7in5.EPD()
epd.init()

display_on_e_paper(image)
#image.show()
