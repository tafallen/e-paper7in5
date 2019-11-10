# e-paper7in5 Demo
Starter project for using the Waveshare 7in5 black &amp; white e-paper screen

This has been developed for use with the WaveShare 7.5in black and white e-paper screen, and a Raspberry Pi, to demonstrate the basics of drawing, writing text and displaying images on the e-paper screen. It's the sort of thing I wish I'd found when I started meddling wigth the display.

## External Dependencies

epd7in5.py and epdconfig.py both come from WaveShare's e-Paper GitHub repo [here|https://github.com/waveshare/e-Paper]

fonts/Roboto-Regular.ttf is from [here|]https://fonts.google.com/]

## Pre-requisites

Pillow - install using `pip3 install Pillow`

## Project Structure

`demo.py` - Run this project to draw to the e-paper screen
`draw.py` - Contains the methods used to write to the screen
`constants.py` - Project constants such as screen size, font paths, etc..
