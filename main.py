# This file was created by: Owen Pence
# Works cited: Chris Cozort & OpenAi

# 
import pygame as pg
from settings import *
from sprites import *
import sys
from random import randint
from os import path
import pygame
import sys




# game class 
class Game:
    # behold the methods...
    def __init__(self):
        pg.init()
        # Display
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # Name of game
        pg.display.set_caption("Pency's Game!")
        # Timer clock countdown
        self.clock = pg.time.Clock()
        self.load_data()
        self.font = pg.font.Font(None, 36)
        self.timer_seconds = 20  # Timer countdown duration in seconds
        self.timer_event = pg.USEREVENT + 1
        pg.time.set_timer(self.timer_event, 1000)  
    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == self.timer_event:
                    self.timer_seconds -= 1
                    if self.timer_seconds <= 0:
                        running = False  # End the game when timer reaches 0

            self.screen.fill((255, 255, 255))

            # Display timer countdown at the top-middle of the screen
            timer_text = self.font.render("Time: " + str(self.timer_seconds), True, (0, 0, 0))
            timer_text_rect = timer_text.get_rect(center=(self.width // 2, 50))
            self.screen.blit(timer_text, timer_text_rect)
            self.clock.tick(20)


    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        # sprites for walls, coins, negatives
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                # Tile location of wall
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                # Tile location of Player
                if tile == 'P':
                    self.player = Player(self, col, row)
                # Tile location of Coin
                if tile == 'C':
                    Coin(self, col, row)
                # Tile location of Negative
                if tile == 'N':
                    Negative(self, col, row)
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # this is input
            self.events()
            # this is processing
            self.update()
            # this output
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()
    # methods
    def input(self): 
        pass
    def update(self):
        self.all_sprites.update()
    
    
    # Grid drawn for the game
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, GREEN, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, GREEN, (0, y), (WIDTH, y))
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('Times new roman')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        pg.display.flip()
     

    def events(self):
            # listening for events
            for event in pg.event.get():
                # when you hit the red x the window closes the game ends
                if event.type == pg.QUIT:
                    self.quit()
                    print("the game has ended..")
                # keyboard events
                # W = up
                # D - right
                # S - Down
                # A - Left
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
# g.show_go_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()

