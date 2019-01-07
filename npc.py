
from vector import *
import pygame




class npc:
    def __init__(self,name,cord,sprite,vectorlist,dir,start):
        self.name = name
        self.cord = cord

        self.sprite = sprite
        self.vectorlist = vectorlist
        self.nMap = None
        self.dir = 0
        self.distance = 0
        self.norm = 0
        self.mag = 0
        self.start = start
        self.currentframe = 0
        self.animationtimer = 0
        self.index = 0
        self.zero = True
        self.direction = "up"
        self.times = 0
        self.sprite_dir = self.sprite[1,0]
    # def npctalking(self,playerpos,npcpos,distancesq):
    #     p = Vector2(playerpos[0],playerpos[1])
    #     n = Vector2(npcpos[0],npcpos[1])
    #     temp = p - n
    #     print(dot(p,n))
    #     if dot(p,n) < distancesq:
    #         print("oi")
    #         return False
    #     else:
    #         return True
    #WIP
    def draw (self,screen, dt):
        self.animationtimer += dt
        if self.animationtimer > 0.2:
            self.currentframe = self.currentframe + 1
            if self.currentframe == 2:
                self.currentframe = 0
            self.animationtimer = 0
        #print(self.currentframe)
        if len(self.vectorlist) == 0:
            screen.blit(self.sprite[(0,-1)][1], self.mMap.get_screen_pos(self.cord[0], self.cord[1]))
        elif len(self.vectorlist)>= 1:
            self.move(dt)
            # print(self.currentframe)
            screen.blit(self.sprite_dir[self.currentframe], self.mMap.get_screen_pos(self.cord[0], self.cord[1]))




    # def move(self, dt,):
    #     self.animationtimer += dt

    def move(self, dt):

        if self.distance >= self.mag and self.times != 0:
            self.dir = 0

            if self.index < len(self.vectorlist) and self.zero:
                self.index +=1
                self.directon ="up"
                if self.index == len(self.vectorlist)-1:
                    self.direction = "down"
                    self.zero = False
            elif self.index == len(self.vectorlist) or not self.zero:
                if self.index >=1:
                    self.index -= 1
                    self.direction = "down"
                if self.index == 0:
                    self.zero = True
                    self.direction = "up"
        # elif self.distance >= self.mag and len(self.vectorlist)==2:
        #     i = self.vectorlist[1] - self.vectorlist[0]
        #     p = self.vectorlist[0] - self.vectorlist[1]
        #
        #     if self.norm == i.normalized:
        #         i = p
        #         self.start = self.vectorlist[1]
        #         self.sprite_dir = self.sprite[0, -1]
        #         # print(self.sprite_dir)
        #     else:
        #         i = self.vectorlist[1] - self.vectorlist[0]
        #         self.start = self.vectorlist[0]
        #         self.sprite_dir = self.sprite[0, 1]
        #         # print(self.sprite_dir)
        #     self.norm = i.normalized
        #     self.mag = i.magnitude
        #     self.distance = 0
        #     self.dir = 1




        #if npc is on the endpoints
        if self.dir == 0:
            # print(self.direction)
            if self.direction == "down":
                i = self.vectorlist[self.index-1] - self.vectorlist[self.index]
                self.start = self.vectorlist[self.index]
                if self.vectorlist[self.index][1] == self.vectorlist[self.index-1][1]:
                    if self.vectorlist[self.index][0] >= self.vectorlist[self.index-1][0]:
                        self.sprite_dir = self.sprite[-1,0]
                    elif self.vectorlist[self.index][0] <= self.vectorlist[self.index-1][0]:
                        self.sprite_dir = self.sprite[1,0]

                elif self.vectorlist[self.index][0] == self.vectorlist[self.index-1][0]:
                    if self.vectorlist[self.index][1] >= self.vectorlist[self.index-1][1]:
                        self.sprite_dir = self.sprite[0,1]
                    elif self.vectorlist[self.index][1] <= self.vectorlist[self.index-1][1]:
                        self.sprite_dir = self.sprite[0,-1]
            elif self.direction == "up":
                i = self.vectorlist[self.index + 1] - self.vectorlist[self.index]
                self.start = self.vectorlist[self.index]
                if self.vectorlist[self.index][1] == self.vectorlist[self.index+1][1]:
                    if self.vectorlist[self.index][0] >= self.vectorlist[self.index+1][0]:
                        self.sprite_dir = self.sprite[-1,0]
                    elif self.vectorlist[self.index][0] <= self.vectorlist[self.index+1][0]:
                        self.sprite_dir = self.sprite[1,0]

                elif self.vectorlist[self.index][0] == self.vectorlist[self.index+1][0]:
                    if self.vectorlist[self.index][1] >= self.vectorlist[self.index+1][1]:
                        self.sprite_dir = self.sprite[0,1]
                    elif self.vectorlist[self.index][1] <= self.vectorlist[self.index+1][1]:
                        self.sprite_dir = self.sprite[0,-1]
            self.norm = i.normalized
            self.mag = i.magnitude
            self.distance = 0
            self.dir = 1
            self.times += 1
        #if npc is not on endpoints
        elif self.dir == 1:
            self.distance += 50 * dt
            #print(self.distance)
            self.cord = self.norm * self.distance + self.start

def npc_create(file):
    fp = open(file)
    list = []
    sprite = {(0, 1): [], (0, -1): [], (1, 0): [], (-1, 0): []}
    vectorlist = []
    for line in fp:
        line = line.strip()
        var = line.split("=")
        if var[0] == "name ": name = var[1]
        if var[0] == "cord ":
            if line.count(",") > 1:
                t = var[1].split(" ")
                for i in t:
                    g = i.split(",")
                    vec = Vector(int(g[0]) * 32, int(g[1]) * 32)
                    vectorlist.append(vec)
                cord = vectorlist[0]
            else:
                t = var[1].split(",")
                cord = Vector2(int(t[0]) * 32, int(t[1]) * 32)
        # if var[0] == "dialog ": dialog = Dialog(var[1])
        if var[0] == "sprite_down ": sprite[0, -1].append(pygame.image.load(var[1]))
        if var[0] == "sprite_up ": sprite[0, 1].append(pygame.image.load(var[1]))
        if var[0] == "sprite_right ": sprite[1, 0].append(pygame.image.load(var[1]))
        if var[0] == "sprite_left ": sprite[-1, 0].append(pygame.image.load(var[1]))
        if line[0:6] == "break":
            start = cord
            i = npc(name, cord, sprite, vectorlist, dir, start)
            list.append(i)
            vectorlist = []
            sprite = {(0, 1): [], (0, -1): [],(1,0):[],(-1,0):[]}
    fp.close()
    return list



# if __name__ == "__main__":
#     test = npc_create("npcfile.txt")
#     test.setvar()
#     screen = pygame.display.set_mode((800,600))
#     while True:
#         test.draw(screen)
#         pygame.display.update()
#     print(test)
    # print(test.name)
    # print(test.cord)
    # print(test.dialog)
    # print(test.npc_list)
    # test.select("name")
    # print(test.name)
    # print(test.cord)
    # print(test.dialog)
