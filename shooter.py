import pygame

pygame.init()
screen=pygame.display.set_mode((900,600))

space=pygame.transform.scale(pygame.image.load('spacebg.png'),(900,600))

redspaceship=pygame.image.load('red_ship.png')
redscale=pygame.transform.scale(redspaceship,(50,50))
redturn=pygame.transform.rotate(redscale,270)

yellowspaceship=pygame.image.load('yellow_ship.png')
yellowscale=pygame.transform.scale(yellowspaceship,(50,50))
yellowturn=pygame.transform.rotate(yellowscale,90)

redbullets=[]
yellowbullets=[]

maxbullets=3
bulletvelocity=7

playing=True

yellow=pygame.Rect(200,300,50,50)
red=pygame.Rect(700,300,50,50)

def yellowmovement(key_pressed,yellow):
    if key_pressed[pygame.K_w] and yellow.y>0:
        yellow.y=yellow.y-5
    if key_pressed[pygame.K_s] and yellow.y<600:
        yellow.y=yellow.y+5
    if key_pressed[pygame.K_a] and yellow.x>0:
        yellow.x=yellow.x-5
    if key_pressed[pygame.K_d] and yellow.x<400:
        yellow.x=yellow.x+5

def redmovement(key_pressed,red):
    if key_pressed[pygame.K_UP] and red.y>0:
        red.y=red.y-5
    if key_pressed[pygame.K_DOWN] and red.y<600:
        red.y=red.y+5
    if key_pressed[pygame.K_LEFT] and red.x>450:
        red.x=red.x-5
    if key_pressed[pygame.K_RIGHT] and red.x<900:
        red.x=red.x+5


while playing==True:
    clock=pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                # start here next lesson
    screen.blit(space,(0,0))
    screen.blit(redturn,(red.x,red.y))
    screen.blit(yellowturn,(yellow.x,yellow.y))
    key_pressed=pygame.key.get_pressed()
    yellowmovement(key_pressed,yellow)
    redmovement(key_pressed,red)
    pygame.draw.rect(screen,'black',pygame.Rect(450,0,10,600))
    pygame.display.update()