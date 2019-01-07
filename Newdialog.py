import pygame

pygame.init()

class dialog:
    def __init__(self,file,clock):
        fp = open("dialogfile\\"+file)
        self.mMasterClock = clock
        self.dict = {}
        self.numb = 0
        self.c = 0
        for line in fp:
            line = line.strip()
            if line.count(":") != 1:
                continue
            a = line.split(":")
            if a[0] == "n":
                self.numb = int(a[1])

            if a[0]== "c":
                self.c = int(a[1])
            if a[0][0] == "a" or a[0][0] == "q" or a[0] =="s" :
                self.dict[a[0]] = a[1]

    def blitthis (self,screen,dia,pos=(75, 600)):
        #temp font
        my_font = pygame.font.SysFont("Comic Sans", 40)

        diasurf = my_font.render(dia,False,(255,255,255))
        screen.blit(diasurf,pos)

    def choice (self,screen):
        start = ()
        phase = 0
        key = pygame.event.poll()
        pressed = 100000
        if phase == 0:
            while phase ==0:
                pygame.draw.rect(screen, (0, 0, 0), (50, 590, 950, 175), 0)
                pygame.draw.rect(screen, (255, 255, 255), (55, 595, 940, 165), 1)
                key = pygame.event.poll()

                self.blitthis(screen,str(self.dict["s"]))
                for i in range(self.c):
                    self.blitthis(screen,str(i+1)+"."+str(self.dict["a"+str(phase+i+1)]),(75,600+40*(i+1)))
                if key.type == pygame.KEYDOWN:
                    if key.key == pygame.K_1:
                        pressed = 1
                    if key.key == pygame.K_2:
                        pressed = 2
                    if key.key == pygame.K_3:
                        pressed = 3
                    if key.key == pygame.K_4:
                        pressed = 4
                    if key.key == pygame.K_5:
                        pressed = 5
                    if key.key == pygame.K_6:
                        pressed = 6
                    if key.key == pygame.K_7:
                        pressed = 7
                    if key.key == pygame.K_8:
                        pressed = 8
                    if key.key == pygame.K_9:
                        pressed = 9
                    else:
                        pass
                    if pressed > self.c:
                        pass
                    elif pressed <= self.c:
                        phase +=1


                pygame.event.pump()
                pygame.display.update()

        while phase > 0 and phase < self.numb-1:
            pygame.draw.rect(screen, (0, 0, 0), (50, 590, 950, 175), 0)
            pygame.draw.rect(screen, (255, 255, 255), (55, 595, 940, 165), 1)
            key = pygame.event.poll()
            pygame.event.pump()
            self.blitthis(screen,str(self.dict["q"+str(pressed+self.c*(phase-1))]))
            for i in range(self.c):
                self.blitthis(screen,str(i+1)+"."+ str(self.dict["a" + str((i+1)+self.c*phase)]), (75, 600 + 40 * (i+1)))
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_1:
                    pressed = 1
                if key.key == pygame.K_2:
                    pressed = 2
                if key.key == pygame.K_3:
                    pressed = 3
                if key.key == pygame.K_4:
                    pressed = 4
                if key.key == pygame.K_5:
                    pressed = 5
                if key.key == pygame.K_6:
                    pressed = 6
                if key.key == pygame.K_7:
                    pressed = 7
                if key.key == pygame.K_8:
                    pressed = 8
                if key.key == pygame.K_9:
                    pressed = 9
                if pressed > self.c:
                    pass
                elif pressed <= self.c:
                    phase +=1
                    break
            pygame.display.update()
        while phase == self.numb-1:
            pygame.draw.rect(screen, (0, 0, 0), (50, 590, 950, 175), 0)
            pygame.draw.rect(screen, (255, 255, 255), (55, 595, 940, 165), 1)
            key = pygame.event.poll()
            pygame.event.pump()
            self.blitthis(screen, str(self.dict["q" + str(pressed+self.c*(phase-1))]))
            self.blitthis(screen, "Press E to exit",(100, 600 + 60 * 1))
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_e:
                    phase+=1
                    break
            self.mMasterClock.tick()
            pygame.display.update()



def convo(screen,file,clock):
    var = dialog(file,clock)
    var.choice(screen)






            # pygame.event.pump()



if __name__ == "__main__":
    while True:
        screen = pygame.display.set_mode((1024,768))
        convo(screen,"jasonsdia.txt")


    # some = "s"











