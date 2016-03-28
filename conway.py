"""
conway.py
Author: Glen Passow
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.state = False

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

thinline = LineStyle(1, black)
rectangle = RectangleAsset(20, 20, thinline, white)

a = 0
b = 0

squares = {}

height = 10
width = 10

for x in range(0, height):
    for y in range(0, width):
        squares[(x,y)] = cell(rectangle, (a, b))
        a = a+20
    a = 0
    b = b+20
print(squares)

for z in range(0, height):
    for w in range(0, width):
        squares[(w, z)]
        if squares[(w+1, z+1)] self.state == True:
            surroundingCells = surroundingCells + 1
        else:
        
        
        
        
    

    


myapp = App()
myapp.run()