

# now galton 2 with single stream etc

# INITIALIZE

import pygame, random

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE, GREY)

#SCREENWIDTH = 1440
#SCREENHEIGHT = 900
SCREENWIDTH = 1280
SCREENHEIGHT = 800


size = (SCREENWIDTH, SCREENHEIGHT)
horizjump = 1
itemcount = 0
# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("galton mania")


class Grain(pygame.sprite.Sprite):  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

    def __init__(self, color, size, x, y,itemnumber):

        super().__init__()
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.itemnumber = itemnumber

    def show(self):
        screen.fill(self.color, ((self.x,self.y), (1, 1)))

def makeone(grainsize,thiscolor,thissize,thisx,thisy,itemnumber):
    grainlist.append(Grain(thiscolor,thissize,thisx,thisy,itemnumber))
    grainsize += 1


# SETUP phase s s s s s s s s


carryon = True
blankscreen = True
counter = 0
grainsize = 0
grainlist=[]
increment=1
screen.fill(GREEN)
topofboard=5
bottomofboard=300
grassheight=10



while carryon:

    counter += 1

    # INPUT phase   i   i   i   i   i   i   i   i   i   i   i   i   i   i

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryon = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        carryon = False

    # UPDATE phase u   u   u   u   u   u   u   u   u   u   u   u   u   u   u

    for thegrain in grainlist:
        if topofboard <= thegrain.y <= SCREENHEIGHT-bottomofboard:
            if thegrain.itemnumber == 8:
                thegrain.x += horizjump
            elif thegrain.itemnumber == 9:
                thegrain.x -= horizjump
            else:
                thegrain.x += (random.choice([-horizjump,horizjump]))

        (r, g, b, a) = screen.get_at((thegrain.x,thegrain.y+increment))
        if r == 0:
            thegrain.y += increment

    # if counter % 10 == 0:
    if counter % 2 == 0:
        # makeone(grainsize, WHITE, 1, random.randint(0,SCREENWIDTH-1),10)
        makeone(grainsize, WHITE, 1, int(SCREENWIDTH/2), 10,itemcount)
        itemcount += 1

    # DRAW PHASE d d d d d d dd

    if blankscreen:
        pygame.draw.rect(screen, BLACK, (0, 0, SCREENWIDTH, SCREENHEIGHT-grassheight))

    for thegrain in grainlist:
        thegrain.show()

    pygame.display.flip()


# End loop e e e e e

pygame.quit()
