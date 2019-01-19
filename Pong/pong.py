'''
Created on Dec 16, 2018

@author: Moises
'''

import pygame
import sys
import random
import math
import time
from pygame.locals import *

window_x = 800
window_y = 800
pixel_size = 20 # Each visible game pixel is 20x20
colors = [(255, 255, 255), [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], (255, 255, 100), (255,0 ,0), \
          (255, 255, 0), (50, 50, 50), (100, 100, 100), (255, 255, 255)]
move_increment = 20
direction = 4 # 1 is right, 2 left, 3 up, 4 down  
player_x = 760
player_y = 0
GAME_STATE = 1 # 1 is menu, 2 is playing state, 3 is game over
    
'''INIT WINDOW & DRAW SURFACE'''
pygame.init() #init pygame module
pygame.font.init()

DISPLAYSURF = pygame.display.set_mode((window_x, window_y)) #creates draw surface, w=600, h=600
pygame.display.set_caption('PONG') #window caption
'''END WINDOW AND DRAW INITIALIZATION'''

def message_display(text, x, y, size, rgb):
# Creates a 'font' object that serves as a template to display text to the screen. 
# the parameter rgb should be a 3 element list, with each element corresponding to an rgb value.
# text parameter is a string, x, y, and size are type int. Size is font size.
    font = pygame.font.SysFont(None, size) #font object, none corresponds to system font
    caption = font.render(text, True, rgb) # caption object where text as string is passed
    DISPLAYSURF.blit(caption, (x, y)) # draws text to board/surface

def draw_board():
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 0, window_x, window_y))
    
def draw_pixel(x, y, color):
    pygame.draw.rect(DISPLAYSURF, color, (x, y, pixel_size, pixel_size))
    
def check_bounds():
    return

def draw_player(player_y):
    for i in range(4):
        draw_pixel(player_x, player_y+5*i, colors[0])

def run_game(mouse_y, player_y):
    check_bounds()
    player_y = mouse_y
    draw_player(player_y)
    
    
def pause_game():
    return
    
def main():
    global player_y, window_x, window_y, pixel_size, GAME_STATE
    
    bounds_passed = False
    
    while True: 
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        
        draw_board()
        
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit() # exits on close
            #if event.type == KEYDOWN:
        
        run_game(mouse_pos[1], player_y)     
                
        pygame.display.update()
        
main()
    