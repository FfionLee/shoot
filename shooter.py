import pygame
import os

pygame.mixer.init()

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

red_health=10
yellow_health=10

redshoot=pygame.mixer.Sound('Grenade+1.mp3')
yellowshoot=pygame.mixer.Sound('Gun+Silencer.mp3')

font=pygame.font.SysFont('Times New Roman',50)

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

def handlebullets():
    global yellowbullets, redbullets, yellow, red, red_health, yellow_health
    for yb in yellowbullets:
        yb.x=yb.x+7
        if yb.colliderect(red):
            red_health=red_health-1
            yellowbullets.remove(yb)
    
    for rb in redbullets:
        rb.x=rb.x-7
        if rb.colliderect(yellow):
            yellow_health=yellow_health-1
            redbullets.remove(rb)
    


while playing==True:
    clock=pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e and len(yellowbullets)<3:
                bullet=pygame.Rect(yellow.x,yellow.y+20,10,5)
                yellowbullets.append(bullet)
                yellowshoot.play()
            if event.key==pygame.K_RCTRL and len(redbullets)<3:
                bullet=pygame.Rect(red.x,red.y+20,10,5)
                redbullets.append(bullet)
                redshoot.play()
    screen.blit(space,(0,0))
    screen.blit(redturn,(red.x,red.y))
    screen.blit(yellowturn,(yellow.x,yellow.y))
    key_pressed=pygame.key.get_pressed()
    yellowmovement(key_pressed,yellow)
    redmovement(key_pressed,red)
    handlebullets()
    for b in yellowbullets:
        pygame.draw.rect(screen,'white',b)
    for b in redbullets:
        pygame.draw.rect(screen,'white',b)
    ytext=font.render('Health: '+str(yellow_health),True,'white')
    rtext=font.render('Health: '+str(red_health),True,'white')
    screen.blit(ytext,(100,20))
    screen.blit(rtext,(600,20))
    if red_health<0:
        ywin=font.render('Yellow wins!',True,'white')
        screen.blit(ywin,(300,300))
        pygame.time.delay(1000)
    elif yellow_health<0:
        rwin=font.render('Red wins!',True,'white')
        screen.blit(rwin,(300,300))
        pygame.time.delay(1000)
    pygame.draw.rect(screen,'black',pygame.Rect(450,0,10,600))
    pygame.display.update()
