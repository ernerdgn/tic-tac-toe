import pygame

MAP = [["","",""],
       ["","",""],
       ["","",""]]
WIDTH, HEIGHT = 600, 600
COLOR_O = (125,0,125)
COLOR_X = (0,125,125)
BLACK = (0,0,0)
WHITE = (255,255,255)
x_to_move = True

def is_empty(row,column):
    if MAP[row][column] == "":
        return True
    else:
        return False

def draw_o(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius, 4)

def draw_x(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos, 4)
    pygame.draw.line(surface, color, (start_pos[0] + 170, start_pos[1]), (end_pos[0] - 170, end_pos[1]), 4)

def check_for_winner(MAP):
    line = ""
    for row in range(3):
        for column in range(3):
            line += MAP[row][column]
        if line == "xxx" or line == "ooo":
            return False
        else:
            line = ""

    for column in range(3):
        for row in range(3):
            line += MAP[row][column]
        if line == "xxx" or line == "ooo":
            return False
        else:
            line = ""
    
    for row in range(3):
        for column in range(3):
            if row == column:
                line += MAP[row][column]
    if line == "xxx" or line == "ooo":
        return False
    else:
        line = ""
    
    line += MAP[1][1]
    for row in range(3):
        for column in range(3):
            if abs(row - column) == 2:
                line += MAP[row][column]
    if line == "xxx" or line == "ooo":
        return False
    else:
        line = ""

    if line == "":
        return True
    
def check_draw(MAP):
    for row in range(3):
        for column in range(3):
            if MAP[row][column] == "":
                return False
    return True
            