from npc import *
from Newdialog import *
import pygame
import map
import player
from vector import *
import time
from Quest import *

win_width = 1024
win_height = 768
credit_pos = win_height - 1
mode = "title"
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((win_width, win_height))
font = pygame.font.SysFont("Courier New", 12)
font1 = pygame.font.SysFont("Courier New", 40)
splash_img = pygame.image.load("images/splash.png")
credits = pygame.image.load("images/credits.png")
clock = pygame.time.Clock()
done = False
shoot_time = 0
npc = npc_create("npcfile.txt")
M = map.Map("maps\\School_Test_Map.txt", (1141,1033,3,1149,1148,1146,1150,1147),(1480,1484,1485,1486,1487,1488,1476,1479,1477,1474,1481,1483),(3054,3055),(728, 100,2886,-1073738939,1610613488,1610613487,1610613486), clock)
P = player.Player((69, 19), M.get_tile_dimensions(),shoot_time)
M.addPlayer(P)
for i in npc:
    P.mMap.addnpc(i)
q_var = quest_var("quests")

current_frame = 0
animation_timer = 0
book = []
books = int(q_var["books"])
Quest_complete = False
paul = pygame.image.load("paul_fieri.png")
pickup_sound = pygame.mixer.Sound("pickup.wav")

quest = quest_set("quests")


while mode == "title":
    screen.blit(splash_img, (0,0))
    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

    # Event Processing
    evt = pygame.event.poll()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
            break
    elif evt.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 730 <= mpos[0] <= 930 and 40 <= mpos[1] <= 112:
            mode = "game"
            break
        elif 698 <= mpos[0] <= 979 and 131 <= mpos[1] <= 196:
            mode = "credits"
            while not done:
                screen.fill((0,0,0))
                screen.blit(credits,(0,credit_pos))
                text = "fps: " + str(int(clock.get_fps()))
                screen.blit(font.render(text, False, (255, 255, 255)), (0, 13))
                pygame.display.flip()
                credit_pos -= 100 * dt
                evt = pygame.event.poll()
                if evt.type == pygame.QUIT:
                    done = True
                elif evt.type == pygame.KEYDOWN:
                    if evt.key == pygame.K_ESCAPE:
                        mode = "title"
                        done = True
                        break

while mode == "game":
    # Updates
    q_var["books"] = int(books)

    dt = clock.tick(60) / 1000.0

    touching = False

    # Event Processing
    evt = pygame.event.poll()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            mode = "title"
            break

    keys = pygame.key.get_pressed()

    if evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_e:
            for i in npc:
                t = P.mPos- i.cord
                if t.magnitude<50:
                    if i.name =="fuckface":
                        convo(screen,"fookfacedia",clock)
                    elif i.name =="alex1":
                        convo(screen,"Alex1.txt",clock)
                    elif i.name =="alex2":
                        convo(screen,"Alex2.txt",clock)
                    elif i.name =="alex3":
                        convo(screen,"Alex3.txt",clock)
                    elif i.name == "ASS":
                        convo(screen, "Alex4.txt", clock)
                    for j in quest:
                        if j.npc == i.name:
                            newvar = j.check(q_var,screen,clock)
                            q_var = newvar
                            if j.phase >= 2:
                                books = int(q_var["books"])



    P.handle_keys(keys, dt)
    M.setCamera((P.mPos[0] - win_width // 2, P.mPos[1] - win_height // 2), (win_width, win_height))

    if books > 0:
        if keys[pygame.K_SPACE] and P.shoot <= 0:
         bx = int(P.mPos[0])
         by = int(P.mPos[1])
         bx2 = int(bx)
         by2 = int(by + 17)
         book.append([bx, by, bx2,by2, P.dx,P.dy])
         P.shoot = 1.0
         books -= 1
    elif books == 0:
        if keys[pygame.K_SPACE] and P.shoot <= 0:
            books = 0
    P.book_update(book,dt,win_width, win_height,M.mCamera)


    # Drawing
    screen.fill((0,0,0))
    M.draw(screen)
    P.render(screen, dt)
    P.draw_bullets(book, screen, M.mCamera)
    for i in npc:
        i.draw(screen,dt)
    if not P.mMap.isPickupable((P.mPos[0], P.mPos[1], P.mDim[0], P.mDim[1])):
        # pygame.mixer.Sound.play(sound)
        # pygame.mixer.music.stop()
        books += 1
    if not P.mMap.Warpable((P.mPos[0], P.mPos[1], P.mDim[0], P.mDim[1])):
        P.mMap.Warp(P)
        if P.mMap.mFName == "maps\\ATCfirstfloor.txt":
            npc = npc_create("npcatclower")
            for i in npc:
                P.mMap.addnpc(i)
        elif P.mMap.mFName == "maps\\School_Test_Map.txt":
            npc = npc_create("npcfile.txt")
            for i in npc:
                P.mMap.addnpc(i)


    # Debug text to show on-screen
    text = "camera: [" + str(int(M.mCamera[0])) + ", " + str(int(M.mCamera[1])) + "]"
    screen.blit(font.render(text, False, (255,255,255)), (0,0))
    text = "player: [" + str(int(P.mPos[0]/32)) + ", " + str(int(P.mPos[1]/32)) + "]"
    screen.blit(font.render(text, False, (255,255,255)), (150, 0))
    text = "fps: " + str(int(clock.get_fps()))
    screen.blit(font.render(text, False, (255,255,255)), (0, 13))
    book_amount = "Books: " + str(books)
    screen.blit(font.render(book_amount,False,(255,255,255)), (150, 13))


    # if keys[pygame.K_f]:
    #     while True:
    #         pygame.draw.rect(screen, (125,125,0), (50,50,450,450), 0)
    #         text = "Books: [" + str(books) + "]"
    #         screen.blit(font1.render(text, False, (255, 255, 255)), (50, 50))
    #         keys = pygame.key.get_pressed()
    #         pygame.display.flip()
    #         pygame.event.pump()
    #         if keys[pygame.K_RETURN]:
    #             break


    if keys[pygame.K_p]:
        while True:
            keys = pygame.key.get_pressed()
            screen.blit(paul,(-100,0))
            screen.blit(paul, (500, 0))
            pygame.display.flip()
            pygame.event.pump()

            if keys[pygame.K_i]:
                break

    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()
